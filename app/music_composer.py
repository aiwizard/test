'''
https://github.com/kroger/pyknon
https://www.youtube.com/watch?v=R37TW97drWA
https://github.com/kairess/python_music

https://onlinesequencer.net/
'''

from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note, Rest

import random

''' 
# Create Demo mid
note1 = NoteSeq('D4 F#8 A Bb4')
midi = Midi(number_tracks=1, tempo=90)
midi.seq_notes(note1, track=0)
midi.write('./1demo.mid')
'''

# Generate Random Notes Function
durations = [
    1/2, # half note
    1/4, # quarter note
    1/8, # eighth note
    1/16 # sixteenth note
]

'''
0  1  2  3  4  5  6  7  8  9  10  11
C  C# D  D# E  F  F# G  G# A  A#  B
'''
# A_major = ['A','B','C#','D','E','F#','G#']
A_major = [9, 11, 1, 2, 4, 6, 8]
# G_major = ['G','A','B','C','D','E','F#']
G_major = [7, 9, 11, 0, 2, 4, 6]
# D_major = ['D','E','F#','G','A','B','C#']
D_major = [2, 4, 6, 7, 9, 11, 1]

def get_random_notes(n, pitches, durations, rests=True):
    if rests:
        pitches.append('r')
        
    result = NoteSeq()

    for i in range(n):
        pitch = random.choice(pitches)
        duration = random.choice(durations)
        
        if pitch == 'r':
            result.append(Rest(dur=duration))
        else:
            result.append(Note(pitch, octave=4, dur=duration))

    return result


# Generate Random Sound
notes1 = get_random_notes(20, pitches=A_major, durations=[1/8, 1/16])
midi = Midi(number_tracks=1, tempo=120)
midi.seq_notes(notes1, track=0)
midi.write('./2A_major.mid')

print(notes1)

# Percussion
hihat = NoteSeq('F#16,, R16') * 16
kick_snare = NoteSeq('C16,, R16 R16 C16 D16 C16 R16 R16') * 4
        
midi = Midi(number_tracks=1, tempo=120)
midi.seq_notes(hihat, track=0)
midi.seq_notes(kick_snare, track=0)
midi.write('./3drum.mid')

# Make it Together
midi = Midi(number_tracks=2, tempo=120)
midi.seq_notes(hihat, track=0)
midi.seq_notes(kick_snare, track=0)
midi.seq_notes(notes1, track=1)
midi.write('./4Amajor_drum.mid')

# Add Piano
piano = NoteSeq('A4, R4') * 4

midi = Midi(number_tracks=3, tempo=120)
midi.seq_notes(hihat, track=0)
midi.seq_notes(kick_snare, track=0)
midi.seq_notes(notes1, track=1)
midi.seq_notes(piano, track=2)
midi.write('./5Amajor_drum_piano.mid')
