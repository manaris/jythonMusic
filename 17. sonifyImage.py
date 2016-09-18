# sonifyImage.py
#
# Demonstrates how to create a soundscape from an image.  
# It also demonstrates how to use functions.
# It loads a jpg image and scans it from left to right.  
# Pixels are mapped to notes using these rules:
# 
# + left-to-right column position is mapped to time,
# + luminosity (pixel brightness) is mapped to pitch within a scale, 
# + redness (pixel R value) is mapped to duration, and 
# + blueness (pixel B value) is mapped to volume.
#
 
from music import *
from image import *
from random import *
 
##### define data structure
soundscapeScore = Score("Loutraki Soundscape", 60)
soundscapePart  = Part(PIANO, 0) 
 
##### define  musical parameters
scale = MIXOLYDIAN_SCALE
 
minPitch = 0        # MIDI pitch (0-127)
maxPitch = 127
 
minDuration = 0.8   # duration (1.0 is QN)
maxDuration = 6.0
 
minVolume = 0       # MIDI velocity (0-127)
maxVolume = 127
 
# start time is randomly displaced by one of these 
# durations (for variety)
timeDisplacement = [DEN, EN, SN, TN]
 
##### read in image (origin (0, 0) is at top left)
image = Image("soundscapeLoutrakiSunset.jpg")
 
# specify image pixel rows to sonify - this depends on the image!
pixelRows = [0, 53, 106, 159, 212]
width = image.getWidth()     # get number of columns in image
height = image.getHeight()   # get number of rows in image
 
##### define function to sonify one pixel
# Returns a note from sonifying the RGB values of 'pixel'.
def sonifyPixel(pixel):
 
   red, green, blue = pixel  # get pixel RGB value
 
   luminosity = (red + green + blue) / 3   # calculate brightness
      
   # map luminosity to pitch (the brighter the pixel, the higher
   # the pitch) using specified scale
   pitch = mapScale(luminosity, 0, 255, minPitch, maxPitch, scale)
 
   # map red value to duration (the redder the pixel, the longer 
   # the note)
   duration = mapValue(red, 0, 255, minDuration, maxDuration)
 
   # map blue value to dynamic (the bluer the pixel, the louder 
   # the note)      
   dynamic = mapValue(blue, 0, 255, minVolume, maxVolume)
   
   # create note and return it to caller
   note = Note(pitch, duration, dynamic)   
   
   # done sonifying this pixel, so return result
   return note
   
##### create musical data
 
# sonify image pixels
for row in pixelRows:   # iterate through selected rows
 
   for col in range(width):  # iterate through all pixels on this row
   
      # get pixel at current coordinates (col and row)
      pixel = image.getPixel(col, row)
     
      # sonify this pixel (we get a note)
      note = sonifyPixel(pixel)
 
      # wrap note in a phrase to give it a start time
      # (Phrases have start time, Notes do not)
 
      # use column value as note start time (e.g., 0.0, 1.0, and so on)
      startTime = float(col)   # phrase start time is a float
      
      # add some random displacement for variety
      startTime = startTime + choice( timeDisplacement )
       
      phrase = Phrase(startTime)   # create phrase with given start time
      phrase.addNote(note)         # and put the note in it 
                         
      # put result in part
      soundscapePart.addPhrase(phrase)
         
   # now, all pixels on this row have been sonified
 
# now, all pixelRows have been sonified, and soundscapePart 
# contains all notes
 
##### combine musical material
soundscapeScore.addPart(soundscapePart)
 
##### view score and write it to an audio and MIDI files
Play.midi(soundscapeScore)