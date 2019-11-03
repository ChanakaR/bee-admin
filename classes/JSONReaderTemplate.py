import json
import os

class JSONReaderTemplate:
    json_file_path = "/home/chanaka/Projects/Workspace/bee-admin/config/"

    def getJSONContent(self,file_name):
        file_full_path = self.json_file_path + file_name
        with open(file_full_path) as f :
            file_content = json.load(f)
        return file_content
