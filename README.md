# Mazescapist Maze Solver

---

### About This Project

This repository houses the Python code I developed to conquer the ***Mazescapist*** Minecraft map, a CTM (Complete The Monument) adventure inspired by the movie The Maze Runner. The goal is not merely to escape, but to find all 16 wools scattered throughout a vast, mysterious maze whose layout changes daily.

This code is my strategic tool to tackle this challenge. It's designed to analyze the maze's structure, track its daily changes, and identify the ***repeating 8-day cycle of its layout***. By understanding this pattern, the program can help pinpoint optimal paths, manage the strict 8-day in-game time limit, and guide my decisions to successfully complete the monument before time runs out.

---

### The Challenge: Mazescapist Minecraft Map

Available at [mazescapist ver 1.16.5](https://www.minecraftmaps.com/puzzle-maps/mazescapist), Mazescapist is an open-world adventure that tests strategy, memory, and combat skills. The primary challenge stems from its core mechanic: the maze's layout shifts every day, creating a dynamic and unpredictable environment.

Players must explore this ever-changing labyrinth to solve its mysteries, find the 16 hidden wools, and survive encounters with dangerous enemies. Along the way, helpful NPCs and powerful gear can be discovered to aid in the journey. The map is intentionally designed to be difficult, demanding efficient exploration and a sharp memory to master the maze's 8-day cycle.

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
