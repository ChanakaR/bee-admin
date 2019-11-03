import os
from ServerPool import ServerPool

class ServerAdministrator:
    
    def __init__(self):

    def loginToServer(self,server_name):
        self.getServerDetails(server_name)

    def getServerDetails(self,server_name):
        self.server = self.jsonReader.getJSONContent("servers.json")


