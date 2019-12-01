# Import numpy so we can calculate with matrices
import numpy as np

# Import the fuel per module
from part1 import fuel_per_module, total_fuel

# Define array 
fuel_for_fuel = []

# Calculate
def get_fuel_for_module(module):
    return np.floor(module / 3) - 2

# TODO: Think how to simplify this
# Loop through the fuel requirements for every module
for mod in fuel_per_module:
    new_fuel = mod
    
    # As long as the fuel is positive, keep calculating
    while new_fuel > 0:
        # Get the fuel for the fuel
        new_fuel = get_fuel_for_module(new_fuel)

        # Add the fuel needed for the fuel to an array
        if new_fuel > 0:
            fuel_for_fuel.append(new_fuel)

# Sum of the fuel requirements of all modules, and the fuel requirements for the fuel
print(np.sum(fuel_for_fuel) + total_fuel)
