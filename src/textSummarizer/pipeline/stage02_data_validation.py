from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        data_ingestion = DataValidation(config=data_validation_config)

        status = data_ingestion.validate_all_files_exist()
        
        if status:
            logger.info("All required files/folders exist")
        else:
            logger.info("Some required files/folders missing")