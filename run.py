#!/usr/bin/python

import os
import json

from classes.ServerAdmin import ServerAdmin

command = 'ls -la'
os.system(command)

serverAdmin = ServerAdmin()
serverAdmin.login("Server Name")

with open('./config/servers.json') as f :
    data = json.load(f)

if "Artemis" in data:
    print data["Artemis"]["IP"]
