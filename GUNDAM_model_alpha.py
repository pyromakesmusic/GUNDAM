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


"""
GLOBAL VARIABLES

Here go the declarations of global variables.
"""
mood = float


"""
FUNCTION DEFINITIONS

Here go function definitions.
"""




"""
MAIN FUNCTION CALLS
"""

athena = pyttsx3.init()
voices = athena.getProperty('voices')
athena.setProperty('voice', voices[1].id)
athena.say("Platform initialized.")
athena.runAndWait()




"""
UNIT TESTS

Here go unit tests.
"""
print("Hello World!")