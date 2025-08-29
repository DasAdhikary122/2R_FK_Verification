from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import math
import time

# Connect to CoppeliaSim (ensure simulation is loaded and Remote API is enabled)
client = RemoteAPIClient()
sim = client.getObject('sim')

# Start simulation
sim.startSimulation()
time.sleep(0.2)  

# Get handles
joint1 = sim.getObject('/Revolute_joint')
joint2 = sim.getObject('/Revolute_joint0')
tcp = sim.getObject('/Dummy')  


link1 = 0.52
link2 = 0.53


theta1_deg = 45
theta2_deg = 30

# Convert to radians and set target positions
theta1_rad = math.radians(theta1_deg)
theta2_rad = math.radians(theta2_deg)

sim.setJointTargetPosition(joint1, theta1_rad)
sim.setJointTargetPosition(joint2, theta2_rad)

for _ in range(100):
    sim.step()
    time.sleep(0.01)

# Read actual joint angles
theta1 = sim.getJointPosition(joint1)
theta2 = sim.getJointPosition(joint2)

# Compute FK
x_fk = link1 * math.cos(theta1) + link2 * math.cos(theta1 + theta2)
y_fk = link1 * math.sin(theta1) + link2 * math.sin(theta1 + theta2)

# Get TCP position (global coordinates)
tcp_pos = sim.getObjectPosition(tcp, -1)

# Compute error
error_x = abs(tcp_pos[0] - x_fk)
error_y = abs(tcp_pos[1] - y_fk)

# Print results with high precision
print(f"\n Python FK Calculation:")
print(f"FK   x: {x_fk:.8f}, y: {y_fk:.8f}")
print(f"TCP  x: {tcp_pos[0]:.8f}, y: {tcp_pos[1]:.8f}")
print(f" Error  x: {error_x:.8f}, y: {error_y:.8f}")


time.sleep(0.1)
sim.stopSimulation()
