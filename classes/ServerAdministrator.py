from ServerPool import ServerPool

class ServerAdministrator:
    
    def __init__(self):
        self.serverPool = ServerPool()

    def loginToServer(self,server_name):
        if (self.serverPool.isServerAvailable(server_name)):
            server = self.serverPool.getServer(server_name)
            server.login()
        else:
            print "Sorry Server is not available"


