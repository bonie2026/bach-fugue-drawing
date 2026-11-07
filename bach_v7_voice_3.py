import pretty_midi
from math import sin, cos, radians
from pathlib import Path
from py5canvas import *

midi_path = Path(__file__).resolve().parent / "kunst_der_fuge_08_(c)simonetto.mid"
midi = pretty_midi.PrettyMIDI(str(midi_path))
notes = midi.instruments[2].notes

# All voices use the duration of the whole piece.
total_time = midi.get_end_time()

def setup():
    create_canvas(900,900)

def draw():
    background(250)
    stroke(35, 130, 90)
    stroke_weight(0.5)

    for note in notes:

        # Start at twelve o'clock; time moves clockwise.
        angle = note.start / total_time * 360 - 90
        angle2 = note.end / total_time * 360 - 90

        amplitude = 45 + (note.pitch - 60) * 2

        radius1 = 300 + amplitude * sin(radians(angle * 6))
        radius2 = 300 + amplitude * cos(radians(angle * 10))

        x1 = 450 + radius1 * cos(radians(angle))
        y1 = 450 + radius1 * sin(radians(angle))

        x2 = 450 + radius2 * cos(radians(angle2))
        y2 = 450 + radius2 * sin(radians(angle2))

        line(x1, y1, x2, y2)

run()
