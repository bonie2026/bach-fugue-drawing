
# Art of Fugue

**A Generative Drawing Based on J. S. Bach's Contrapunctus VIII**

Art of Fugue is a computational art project that translates a three-voice fugue by Johann Sebastian Bach into a multi-layered generative drawing.

Using Python, MIDI data and py5canvas, the project explores how musical structures can be interpreted visually through pitch, timing and mathematical rules.

Each of the three musical voices generates an independent drawing. When combined, the layers reveal the relationships between the voices, reflecting the polyphonic structure of the original composition.

## Final Artwork

The final composition consists of three visual layers, represented in blue, orange and green.

Each layer follows the same circular timeline, beginning at twelve o'clock and progressing clockwise through the composition.

The three drawings can be viewed individually or combined into a single image.

The physical installation is designed to present the drawings on separate sheets of translucent paper, suspended one behind another.

<p align="center">
  <img src="journal/assets/Framed Abstract Floral Burst.png" width="600" alt="Art of Fugue – Three-Voice Combined Drawing">
</p>

## Tools and Technologies

- Python
- py5canvas — Generative drawing
- pretty_midi — MIDI data processing
- MIDI — Musical note data
- GitHub — Code and process documentation

## How It Works

### 1. MIDI Data

The project uses an existing MIDI transcription of Bach's *Contrapunctus VIII* from *The Art of Fugue* (BWV 1080).

The MIDI file is processed using `pretty_midi` to extract musical information, including:

- Pitch
- Note start time
- Note end time

### 2. Circular Timeline

The duration of the composition is mapped onto a 360-degree circle.

Each note's start and end times determine its angular position, allowing all three voices to share the same temporal structure.

### 3. Generative Drawing

Pitch values influence the radial displacement of line endpoints through mathematical functions.

Each note is represented by a line connecting two calculated points.

Different parameters and colours distinguish the three voices while maintaining a shared visual structure.

### 4. Layering

The three drawings are combined to explore how independent musical lines interact within a polyphonic composition.

## Project Files

| File | Description |
|---|---|
| [bach_v7_voice_1.py](bach_v7_voice_1.py) | Generative drawing for Voice 1 |
| [bach_v7_voice_2.py](bach_v7_voice_2.py) | Generative drawing for Voice 2 |
| [bach_v7_voice_3.py](bach_v7_voice_3.py) | Generative drawing for Voice 3 |
| [bach_v7_combined.py](bach_v7_combined.py) | Combined three-voice drawing |
| [project_statement.md](project_statement.md) | Artistic concept and technical explanation |
| [background-research.md](background-research.md) | Musical background and research |
| [journal/](journal/) | Development process and visual experiments |

## How to Run

### Requirements

- Python 3
- py5canvas
- pretty_midi
- numpy

Install the required Python packages:

```bash
pip install py5canvas pretty_midi numpy
```

### Running the Project

1. Download or clone this repository.
2. Make sure the MIDI file is in the same directory as the Python scripts.
3. Open a terminal in the project directory.
4. Run the combined drawing:

```bash
python bach_v7_combined.py
```

Alternatively, run each voice separately:

```bash
python bach_v7_voice_1.py
python bach_v7_voice_2.py
python bach_v7_voice_3.py
```

The scripts use py5canvas to generate the visual compositions.

## Documentation

Further documentation is available in the following sections:

- [Project Statement](project_statement.md) — Artistic intentions, visual methodology and physical presentation.
- [Background Research](background-research.md) — Research into Bach's fugue, polyphony and musical structure.
- [Development Journal](journal/) — Experiments, iterations and the development of the final artwork.

## AI Acknowledgement

The artistic concept and visual direction were developed by the author.

ChatGPT (GPT-6) was used to assist with MIDI parsing, Python programming and technical problem-solving.

A more detailed acknowledgement is included in the [Project Statement](project_statement.md).

## Credits and References

**Music:** Johann Sebastian Bach, *Contrapunctus VIII*, from *The Art of Fugue*, BWV 1080.

**MIDI:** Simonetto, A. G. (n.d.) *Contrapunctus VIII a 3*, from J. S. Bach’s *The Art of Fugue*, BWV 1080 [MIDI transcription]. Kunst der Fuge. Available at: https://www.kunstderfuge.com/bach/canons.htm (Accessed: 8 November 2026).

**Research:** Collins, D. (2018). "Horizontal-Shifting Counterpoint and Parallel-Section Constructions in Contrapunctus 8 and 11 from J. S. Bach's Art of Fugue." *Music Theory Online*, 24(4).

[Read the research article](https://mtosmt.org/ojs/index.php/mto/article/view/103)
