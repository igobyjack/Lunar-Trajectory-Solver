# Lunar Trajectory Solver

This project uses the General Mission Analysis Tool (GMAT) to determine the optimal launch time for a lunar transfer. The script scans through various delta-V values, coast times, and start epochs to find the best solution that minimizes the distance to the moon.

I built this to become more familiar with GMAT, a tool to simulate spacecraft trajectories/orbits, and its Python API. 

3-Body simulation.

## Example Solution
![alt](https://github.com/igobyjack/Lunar-Trajectory-Solver/blob/main/solved_trajectory.png)

## Usage

1. Ensure GMAT is installed and accessible from your environment.
2. Ensure the project is in the GMAT API folder.
3. Run the `Solver.py` script to start the optimization process.
4. The script will output the best launch time, coast time, delta-V, and the final distance to the moon.
5. The solution will be saved to a new GMAT script file named `ToLuna_solution.script` which can be viewed using GMAT. 

