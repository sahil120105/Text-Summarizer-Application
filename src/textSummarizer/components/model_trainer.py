from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer, DataCollatorForSeq2Seq
import torch
import evaluate
import nltk
import numpy as np
from nltk.tokenize import sent_tokenize
from datasets import load_from_disk
from textSummarizer.entity import ModelTrainingConfig
from textSummarizer.logging import logger

class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)

    def evaluate(self, eval_pred):
        # Download the NLTK punctuation tokenizer and the required punkt_tab
        nltk.download("punkt")
        nltk.download("punkt_tab")

        # Load the ROUGE metric
        rouge_metric = evaluate.load("rouge")

        predictions, labels = eval_pred

        # Fix: Ensure predictions are within the valid tokenizer vocabulary range to avoid OverflowError
        vocab_size = len(self.tokenizer)
        predictions = np.clip(predictions, 0, vocab_size - 1)

        # 1. Decode the model's predictions back into text
        decoded_preds = self.tokenizer.batch_decode(predictions, skip_special_tokens=True)

        # 2. Replace the -100s in the labels back to pad_token_id
        labels = np.where(labels != -100, labels, self.tokenizer.pad_token_id)
        labels = np.clip(labels, 0, vocab_size - 1)
        decoded_labels = self.tokenizer.batch_decode(labels, skip_special_tokens=True)

        # 3. ROUGE-Lsum expects text to have newlines between sentences
        decoded_preds = ["\n".join(sent_tokenize(pred.strip())) for pred in decoded_preds]
        decoded_labels = ["\n".join(sent_tokenize(label.strip())) for label in decoded_labels]

        # 4. Calculate the ROUGE scores
        result = rouge_metric.compute(
            predictions=decoded_preds,
            references=decoded_labels,
            use_stemmer=True,
            rouge_types=["rouge1", "rouge2", "rougeL", "rougeLsum"]
        )

        # 5. Scale to percentages
        result = {key: value * 100 for key, value in result.items()}

        prediction_lens = [np.count_nonzero(pred != self.tokenizer.pad_token_id) for pred in predictions]
        result["gen_len"] = np.mean(prediction_lens)

        return {k: round(v, 4) for k, v in result.items()}

    
    def train(self):
        seq2seq_data_collator = DataCollatorForSeq2Seq(self.tokenizer, model=self.model, label_pad_token_id=-100)
        
        training_args = Seq2SeqTrainingArguments(
            output_dir= self.config.output_dir,
            num_train_epochs= self.config.num_train_epochs,
            per_device_train_batch_size= self.config.per_device_train_batch_size,
            per_device_eval_batch_size= self.config.per_device_eval_batch_size,
            warmup_steps= self.config.warmup_steps,
            weight_decay= self.config.weight_decay,
            logging_steps= self.config.logging_steps,
            eval_steps= self.config.eval_steps,             
            save_steps= self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            report_to=self.config.report_to,
            eval_strategy=self.config.eval_strategy,
            predict_with_generate=self.config.predict_with_generate,
            generation_max_length=self.config.generation_max_length
        )

        logger.info("Loading tokenized data...")

        tokenized_data = load_from_disk(self.config.data_path)

        trainer = Seq2SeqTrainer(
            model=self.model,
            args=training_args,
            processing_class=self.tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=tokenized_data["train"],
            eval_dataset=tokenized_data["validation"],
            compute_metrics= self.evaluate
        )

        logger.info(f"Starting Trainig ({self.config.num_train_epochs} epochs)...")
        trainer.train()