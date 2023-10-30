# Cellular-automata

## Content
### What are cellular automata
#### Game of Life

## What are cellular automata
**Cellular automata** (singular = cellular automaton) are algorithms that evolve based on some rules. 

Cellular automatons are best explained as a **grid of cells**, they can be 1D, 2D, 3D grid, and so on. 

Cells can have **any shape** you want (for example hexagons, squares, triangles...). 

One "tick" when changes are applied is called **generation**. A new generation is computed by applying rules to one or more older generations. 

**A state of a cell** can be 1 or 0 or you can have more states like immune, infected, cured, and carrier. 

**A rule** can be something like this if the dead cell has 2 o more live neighbours, it becomes alive. 

When we are looking at rules we must know what **neighborhood** is used. In 2D grids, there are two main neighborhoods. **Moore's neighborhood** has nine cells in total with the main cell in the middle. The second one is called **von Neumann's neighborhood**, there are six cells (the main is in the middle again). This neighborhood consists of one cell above the main one, one down from the main cell, and one left and right. There is also an extended von Neumann's neighborhood it has the same cells as the original, but there is added one cell in each direction.
### Game of Life
My instance of The Game of Life. Original Game of Life comes from British mathematician John Horton Conway from 1970.
