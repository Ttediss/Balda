import os
import shutil
from const import *

def list_my_progs():
    list_prog = []
    for filename in os.listdir(Command_arch):
        print(filename)
        list_prog.append(filename)
    return list_prog

def execute_file(file_name):
    shutil.copy2(Command_arch+"\\"+file_name, Command)
