# Project Statement

## From fugue to drawing

In simple terms, this project turns music into a generative drawing. I chose J. S. Bach’s *Contrapunctus VIII* from *The Art of Fugue* (BWV 1080), a triple fugue in three voices. What drew me to the piece was the way each voice has a melodic line I can follow on its own, while the three voices come together in unexpected but coherent ways. Bach introduces three distinct subjects, passes them between voices and eventually brings them together. I wanted to see whether a drawing could do something similar. Each voice would have its own image, and layering the three images would reveal relationships that are only visible when they are seen together.

## From note data to line

I started with the score and used a MIDI version to work with the notes as data. In Python, I used `pretty_midi` to read each voice separately and extract the pitch, start time and end time of each note. I then used `py5canvas` to draw all three voices against the same circular timeline. The piece begins at twelve o’clock, and time moves clockwise through one full turn.

The three voices share the duration of the full MIDI file. In [the Voice 1 script](bach_v7_voice_1.py), I divide each note’s start and end times by that duration to place its two endpoints on the same circular timeline.

```python
total_time = midi.get_end_time()
```

```python
angle = note.start / total_time * 360 - 90
angle2 = note.end / total_time * 360 - 90
```

The −90° offset places the start of the piece at twelve o’clock. Notes that start at the same time share a starting angle across all three layers.

Pitch controls how far the endpoints can move from the base circle. In Voice 1, middle C (MIDI note 60) gives an amplitude of 45 pixels, with a change of 2 pixels per semitone. I use the note’s starting angle in both wave calculations. The sine and cosine terms move the endpoints inside or outside the 300-pixel base radius at different rates around the circle.

```python
amplitude = 45 + (note.pitch - 60) * 2
radius1 = 300 + amplitude * sin(radians(angle * 6))
radius2 = 300 + amplitude * cos(radians(angle * 10))
```

I convert each endpoint’s angle and radius into coordinates and join the two points with a straight line. The note’s duration determines the angular separation between the endpoints, while the visible line length depends on both the angles and the radii.

Blue, orange and green distinguish the three voices. On each layer, gaps in the sequence of line starts show where that voice has fewer or no new note attacks. A note that is already sounding can still extend through that part of the timeline. Because the three drawings use the same time scale, a sparse passage in one voice can line up with activity in another when the layers are brought together. The open centre comes mainly from my decision to place the lines around a ring.

## Physical presentation

I initially wanted to use screen printing because overlapping translucent inks can produce a new colour where they meet. I saw a parallel with the fugue, where independent melodic lines change how we hear each of them when they sound together. I was unable to get access to the university’s screen-printing workshop, so I chose to print the three drawings separately on translucent tracing paper.

I plan to suspend the three sheets one behind another, leaving space between them. From the front, the drawings align into a single image of the piece. As viewers move to the side, the overlap shifts and the individual layers become easier to distinguish. I want viewers to experience what drew me to the fugue in the first place: three voices that retain their own character and form a coherent whole together.

## AI acknowledgement

I developed the visual concept and created the generative drawings myself. I received substantial assistance from ChatGPT (GPT-6) with importing and parsing the MIDI file and using the extracted note data as variables in the drawing code.

## Reference

- Denis Collins, “[Horizontal-Shifting Counterpoint and Parallel-Section Constructions in Contrapunctus 8 and 11 from J. S. Bach’s Art of Fugue](https://mtosmt.org/ojs/index.php/mto/article/view/103),” *Music Theory Online*, 24(4).
- Sun, R. (2022) *The Art of Fugue, BWV 1080: Contrapunctus VIII [with analysis]* [YouTube video]. 22 May. Available at: https://www.youtube.com/watch?v=INKRUAEVRi0 (Accessed: 8 November 2026).
