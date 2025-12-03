# 🧩 BFS Maze Solver (Python + PyGame)
A visual maze generator and solver built using DFS (maze generation) + BFS (shortest-path search) with smooth animations and interactive UI buttons.

## 🚀 Features
- **Random Maze Generation**
- DFS Recursive Backtracking algorithm
- New maze created instantly with one click
- **BFS Maze Solving**
- Real-time exploration animation
- Clearly visualized shortest path
- **Interactive UI Buttons**
- Start BFS – begin visualization
- Regenerate Maze – create a new maze anytime
- Clear Visualization – reset BFS colors
- **Start & End Indicators**
- Green = Start
- Red = End
- **Clean, modular architecture with separate files for:**
- Maze generation
- BFS solving
- Visualization
- UI buttons

## 📁 Project Structure
```text
bfs_maze_solver/
│
├── assets/                     # optional (icons, fonts, images)
│
├── src/
│   ├── main.py                 # game loop + UI + animation
│   ├── config.py               # constants (colors, sizes, speeds)
│   ├── cell.py                 # Cell class (walls + fill + draw)
│   ├── maze_generator.py       # DFS backtracking maze generator
│   ├── bfs_solver.py           # BFS solver + path reconstruction
│   ├── ui.py                   # clickable button class + UI bar
│   └── utils.py                # optional helpers
│
├── env/                        # virtual environment
│
├── requirements.txt            # pygame
├── .gitignore
└── README.md
```

## 🛠 Tech Stack
- Python 3
- PyGame — rendering, animation, UI
- DFS — maze generation
- BFS — shortest path search

## 🔧 Installation & Setup
**1. Clone the repository**
- git clone <your-repo-url>
- cd bfs_maze_solver

**2. Create a virtual environment (Windows)**
- python -m venv env
- env\Scripts\activate

**3. Install dependencies**
- pip install pygame

## ▶ Running the Project
- Inside the project directory, with environment activated:
- python src/main.py

## 🎮 Controls & UI Buttons
**On-screen buttons**
- **Start BFS** → animate BFS from start to end
- **Regenerate** → generate a brand-new random maze
- **Clear Vis** → clear BFS colors without rebuilding maze

**Node indicators**
- 🟩 Green = Start cell
- 🟥 Red = End cell

## ✨ How It Works
**Maze Generation (DFS)**
- Starts at a random cell
- Carves passages by removing walls
- Backtracks when no unvisited neighbors
- Produces a perfect maze (one unique path between cells)

  **BFS Solver**
- Expands outward layer by layer
- Tracks visited order for animation
- Reconstructs shortest path to the goal
- Path is drawn after BFS finishes

**Visualization**
- Light blue → visited BFS cells
- Yellow → shortest path
- Maze walls always drawn on top

## 📝 License
- Free to use, modify, and learn from.
- Credit appreciated.
