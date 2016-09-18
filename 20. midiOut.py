# midiOut.py
#
# Demonstrates how to play a note on an external MIDI synthesizer.
#

from midi import *
from music import *  # for C4 symbol

midiOut = MidiOut() 

# play C4 note starting now for 1000ms 
# with volume 127 on channel 0 
midiOut.playNote(C4, 0, 1000, 127, 0)