#Importar modulos
from ast import Import
from importlib import import_module
from multiprocessing.dummy import Process
from platform import platform


import platform
import os
import getpass


ProcessList= [os.popen('wmic process get description, processid').read()]
SistemaOP = [platform.uname()]
ProcessInfo = SistemaOP[0].processor
user = getpass.getuser()
NameOS = platform.system()
VersionOS = platform.version()
#print(NameOS, VersionOS, user, ProcessInfo)

