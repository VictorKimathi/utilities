import math

# Given values
m = 3 * 10**-2  # mass in kg
L = 0.15  # length in m
theta_deg = 5  # angle in degrees
g = 9.81  # acceleration due to gravity in m/s^2
k = 8.99 * 10**9  # Coulomb's constant in Nm^2/C^2

# Convert angle to radians
theta_rad = math.radians(theta_deg)

# Calculate sin(theta) and tan(theta)
sin_theta = math.sin(theta_rad)
tan_theta = math.tan(theta_rad)

# Calculate the charge q
q_squared = (4 * (L**2) * (sin_theta**2) * m * g * tan_theta) / k
q = math.sqrt(q_squared)

q
