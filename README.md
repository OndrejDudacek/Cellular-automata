# About this app

This application is my school project on cellular automata. When I presented it in class I used this presentation I created.

# Cellular-automata
## What are cellular automata
**Cellular automata** (singular = cellular automaton) are algorithms that evolve based on some rules. 

Cellular automatons are best explained as a **grid of cells**, they can be 1D, 2D, 3D grid, and so on. 

Cells can have **any shape** you want (for example hexagons, squares, triangles...). 

One "tick" when changes are applied is called **generation**. A new generation is computed by applying rules to one or more older generations. 

**A state of a cell** can be 1 or 0 or you can have more states like immune, infected, cured, and carrier. 

**A rule** can be something like this if the dead cell has 2 o more live neighbours, it becomes alive. 

When we are looking at rules we must know what **neighborhood** is used. In 2D grids, there are two main neighborhoods. **Moore's neighborhood** has nine cells in total with the main cell in the middle. The second one is called **von Neumann's neighborhood**, there are six cells (the main is in the middle again). This neighborhood consists of one cell above the main one, one down from the main cell, and one left and right. There is also an extended von Neumann's neighborhood it has the same cells as the original, but there is added one cell in each direction.


## Game of Life:
The Game of Life is a classic example of a cellular automaton introduced by the British mathematician John Horton Conway in 1970. It is a 2D cellular automaton with simple rules but exhibits complex and unpredictable behavior.

### Rules:
Each cell in the grid can be in one of two states: alive (1) or dead (0).
- The evolution of the grid occurs in generations, where the state of each cell is determined by its neighbors in the previous generation.
- The rules are simple:
- Any live cell with fewer than two live neighbors dies (underpopulation).
- Any live cell with two or three live neighbors survives.
- Any live cell with more than three live neighbors dies (overpopulation).
- Any dead cell with exactly three live neighbors becomes alive (reproduction).
  
### Behavior:
Despite the simplicity of these rules, the Game of Life can exhibit complex and fascinating patterns, including oscillators, gliders, spaceships, and stable formations. It has attracted attention not only for its mathematical properties but also for its relevance in the study of emergent phenomena and complexity.


## Elementary Cellular Automaton:
An Elementary Cellular Automaton (CA) is a specific type of cellular automaton that operates on a one-dimensional grid of cells. Each cell has two possible states (0 or 1), and the evolution of the system is determined by a set of simple rules.

### Rules:
- The rules for an elementary CA are defined by an 8-bit binary number. Each bit of the binary number represents a possible configuration of a cell and its two neighbors (left and right).
- For example, the binary rule "11011010" means that if a cell and its neighbors are in the configuration "110," the cell becomes alive (1) in the next generation.
- There are a total of 256 possible elementary cellular automaton rules.

### Behavior:
Elementary cellular automata can display a wide range of behaviors, including periodic patterns, chaotic sequences, and self-replicating structures. The simplicity of the rules makes them an interesting subject for studying the emergence of complex behavior from basic principles.

