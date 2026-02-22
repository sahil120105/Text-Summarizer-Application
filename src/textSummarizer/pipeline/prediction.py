from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_prediction_config()


    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)

        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        
        with torch.no_grad():
            output_ids = model.generate(
                **inputs,
                **gen_kwargs
            )

        output = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        return output
