import os
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            overall_validation_status = True

            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            
            with open(self.config.STATUS_FILE, 'w') as f:
                
                for file in self.config.ALL_REQUIRED_FILES:
                    if file not in all_files:
                        file_status = False
                        overall_validation_status = False
                    else:
                        file_status = True
                    
                    f.write(f"Folder/file name: {file} \t Status: {file_status}\n")
            
            return overall_validation_status
        
        except Exception as e:
            raise e