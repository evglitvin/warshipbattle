import yaml

class Config:

    def __init__(self, path="lin/config/config.yaml"):
        self.path = path
        self.data = self.read()

    def read(self):
        with open(self.path, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as e:
                print(e)
