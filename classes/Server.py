import os

class Server:
    
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port

    def login (self):
        cmd = "ssh -p " + str(self.port) + " chanaka@" + str(self.ip)
        os.system(cmd) 