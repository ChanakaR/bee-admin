import json

class JSONReaderTemplate:
    json_file_path = "./config/"
    
    def getJSONContent(self,file_name):
        file_full_path = self.json_file_path + file_name
        with open(file_full_path) as f :
            file_content = json.load(f)
        return file_content
