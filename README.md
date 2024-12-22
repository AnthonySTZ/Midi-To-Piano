# Midi To Piano

This script can be used to convert midi files directly into piano notes in Houdini.

## Prerequisites

For the script to work properly, you have to: 
- select a node
- have a point attribute named "note" for each note between 0-87

## Interface

This interface is pretty simple, you can press the "Browse" button to open a midi file.
Then you can choose the starting frame for the song to play.
Once you're done, you can press the "Accept" button.

![Interface](/readme/interface.jpg)

## Visualization

Once pressing "Accept", it will created a chopnet where the note animation will be played, and a point wrangle that it used to transfer this animation to the point using a "active" attribute. You can connect it to your point !

![Graph](/readme/graph.jpg)

Then you can just use a color node to see the active attribute.

![Color](/readme/color.jpg)


## Watch piano plays

![Piano](/readme/piano.jpg)