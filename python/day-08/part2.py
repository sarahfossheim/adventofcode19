# Get the input
from input import puzzle_input

#puzzle_input = "1234222233331212"
#puzzle_input = "00001111012012015555555555555555"
#puzzle_input = "0222112222120000"

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
colors = []
while index < len(layers[0]):
    for layer in layers:
        if layer[index] != "2":
            # colors.append(layer[index])
            if layer[index] == "0":
                colors.append(" ")
            else:
                colors.append("1")
            break
        
    index += 1

row = ""
row_index = 0
for color in colors:
    row += color

    row_index += 1

    if row_index % width == 0:
        row += "\n"

print(row)