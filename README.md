# Cellular-automata

## Content

## What are cellular automata
Cellular automata (singular = cellular automaton) are algorithms that evolves based on some rules. Cellular automatons are best expalined as **grid of cells**, it can be 1D, 2D, 3D grid and so on. Cells can have **any shape** you want (for exmaple hexagons, squares, triangel...).One "tick" when changes are aplied is called **generation**. New generation is computed by apliing rules to one or more older genrations. **State of a cell** can be _1_ or _0_ or you can have more states like _imune, infected, cured, carrier_. **Rule** can be something like this _if dead cell has 2 o more live neighbours, it becomes alive_. When we are looking at rules we must know what **neighborhood** is used. In 2D grids there are two main neighborhoods. **Moore neighborhood** is nine cells in total with the main cell in the midle. The secund one is called **von Neumann neighborhood**, there is six cells (main again in the middle). This neighborhood consist of one cell above the main one, one down form the main cell and one left and right. There is also extended von Neumann neighborhood it has same cells as the original, but there is added one cell in each direction.

### Conway's Game of Life
My instance of The Game of Life. Original Game of Life comes from British mathematician John Horton Conway from 1970.
