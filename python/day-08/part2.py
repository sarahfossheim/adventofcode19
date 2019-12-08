# Get the input
from input import puzzle_input

# Set the width and height
width = 25
height = 6

# Split the input up in layers
layers = []
layer = ""
for index in range(0,len(puzzle_input) + 1):
    if index % (width * height) == 0:
        if layer:
            layers.append(layer)
        layer = ""
    
    if index < len(puzzle_input):
        layer += puzzle_input[index]
    
index = 0
colors = ""
while index < len(layers[0]):
    for layer in layers:
        if layer[index] != "2":
            if layer[index] == "0":
                colors += " "
            else:
                colors += "1"
            break
    index += 1

    if index % width == 0:
        colors += "\n"


print(colors)