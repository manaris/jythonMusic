# midiIn1.py
#
# Demonstrates how to run arbitrary code when the user plays a note 
# on a MIDI piano (or other MIDI instrument).
#

from midi import *

midiIn = MidiIn()     

def printNote(eventType, channel, data1, data2):
   print "pitch =", data1, "volume =", data2

midiIn.onNoteOn(printNote)