# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 06:32:51 2022

@author: Ghost
"""



"""
LIBRARIES

Here come the importations of libraries.
"""
import numpy
import scipy
import ast
import datetime
import pandas
import tensorflow as tf
import pyttsx3
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import AsyncIOOSCUDPServer
import asyncio
import threading

"""
GLOBAL VARIABLES

Here go the declarations of global variables.
"""
mood = float
athena = pyttsx3.init()



# Strings, just an absolute fuck ton of strings
init_complete = "System initialization complete. Ready for deployment."
security_mode = "Entering security mode."
unauthorized = "Unauthorized user. Initiating security protocol."



"""
ATHENA CONFIG
"""
voices = athena.getProperty('voices')
athena.setProperty('voice', voices[1].id)



rate = athena.getProperty('rate')
print(rate)
athena.setProperty('rate', 230)

volume = athena.getProperty('volume')
print(volume)
athena.setProperty('volume', 1.0)


"""
CLASS DEFINITIONS

Here go class definitions.
"""

class RunThread(threading.Thread):
    def __init__(self, func, args, kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        super().__init__()
        
    def run(self):
        self.result = asyncio.run(self.func(*self.args, **self.kwargs))


"""
FUNCTION DEFINITIONS

Here go function definitions.
"""

def filter_handler(address, *args):
    """
    Takes an OSC address and args and prints args as formatted string.
    """
    print(f"{address}: {args}")

def run_async(func, *args, **kwargs):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None
    if loop and loop.is_running():
        thread = RunThread(func, args, kwargs)
        thread.start()
        thread.join()
        return thread.result
    else:
        return asyncio.run(func(*args, **kwargs))


def respond():
    return(True)


"""
MAIN
"""
dispatcher = Dispatcher()
dispatcher.map("/filter", filter_handler)

ip = "127.0.0.1"
port = 1337

async def loop():
    """Example main loop that only runs for 10 iterations before finishing"""
    for i in range(3):
        print("Initializing...")
        await asyncio.sleep(1)
        
async def init_main():
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint() # Create datagram endpoint and start serving
    await loop() # Enter main loop of program
    transport.close() # Clean up serve endpoint
   
async def test(name):
    await asyncio.sleep(5)
    return f"hello {name}"

run_async(init_main)




print(init_complete)
athena.say(init_complete)
athena.runAndWait()




"""
UNIT TESTS

Here go unit tests.
"""