import json
import os

class JSONReaderTemplate:
    json_file_path = os.path.dirname(os.path.realpath(__file__)) + "/../config/"
    print(os.path.dirname(os.path.realpath(__file__)))

    def getJSONContent(self,file_name):
        file_full_path = self.json_file_path + file_name
        with open(file_full_path) as f :
            file_content = json.load(f)
        return file_content
