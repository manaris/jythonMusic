# sinewavePatchTest.py

from music import *

# for RT Mixer and RT Line
from jm.audio import *
from jm.music.rt import *

# out RT instrument with setFrequency() and setVolume()
import SinewaveInstrument


class SinewavePatch(RTLine):

   def __init__(self, frequency=440.0, envelopePoints = [0.0, 0.0, 
                                                         0.01, 1.0, 
                                                         0.99, 1.0, 
                                                         1.0, 0.0], 
                      sampleRate=44100, channels=2):              

      self.inst = SinewaveInstrument(sampleRate, channels, envelopePoints, frequency)

      RTLine.__init__(self, [self.inst])
      mixer = RTMixer( [self] )
      mixer.begin()

   def getNextNote(self):
      
      # generate a continuous flow of long notes
      n =  Note( inst.getFrequency(), WN*1000, 127)
      #n =  Note( int(random() * 12 + 60), WN*1000)
      return n


SinewavePatch()                       # and play random music with it

#inst = SimpleFMInst(44100, 800, 34.4)  # create an instrument
#MyLine( [inst] )                       # and play random music with it

# and another
#inst = SimpleFMInst(44100, 800, 34.4)  # create an instrument
#MyLine( [inst] )                       # and play random music with it

# and another
#inst = SimpleFMInst(44100, 800, 34.4)  # create an instrument
#MyLine( [inst] )                       # and play random music with it
