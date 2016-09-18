# furElise.py
# Generates the theme from Beethoven's Fur Elise.
 
from music import *
 
# theme has some repetition, so break it up to maximize economy
# (also notice how we line up corresponding pitches and durations)
pitches1   = [E5, DS5, E5, DS5, E5, B4, D5, C5]
durations1 = [SN, SN,  SN, SN,  SN, SN, SN, SN]
pitches2   = [A4, REST, C4, E4, A4, B4, REST, E4]
durations2 = [EN, SN,   SN, SN, SN, EN, SN,   SN]
pitches3   = [GS4, B4, C5, REST, E4]
durations3 = [SN,  SN, EN, SN,   SN]
pitches4   = [C5, B4, A4]
durations4 = [SN, SN, EN]
 
# create an empty phrase, and construct theme from the above motifs
theme = Phrase()   
theme.addNoteList(pitches1, durations1)
theme.addNoteList(pitches2, durations2)
theme.addNoteList(pitches3, durations3)
theme.addNoteList(pitches1, durations1)  # again
theme.addNoteList(pitches2, durations2)
theme.addNoteList(pitches4, durations4)
 
# play it
Play.midi(theme)