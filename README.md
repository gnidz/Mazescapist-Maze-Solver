# Mazescapist Maze Solver

---

### About This Project

This repository houses the Python code I developed to conquer the incredibly challenging **Mazescapist** Minecraft map. This map throws you into a complex labyrinth with a strict **8-day in-game time limit** to find the exit. My code is designed to help analyze the maze, identify optimal paths, and guide my decisions to escape before time runs out.

---

### The Challenge: Mazescapist Minecraft Map

I recently dove into the intense world of the "Mazescapist" Minecraft map, available at [mazescapist ver 1.16.5](https://www.minecraftmaps.com/puzzle-maps/mazescapist). It's not just any maze; its intricate design and the added pressure of a limited in-game timeframe make it a true test of strategy and spatial reasoning.

---

### How This Code Helps

This Python project aims to provide a systematic approach to solving the Mazescapist map. Here's how it's intended to assist:

* **Maze Analysis**: The code will interpret the structure of the maze, potentially from input data (e.g., a representation of the maze walls and paths).
* **Pathfinding Algorithms**: It will implement algorithms (like Breadth-First Search, Depth-First Search, or A*) to identify the most efficient routes from a starting point to the exit.
* **Strategic Guidance**: By finding optimal paths, the solver can provide insights into which turns to take, helping to minimize wasted time within the game.

Ultimately, this project is my secret weapon to navigate the "Mazescapist" and emerge victorious!

---

### Getting Started

To run or contribute to this project, follow these steps:

#### 1. Clone the Repository

First, get a copy of the code on your local machine:

```bash
git clone [https://github.com/gnidz/Mazescapist-Maze-Solver.git](https://github.com/gnidz/Mazescapist-Maze-Solver.git)
cd Mazescapist-Maze-Solver
```
#### 2. Set Up Your Virtual Environment
It's crucial to use a virtual environment to manage project dependencies and avoid conflicts with your system's Python installation.

**Create and Activate:**

* **On macOS/Linux/Git Bash:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

* **On Windows (PowerShell):**
    ```powershell
    py -m venv .venv
    .venv\Scripts\Activate.ps1
    ```

* **On Windows (Command Prompt):**
    ```dos
    py -m venv .venv
    .venv\Scripts\activate.bat
    ```

Your terminal prompt should now show `(.venv)` indicating the virtual environment is active.

#### 3. Install Dependencies
Once your virtual environment is active, install the necessary Python packages:

```bash
pip install -r requirements.txt
```

### 4. Run the Solver
Execute your main Python script (replace main.py if your entry point is named differently):

```bash
python main.py
```
(Further instructions on how to use the solver (e.g., input format, command-line arguments) would go here once the specific functionality is implemented.)

### 5. Deactivate the Virtual Environment
When you're done working on the project, you can deactivate the virtual environment:

```bash
deactivate
```

---

### Contribution
Feel free to explore the code, suggest improvements, or even contribute. Any help in making this maze solver more robust would be greatly appreciated!
