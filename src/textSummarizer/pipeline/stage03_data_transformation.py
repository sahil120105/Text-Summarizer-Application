from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.entity import DataTransformationConfig 
from textSummarizer.components.data_transformation import DataTransformation

class DataTransformationPipeline:

    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        data_transformation_config = config_manager.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.tokenize()