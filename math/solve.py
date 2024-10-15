from sympy import symbols, Eq, solve

# Define the variable
x = symbols('x')

# Set up the equation
equation = Eq(15 * x**2, 6 * (2 - x)**2)

# Solve the equation
solutions = solve(equation, x)
solutions
