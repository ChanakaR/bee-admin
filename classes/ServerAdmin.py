from .JSONReaderTemplate import JSONReaderTemplate

class ServerAdmin:
    species = "bird"

    def __init__(self):
        self.jsonReader = JSONReaderTemplate()
    
    def login(self,server_name):
        self.getServerDetails(server_name)

    def getServerDetails(self,server_name):
        self.jsonReader.getJSONContent("servers.json")


