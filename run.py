#!/usr/bin/python

import os
import json

from classes.ServerAdmin import ServerAdmin

# command = 'ls -la'
# os.system(command)

serverAdmin = ServerAdmin()
serverAdmin.login("Artemis")
