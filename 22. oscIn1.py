# oscIn1.py
# 
# Demonstrates how to run some code when a particular OSC message arrives.
#

from osc import *

oscIn = OscIn( 57110 ) 

def simple(message): 
 print "Hello world!"

oscIn.onInput("/helloWorld", simple)