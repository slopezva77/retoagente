#Importar modulos
from ast import Import
from importlib import import_module
from multiprocessing.dummy import Process
from platform import platform


import platform
import os


ProcessInfo = [os.popen('wmic process get description, processid').read()]
SistemaOP = [platform.uname()]
print(SistemaOP)

