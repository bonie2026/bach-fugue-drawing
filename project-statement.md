# Project Statement

## From fugue to drawing

In simple terms, this project turns music into a generative drawing. I chose J. S. Bach’s *Contrapunctus VIII* from *The Art of Fugue* (BWV 1080), a triple fugue in three voices. What drew me to the piece was the way each voice has a melodic line I can follow on its own, while the three voices come together in unexpected but coherent ways. Bach introduces three distinct subjects, passes them between voices and eventually brings them together. I wanted to see whether a drawing could do something similar. Each voice would have its own image, and layering the three images would reveal relationships that are only visible when they are seen together.

## From note data to line

I started with the score and used a MIDI version to work with the notes as data. In Python, I used `pretty_midi` to read each voice separately and extract the pitch, start time and end time of each note. I then used `py5canvas` to draw all three voices against the same circular timeline. The piece begins at twelve o’clock, and time moves clockwise through one full turn.

The key rule in my drawing is how pitch shapes the radial pattern. In the Voice 1 script, each note’s pitch controls how far the endpoints of its line can move away from the base circle. I calculate the amplitude using this rule:

```python
amplitude = 45 + (note.pitch - 60) * 2
```
Middle C (MIDI note 60) gives an amplitude of 45. Each semitone above middle C adds 2, and each semitone below it subtracts 2. I use this amplitude to scale a sine wave and a cosine wave with different frequencies. The two waves determine how far each endpoint sits inside or outside the 300-pixel base radius.

The program repeats this calculation for each MIDI note and joins the two endpoints with a straight line. On the shared clockwise timeline, the note’s start and end times set the angles of the two endpoints. The time between them determines their angular separation, while the visible length of the line depends on both the angles and the two radii.

Blue, orange and green distinguish the three voices. On each layer, gaps in the sequence of line starts show where that voice has fewer or no new note attacks. A note that is already sounding can still extend through that part of the timeline. Because the three drawings use the same time scale, a sparse passage in one voice can line up with activity in another when the layers are brought together. The open centre comes mainly from my decision to place the lines around a ring.

## Physical presentation

I initially wanted to use screen printing because overlapping translucent inks can produce a new colour where they meet. I saw a parallel with the fugue, where independent melodic lines change how we hear each of them when they sound together. I was unable to get access to the university’s screen-printing workshop, so I chose to print the three drawings separately on translucent tracing paper.

I plan to suspend the three sheets one behind another, leaving space between them. From the front, the drawings align into a single image of the piece. As viewers move to the side, the overlap shifts and the individual layers become easier to distinguish. I want viewers to experience what drew me to the fugue in the first place: three voices that retain their own character and form a coherent whole together.

## AI acknowledgement

I developed the visual concept and created the generative drawings myself. I received substantial assistance from ChatGPT (GPT-6) with importing and parsing the MIDI file and using the extracted note data as variables in the drawing code.

## Reference

- Denis Collins, “[Horizontal-Shifting Counterpoint and Parallel-Section Constructions in Contrapunctus 8 and 11 from J. S. Bach’s Art of Fugue](https://mtosmt.org/ojs/index.php/mto/article/view/103),” *Music Theory Online*, 24(4).
