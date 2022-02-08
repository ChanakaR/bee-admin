#!/usr/bin/python3
import sys
from classes.ServerAdministrator import ServerAdministrator

serverName = sys.argv[1] 
serverAdmin = ServerAdministrator()
serverAdmin.loginToServer(serverName)
