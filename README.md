# 2R_FK_Verification
project for verifying Forward Kinematics (FK) of a 2-link planar robot arm using Python and CoppeliaSim Remote API. Includes FK calculation, simulation control, and TCP position validation.

---

## 🚀 How to Run the Simulation (via Python API)

### 1. Prerequisites
- Install [CoppeliaSim](https://www.coppeliarobotics.com/)
- Install Python 3.8+  
- Install dependencies:
  ```bash
  pip install numpy

Copy sim.py (from CoppeliaSim/programming/remoteApiBindings/python/) into this project folder.



2. Start CoppeliaSim

Launch CoppeliaSim.
Open the provided scene (scenes/RoboticArmSimulation_FK_API.ttt).
Make sure the Remote API server is running (default port 19997).
In CoppeliaSim menu: Tools → Remote API Server.


3. Run the Python Code

From command prompt first will enter into the file where the python code is located.
- after that
     ```bash
     python 2r_fk_tcp.py

4. What Happens
The script connects to CoppeliaSim using the Remote API.
Joint angles are set in the simulator.
TCP (Tool Center Point) position is read from the simulation.
FK math (from Python) is compared with the simulated TCP position.


5. Expected Output

Console prints showing both calculated FK TCP position and simulated TCP position.
Values should be nearly identical (small difference due to simulation precision).


👨‍💻 Author

Suman Das Adhikary

📧 For any queries, feel free to reach out: sumandasadhikary457@gmail.com



