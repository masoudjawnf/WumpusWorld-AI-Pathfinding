# Wumpus World AI Agent

A Python implementation of the **Wumpus World** environment, where an AI agent navigates a grid-based world to find gold while avoiding pits and the Wumpus. This project focuses on **pathfinding, logic-based decision making, and constraint satisfaction**.

## Features

- Fully functional AI agent that navigates safely using a logic-based approach.  
- Avoids hazards like pits and Wumpus based on surrounding indicators (breeze and stench).  
- Keeps track of visited cells and updates safe locations dynamically.  
- Interactive grid display showing agent movements and world status.  
- **AI Logic Highlights:**  
  - The agent checks each cell it moves into, and if there is **no breeze or stench**, it marks all adjacent cells as safe.  
  - The agent updates its **knowledge of the surrounding environment** based on observations to make better pathfinding decisions.  

## How It Works

- The world is represented as a grid with pits (`P`), Wumpus (`W`), and gold (`G`).  
- The agent (`A`) starts at a safe cell `(0,0)` and chooses moves based on safe paths and a counter to minimize revisiting the same cell.  
- Adjacent cells to hazards have indicators:  
  - `B` for breeze (near pits)  
  - `S` for stench (near Wumpus)  
- The agent moves until it finds the gold or encounters a hazard.  

## Getting Started

### Prerequisites

- Python 3.x

### Running the Project

1. Clone the repository:  
   ```bash
   git clone <repository-url>
2.Navigate to the project folder:
```bash
cd wumpus-world
```
3.Run the Python script:
```bash
python wumpus_world.py
```
Customization
Grid size can be changed by modifying the size variable.
Pit, Wumpus, and gold positions can be set with:
```bash
world.place_pits(num_pits, x, y)
world.place_wumpus(x, y)
world.place_gold(x, y)
```
Example Output
The script prints the following during execution:
Current agent position
Safe pits and Wumpus lists
Grid display
Messages when the agent falls into a pit, encounters the Wumpus, or finds the gold

License
This project is open-source and free to use.
