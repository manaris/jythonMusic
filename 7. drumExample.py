# drumExample.py
# A quick demonstration of playing a drum sound.
 
from music import *
 
# for drums always use a part on channel 9 
# when using channel 9, the instrument (2nd argument) is ignored
drumPart = Part("Drums", 0, 9)
 
# try one of these as pitch: ACOUSTIC_BASS_DRUM, BASS_DRUM_1, SIDE_STICK, 
# ACOUSTIC_SNARE, HAND_CLAP, ELECTRIC_SNARE, LOW_FLOOR_TOM, CLOSED_HI_HAT,
# HIGH_FLOOR_TOM, PEDAL_HI_HAT, LOW_TOM, OPEN_HI_HAT, LOW_MID_TOM, 
# HI_MID_TOM, CRASH_CYMBAL_1 (for more, see Appendix A)
 
note = Note( PEDAL_HI_HAT, QN )
 
drumPhrase = Phrase()
drumPhrase.addNote(note)
 
drumPart.addPhrase(drumPhrase)
 
Play.midi( drumPart )