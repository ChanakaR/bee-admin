from ServerPool import ServerPool
from Utils.Color import bcolors

class ServerAdministrator:
    
    def __init__(self):
        self.serverPool = ServerPool()

    def loginToServer(self,server_name):
        if (self.serverPool.isServerAvailable(server_name)):
            print bcolors.OKBLUE + 'LOG INTO THE SERVER ' + server_name + bcolors.ENDC
            server = self.serverPool.getServer(server_name)
            server.login()
        else:
            print bcolors.FAIL + 'Sorry!, REQUESTED SERVER IS NOT AVAILABLE' + bcolors.ENDC

