# Get the input
from input import puzzle_input

#puzzle_input = "1234222233331212"
#puzzle_input = "00001111012012015555555555555555"

# Set the width and height
width = 25
height = 6

# Split the input up in layers
layer_amount = len(puzzle_input) / (width * height)
layers = []
layer = ""
for i in range(0,len(puzzle_input)):
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