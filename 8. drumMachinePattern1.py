# drumMachinePattern1.py
#
# Implements a drum-machine pattern consisting of bass (kick),
# snare and hi-hat sounds. It uses notes, three phrases, a part and
# a score, with each layer adding additional rhythms.
 
from music import *
 
repetitions = 8      # times to repeat drum pattern
 
##### define the data structure
score = Score("Drum Machine Pattern #1", 125.0) # tempo is 125 bpm
 
drumsPart = Part("Drums", 0, 9)  # using MIDI channel 9 (percussion)
 
bassDrumPhrase = Phrase(0.0)     # create phrase for each drum sound
snareDrumPhrase = Phrase(0.0)
hiHatPhrase = Phrase(0.0)
 
##### create musical data
 
# bass drum pattern (one bass + one rest 1/4 note) x 4 = 2 measures
bassPitches   = [BDR, REST] * 4
bassDurations = [QN,  QN] * 4
bassDrumPhrase.addNoteList(bassPitches, bassDurations)
 
# snare drum pattern (one rest + one snare 1/4 note) x 4 = 2 measures
snarePitches   = [REST, SNR] * 4
snareDurations = [QN,   QN] * 4
snareDrumPhrase.addNoteList(snarePitches, snareDurations)
 
# hi-hat pattern (15 closed 1/8 notes + 1 open 1/8 note) = 2 measures
hiHatPitches   = [CHH] * 15 + [OHH]
hiHatDurations = [EN] * 15  + [EN]  
hiHatPhrase.addNoteList(hiHatPitches, hiHatDurations)
 
##### repeat material as needed
Mod.repeat(bassDrumPhrase, repetitions)
Mod.repeat(snareDrumPhrase, repetitions)
Mod.repeat(hiHatPhrase, repetitions)
 
##### combine musical material
drumsPart.addPhrase(bassDrumPhrase)
drumsPart.addPhrase(snareDrumPhrase)
drumsPart.addPhrase(hiHatPhrase)
score.addPart(drumsPart)
 
##### view and play
View.sketch(score)
Play.midi(score)