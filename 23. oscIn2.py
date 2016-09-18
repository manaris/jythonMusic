# oscIn2.py
#
# Demonstrates how to see what type of messages an OSC device 
# (e.g., a smartphone app) generates.
#

from osc import *

oscIn = OscIn( 57110 )

def printMessage(message):    
   address = message.getAddress()
   args    = message.getArguments()
   print "OSC message:", address,         
   for i in range( len(args) ):            
      print args[i],
   print

oscIn.onInput("/.*", printMessage)