# Background Research — Hearing and Seeing a Triple Fugue

**Research question** · How can generative drawing make the independence and interaction of the three voices in Bach’s *Contrapunctus VIII* visible?

## 1. What does polyphony sound like?

Imagine two groups singing *Frère Jacques*. The second group begins while the first is still singing. You can follow either group, but at any given moment the notes from both groups create a combined sound. This is a simple way to hear **polyphony**. A **voice** is a melodic line you can follow, even when one person plays several lines on a keyboard.

| Texture | What to listen for |
| --- | --- |
| Melody with accompaniment | One tune leads while chords or a repeated pattern support it. Imagine a singer with a strumming guitarist. |
| Polyphony | Two or more melodic lines unfold together. Your attention can move from one to another as they answer, cross or overlap. |

**Counterpoint** is the craft of composing those lines together. Listen *horizontally* and you hear how one line moves through time. Listen *vertically* and you hear which notes meet at a given moment. The lines can create tension as well as consonance. A note that sounds unsettled against another can make its resolution feel more deliberate. [University of Iowa, *Fugue*](https://pressbooks.uiowa.edu/twentieth-and-twenty-first-century-music/chapter/fugue/)

[![Watch the counterpoint example from my research notes](https://i.ytimg.com/vi/BGaRq5vi-gA/hqdefault.jpg)](https://www.youtube.com/watch?v=BGaRq5vi-gA&t=4s)

[Watch the counterpoint example from my research notes ↗](https://www.youtube.com/watch?v=BGaRq5vi-gA&t=4s)

## 2. What makes a fugue triple?

A **subject** is a recognisable musical idea, like a short phrase you could hum. In a **fugue**, one voice introduces the subject and another takes it up. The first voice can keep moving while the second presents the idea. Later, the subject can return in a different register, alongside other material, or after a passage that uses only a fragment of it.

A **triple fugue** develops **three distinct subjects**. Think of three actors and three lines of dialogue. An actor can speak different lines over the course of the scene, and the same line can be spoken by different actors. In *Contrapunctus VIII*, Bach uses three voices and introduces the three subjects in succession. The equal numbers are two separate features of this piece. *Contrapunctus XI* provides a useful comparison because it works with related versions of the same three subjects in **four** voices. [Denis Collins, *Music Theory Online*](https://mtosmt.org/issues/mto.18.24.4/mto.18.24.4.collins.html)

### Three subjects in the score

| Subject | Score excerpt | What to listen for |
| --- | --- | --- |
| 1 | ![Score excerpt for subject 1](https://www.teoria.com/res/images/articles/kdf/VIII/S1.gif) | The opening phrase. Try humming its contour before the other voices enter. |
| 2 | ![Score excerpt for subject 2](https://www.teoria.com/res/images/articles/kdf/VIII/S2.gif) | The repeated notes around bar 39. Listen for the first subject continuing above this new material. |
| 3 | ![Score excerpt for subject 3](https://www.teoria.com/res/images/articles/kdf/VIII/S3.gif) | A variation of the main theme of *The Art of Fugue*, entering around bar 94. |

*Score excerpts from [José Rodríguez Alvira’s Teoria analysis](https://www.teoria.com/en/articles/kdf/VIII/). Bar numbers follow [Collins’s analysis](https://mtosmt.org/issues/mto.18.24.4/mto.18.24.4.collins.html).*

## 3. Why I chose Contrapunctus VIII

I started by listening to the C-major Prelude, BWV 846, from *The Well-Tempered Clavier*. The steady broken-chord pattern made me think about how repeating one rule can produce variation. The prelude and its companion fugue are separate pieces. My early notes also explored equal temperament, a tuning system that divides the octave into twelve equal semitone steps. For the drawing, the idea I carried forward was the interaction between melodic lines. I work with MIDI note numbers and timings.

[![Listen to Bach’s C-major Prelude, BWV 846](https://i.ytimg.com/vi/ToWj_4xvVZA/hqdefault.jpg)](https://www.youtube.com/watch?v=ToWj_4xvVZA)

[Listen to Bach’s C-major Prelude, BWV 846 ↗](https://www.youtube.com/watch?v=ToWj_4xvVZA)

I chose *Contrapunctus VIII* because I wanted a piece that would give me **three independent drawings with a reason to be seen together**. The three-voice texture gives me a clear correspondence between the score and the three sheets. The piece also lets the listener hear relationships develop. A subject becomes familiar on its own, meets another subject, and later returns in a different combination. That progression made it possible to think about what a viewer discovers when moving from one sheet to the combined image.

| Where to listen | What happens |
| --- | --- |
| Opening | Learn the shape of the first subject. Listen for it to move between voices. |
| Bars 39–47 | The second subject enters in the middle voice against the first subject above it. In the next statement, the second subject is at the top and the first is at the bottom. |
| Around bar 94 | A third subject joins the piece, drawing on the main theme of the larger collection. |
| Final section | Listen for the three familiar ideas sounding together and changing places across the voices. |

*The bar references follow [Collins’s analysis, particularly Examples 2a–b and Table 5](https://mtosmt.org/issues/mto.18.24.4/mto.18.24.4.collins.html).*

[![Open the Bach video from my research notes](https://i.ytimg.com/vi/INKRUAEVRi0/hqdefault.jpg)](https://www.youtube.com/watch?v=INKRUAEVRi0)

[Open the Bach video from my research notes ↗](https://www.youtube.com/watch?v=INKRUAEVRi0)

[Listen to *The Art of Fugue* at the Netherlands Bach Society](https://www.bachvereniging.nl/en/bwv/bwv-1080)

## 4. Turning the score into a drawing

My early reading on musical networks gave me a way to think about relationships between events. A network can represent selected musical units as points and draw connections according to an explicit rule. My own rule is geometric. I use each note’s start time, end time and pitch to draw a line, with all three voices measured against the same circular clock. [Analysis and Visualization of Musical Structure using Networks](https://arxiv.org/abs/2404.15208) · [Higher-Order Network Representation of J. S. Bach’s Solo Violin Sonatas and Partitas](https://arxiv.org/abs/2506.08540)

| Musical feature | Drawing decision |
| --- | --- |
| One voice | One colour and one sheet of tracing paper |
| A note’s start and end | Two angular positions on a shared clockwise timeline |
| Pitch | A change in the amplitude of the radial pattern |
| Voices active at the same time | Marks occupy the same angular region across layers, even if their radii differ |
| A subject changes voices | Its notes follow the receiving voice’s colour. Colours identify voices throughout the piece. |

The drawing works at the level of individual MIDI notes. I use the score excerpts above to identify the subjects. The program can reveal alignments in timing and differences in density, while the score and recordings help explain what those patterns mean musically. The MIDI source is [Kunst der Fuge](https://www.kunstderfuge.com/bach/canons.htm), and the static 2D drawing is made with [py5canvas](https://github.com/colormotor/py5canvas). [Read the project statement for the code and mapping](project-statement.md).

## 5. Visual references and the physical layers

### Julien Gachadoat · *Mineral #11* (2023)

![Mineral #11 by Julien Gachadoat, a black-and-white composition made from fields of fine lines](https://assets.rcs-cdn.com/img/5aa957fa-8cbd-474b-863b-9e332091b8fb/5307cc685295049d?w=1280&f=auto&sig=e6cbf74aa86ca590ae384d31c01b757e)

I was drawn to the way thin lines gather into denser areas and then open up again. The changes in direction and density make separate regions visible inside the same composition. This helped me think about how the three voices could share an overall shape while each retaining its own rhythm of marks. [Image and interview, *The Power of the Plotter*, Right Click Save](https://www.rightclicksave.com/article/the-power-of-the-plotter-generative-art-aleksandra-jovanic-julien-gachadoat-feral-file-graph-interview)

### Eduardo Mac Entyre · Generative painting

![Eduardo Mac Entyre’s red-ground painting with overlapping coloured loops](https://www.retroavangarda.com/wp-content/uploads/2020/11/08-Mac-Entyre.jpg)

The coloured loops in this painting remain visible individually even where they gather into a brighter, more complex centre. I initially explored screen printing and Risograph printing because overlapping inks can change how colours are perceived. For the installation, I use three separate tracing-paper sheets. From the front, the layers register into one image. Moving sideways shifts their apparent alignment, giving the viewer a chance to follow one voice and then see how it fits back into the whole. [Image and historical context, Anna Kłos, *Generative Art in Argentina*, Retroavangarda](https://www.retroavangarda.com/generative-art-in-argentina/)
