# changesByTupac.py
# Plays main chord progression from 2Pac's "Changes" (1998).
 
from music import *
 
mPhrase = Phrase()
mPhrase.setTempo(105)
 
# section 1 - chords to be repeated
pitch1 = [[E4,G4,C5], [E4,G4,C5], [D4,G4,B4], A4, G4, [D4, FS4, A4], 
           [D4, G4, B4], [C4, E4, G4], E4, D4, C4, [G3, B4, D4]]
dur1   = [DEN,        DEN,        HN,         SN, SN, DEN,         
           DEN,          DQN,          EN, SN, SN, DQN]

# section 2 - embellishing notes
pitch2 = [A4, B4]
dur2   = [SN, SN] 
 
mPhrase.addNoteList(pitch1, dur1)  # add section 1 
mPhrase.addNoteList(pitch2, dur2)  # add section 2
mPhrase.addNoteList(pitch1, dur1)  # again, add section 1
 
Play.midi(mPhrase)