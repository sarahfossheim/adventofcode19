# Set the coordinates
distances = []

# Get all the directions from the input
from input import moving_input_1, moving_input_2

def populate_grid(moving_input):
    coordinates_all = []

    # Set the current position
    x = 0
    y = 0

    # Loop through all the directions
    for move in moving_input:
        direction = move[0]
        distance = int(move[1:])

        move_x = move_y = 0

        if direction == "L":
            move_x = -1
        if direction == "R":
            move_x = 1
        if direction == "D":
            move_y = -1
        if direction == "U":
            move_y = 1

        for _ in range(0, distance):
            x += move_x
            y += move_y

            new_coordinate = (x, y)

            coordinates_all.append(new_coordinate)

    return coordinates_all

line_1 = populate_grid(moving_input_1)
line_2 = populate_grid(moving_input_2)

intersections = list(set(line_1) & set(line_2))

for intersection in intersections:
    dist = abs(intersection[0]) + abs(intersection[1])
    distances.append(dist)
    

print("SOLUTION", min(distances))