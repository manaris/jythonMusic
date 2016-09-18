# oscOut.py

from osc import *

oscOut = OscOut("localhost", 57110) 

oscOut.sendMessage("/helloWorld")
oscOut.sendMessage("/test", 1, 2, 3)
oscOut.sendMessage("/itsFullOfStars", 1, 2.35, "wow!", True)