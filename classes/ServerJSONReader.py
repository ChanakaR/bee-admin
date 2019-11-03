from JSONReaderTemplate import JSONReaderTemplate

class ServerJSONReader(JSONReaderTemplate):
    file_name = "server.json"

    def __init__(self):

    def getServers(self):
        servers = self.getJSONContent(self.file_name)
        return servers
