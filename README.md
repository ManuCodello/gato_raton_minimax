# Cat & Mouse Maze – Minimax Duel  
A strategic maze game in Python where the predator hunts and the prey escapes.  

## 🎮 Project Overview  
This is a Python-based strategic game titled *“Cat & Mouse Maze – Minimax Duel”*.  
You control one of the characters (Mouse or Cat), and face off against a computer-controlled opponent driven by the **Minimax algorithm**.  
The game emphasizes:  
- Procedural maze generation with obstacles.  
- Balanced starting positions and a clear goal (Mouse to reach cheese, Cat to catch).  
- A turn-based duel of wits, combining game logic + AI.  

## 🎯 Core Objectives  
- Generate a 10×10 grid maze populated with obstacles, the cheese, the Mouse, and the Cat.  
- Ensure fair start distances so gameplay is balanced.  
- Implement three gameplay modes:  
  - Player vs Machine  
  - Player vs Player  
  - Machine vs Machine  
- Use the **Minimax** algorithm (with adjustable depth) to drive one of the characters’ strategy.  
- Use emojis for board visualization (fun, clear) and keep the interface console-based for simplicity.  

## 🧰 Technologies & Tools  
- **Python 3.x** — primary language.  
- Standard Python libraries (no external dependencies required).  
- Minimax algorithm implementing heuristic evaluations of positions.  
- Data structures representing the board, distances (Manhattan), turn logic and win conditions.  

## 📁 Project Structure  
/
├── juego-del-gatoyraton.py # Main game script
├── README.md # This file

bash
Copiar código
*(Rename filenames if they differ slightly.)*

## 🕹 How to Play  
1. Clone the repository:  
   ```bash
   git clone https://github.com/ManuCodello/gato_raton_minimax.git
Enter the project folder:

bash
Copiar código
cd gato_raton_minimax
Ensure you have Python 3 installed:

bash
Copiar código
python --version
Run the game script:

bash
Copiar código
python juego-del-gatoyraton.py
After the prompt: choose the mode (1, 2 or 3) and if relevant, choose your character (Cat or Mouse). Then play: avoid obstacles, make your moves, the AI does its moves via Minimax.

🧠 What You’ll Learn from This Project
How to generate a maze with embedded goal, obstacles and balanced start positions.

How to implement Minimax algorithm to make one character react intelligently (simulate future states & pick best move).

How to model game states (board, players, turns) and terminate game based on win/lose or turn-limit.

How to structure Python code for game logic, keeping it modular and clean — great for your portfolio.

🚧 Possible Future Enhancements
Add a graphical UI (with e.g., Pygame) to make the visuals more engaging.

Implement difficulty levels (e.g., deeper Minimax for harder Cat, or special moves for Mouse).

Add multiple levels/mazes with increasing complexity (larger grid, more obstacles).

Write unit tests covering maze generation, Minimax logic, move validity.

Improve pathfinding heuristics (e.g., combining Minimax with A* or other search algorithms).

👤 Author
Manu Codello — Computer Science Student & Aspiring Developer
GitHub: ManuCodello
Leveraging algorithmic thinking + project building to step into a remote programming role.
