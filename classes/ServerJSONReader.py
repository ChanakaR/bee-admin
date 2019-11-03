from JSONReaderTemplate import JSONReaderTemplate

class ServerJSONReader(JSONReaderTemplate):
    file_name = "servers.json"

    def getServers(self):
        servers = self.getJSONContent(self.file_name)
        return servers
