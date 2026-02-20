from textSummarizer.pipeline.stage01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.stage02_data_validation import DataValidationPipeline
from textSummarizer.logging import logger


# STAGE_NAME = "Data Ingestion Stage"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     data_ingestion = DataIngestionPipeline()
#     data_ingestion.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(f"Error in stage {STAGE_NAME}: {e}")
#     raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"Error in stage {STAGE_NAME}: {e}")
    raise e