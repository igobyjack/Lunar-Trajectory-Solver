# Lunar Trajectory Solver

This project uses the General Mission Analysis Tool (GMAT) to determine the optimal launch time for a lunar transfer. The script scans through various delta-V values, coast times, and start epochs to find the best solution that minimizes the distance to the moon.

## Usage

1. Ensure GMAT is installed and accessible from your environment.
2. Run the `Solver.py.py` script to start the optimization process.
3. The script will output the best launch time, coast time, delta-V, and the final distance to the moon.
4. The solution will be saved to a new GMAT script file named `ToLuna_solution.script`.

