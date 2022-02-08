from .ServerJSONReader import ServerJSONReader
from .Server import Server

class ServerPool:
    def __init__(self):
        self.serverJSONReader = ServerJSONReader()
        self.servers = self.serverJSONReader.getServers()
    
    def isServerAvailable(self,server_name):
        if server_name in self.servers:
            return True
        return False

    def getServer(self,server_name):
        if(self.isServerAvailable(server_name)):
            server = Server(self.servers[server_name]["IP"],self.servers[server_name]["PORT"])
            return server

    