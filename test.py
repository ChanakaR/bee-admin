#!/usr/bin/python

import os
from classes.ServerAdmin import ServerAdmin
command = 'ls -la'
os.system(command)

serverAdmin = ServerAdmin()
serverAdmin.login("Server Name")

