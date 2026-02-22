from textSummarizer.pipeline.stage04_model_trainer import ModelTrainingPipeline
from textSummarizer.pipeline.prediction import PredictionPipeline
from textSummarizer.logging import logger
from datasets import load_from_disk
import os
import random


# STAGE_NAME = "Data Ingestion Stage"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     data_ingestion = DataIngestionPipeline()
#     data_ingestion.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(f"Error in stage {STAGE_NAME}: {e}")
#     raise e



# STAGE_NAME = "Data Validation Stage"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     data_validation = DataValidationPipeline()
#     data_validation.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(f"Error in stage {STAGE_NAME}: {e}")
#     raise e



# STAGE_NAME = "Data Transformation Stage"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     data_transformation = DataTransformationPipeline()
#     data_transformation.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(f"Error in stage {STAGE_NAME}: {e}")
#     raise e


# STAGE_NAME = "Model Training Stage"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     model_training = ModelTrainingPipeline()
#     model_training.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(f"Error in stage {STAGE_NAME}: {e}")
#     raise e


STAGE_NAME = "Prediction Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    
    # Load dataset sample
    dataset_path = os.path.join("artifacts", "data_ingestion", "samsum_dataset")
    dataset = load_from_disk(dataset_path)
    
    # Pick a random sample from the test set
    test_data = dataset['test']
    sample_idx = random.randint(0, len(test_data) - 1)
    
    sample_dialogue = test_data[sample_idx]['dialogue']
    reference_summary = test_data[sample_idx]['summary']
    
    prediction = PredictionPipeline()
    model_summary = prediction.predict(sample_dialogue)
    
    print("\n" + "="*50)
    print(f"FINAL INFERENCE RESULTS (Sample Index: {sample_idx})")
    print("="*50)
    print(f"DIALOGUE:\n{sample_dialogue}")
    print("-"*50)
    print(f"GROUND TRUTH SUMMARY:\n{reference_summary}")
    print("-"*50)
    print(f"MODEL SUMMARY:\n{model_summary}")
    print("="*50)

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"Error in stage {STAGE_NAME}: {e}")
    raise e