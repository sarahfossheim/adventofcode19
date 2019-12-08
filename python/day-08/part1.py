# Get the input
from input import puzzle_input

# Set the width and height
width = 25
height = 6

# Split the input up in layers
layers = []
layer = ""
for i in range(0,len(puzzle_input) + 1):
    if i % (width * height) == 0:
        if layer:
            layers.append(layer)
        layer = ""
    
    if i < len(puzzle_input):
        layer += puzzle_input[i]
    

# Find the layer with the fewest 0 digits
counts = []
for layer in layers:
    counts.append({"name": layer, "count": layer.count("0")})

minimum = min(counts, key=lambda c: c["count"])["name"]

# Get the amount of 1 digits in the layer
number_1 = minimum.count("1")

# Get the amount of 2 digits in the layer
number_2 = minimum.count("2")

# Multiply number 1 with number 2
print(number_1 * number_2)