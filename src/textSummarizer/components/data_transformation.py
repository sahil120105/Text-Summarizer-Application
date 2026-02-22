from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.entity import DataTransformationConfig
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def tokenize_content(self,data):
        dialogues = data['dialogue']
        summaries = data['summary']

        inputs = ["summarize: " + d if d else "summarize: " for d in dialogues]
        targets = [s if s else "" for s in summaries]

        # Tokenize WITHOUT padding="max_length"
        input_encodings = self.tokenizer(
            inputs,
            max_length=1024,
            truncation=True
        )

        target_encodings = self.tokenizer(
            text_target=targets,
            max_length=128,
            truncation=True
        )

        # Just return the raw lists. No manual -100 replacement needed!
        return {
            "input_ids": input_encodings["input_ids"],
            "attention_mask": input_encodings["attention_mask"],
            "labels": target_encodings["input_ids"]
        }

    def tokenize(self):
        logger.info("Loading dataset from disk...")
        dataset = load_from_disk(self.config.data_path)

        logger.info("Tokenizing the dataset...")
        tokenized_dataset = dataset.map(
            self.tokenize_content,
            batched=True
        )

        logger.info("Saving tokenized dataset to disk...")
        tokenized_dataset.save_to_disk(self.config.root_dir)