import yaml
from pathlib import Path

class config_helper:

    def read_confing(self,attribute: str):
        filePath = Path(__file__).with_name('config.yaml')
        with filePath.open('r') as f:
            data = yaml.safe_load(f)
            return data[attribute]