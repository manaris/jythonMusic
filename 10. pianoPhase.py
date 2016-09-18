# pianoPhase.py
# Plays Steve Reich's minimalist piece, Piano Phase (1967).
 
from music import *
 
pianoPart = Part(PIANO, 0) # create piano part
 
phrase1 = Phrase(0.0)      # create two phrases
phrase2 = Phrase(0.0)
 
# write music in a convenient way
pitchList    = [E4, FS4, B4, CS5, D5, FS4, E4, CS5, B4, FS4, D5, CS5]
durationList = [SN, SN,  SN, SN,  SN, SN,  SN, SN,  SN, SN,  SN, SN]
 
# add the same notes to both phrases
phrase1.addNoteList(pitchList, durationList)
phrase2.addNoteList(pitchList, durationList)
 
Mod.repeat(phrase1, 41)   # repeat first phrase 41 times
Mod.repeat(phrase2, 41)   # repeat second phrase 41 times
 
phrase1.setTempo(100.0)   # set tempo to 100 beats-per-minute
phrase2.setTempo(100.5)   # set tempo to 100.5 beats-per-minute
 
pianoPart.addPhrase(phrase1)   # add phrases to part
pianoPart.addPhrase(phrase2)
 
Play.midi(pianoPart)      # play music