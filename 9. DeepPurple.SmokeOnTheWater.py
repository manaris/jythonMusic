# DeepPurple.SmokeOnTheWater.py
#
# Demonstrates how to combine melodic lines, chords, and
# percussion.  This is based on the intro of "Smoke On the Water" 
# by Deep Purple.
 
from music import *
 
##### define the data structure
score  = Score("Deep Purple, Smoke On The Water", 110)  # 110 bpm
 
guitarPart = Part(OVERDRIVE_GUITAR, 0)
bassPart = Part(ELECTRIC_BASS, 1)
drumPart = Part(0, 9)    # using MIDI channel 9 (percussion)
 
guitarPhrase1 = Phrase(0.0)   # guitar opening melody
guitarPhrase2 = Phrase(32.0)  # guitar opening melody an octave lower
bassPhrase = Phrase(64.0)     # bass melody
drumPhrase = Phrase(96.0)     # drum pattern
 
##### create musical data
# guitar opening melody (16QN = 4 measures)
guitarPitches   = [G2, AS2, C3,  G2, AS2, CS3, C3, G2, AS2, C3,  AS2, 
                    G2]    
guitarDurations = [QN, QN,  DQN, QN, QN,  EN,  HN, QN, QN,  DQN, QN,  
                    DHN+EN]
guitarPhrase1.addNoteList(guitarPitches, guitarDurations)
 
# create a power-chord sound by repeating the melody an octave lower
guitarPhrase2.addNoteList(guitarPitches, guitarDurations)
Mod.transpose(guitarPhrase2, -12)
 
# bass melody (32EN = 4 measures)
bassPitches1   = [G2, G2, G2, G2, G2, G2, G2, G2, G2, G2, 
                  G2, G2, G2, G2, G2, G2, G2, G2]
bassDurations1 = [EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, 
                  EN, EN, EN, EN, EN, EN, EN, EN]
bassPitches2   = [AS2, AS2, C3, C3, C3, AS2, AS2, G2, G2, 
                  G2, G2, G2, G2, G2]
bassDurations2 = [EN,  EN,  EN, EN, EN, EN,  EN,  EN, EN, 
                  EN, EN, EN, EN, EN]
bassPhrase.addNoteList(bassPitches1, bassDurations1)
bassPhrase.addNoteList(bassPitches2, bassDurations2)
 
# snare drum pattern (2QN x 8 = 4 measures)
drumPitches   = [REST, SNR] * 8
drumDurations = [QN,   QN]  * 8
drumPhrase.addNoteList(drumPitches, drumDurations)
 
##### repeat material as needed (based on how it's arranged in time)
Mod.repeat(guitarPhrase1, 8)
Mod.repeat(guitarPhrase2, 6)
Mod.repeat(bassPhrase, 4)
Mod.repeat(drumPhrase, 2)
 
##### combine musical material
guitarPart.addPhrase(guitarPhrase1)
guitarPart.addPhrase(guitarPhrase2)
bassPart.addPhrase(bassPhrase)
drumPart.addPhrase(drumPhrase)
score.addPart(guitarPart)
score.addPart(bassPart)
score.addPart(drumPart)
 
##### play and write score to a MIDI file
Play.midi(score)
Write.midi(score, "DeepPurple.SmokeOnTheWater.mid")