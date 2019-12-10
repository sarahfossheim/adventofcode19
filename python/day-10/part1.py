from input import asteroids
import math
from collections import defaultdict


asteroids_coordinates = []
for row in range(0, len(asteroids)):
    for column in range(0,len(asteroids[row])):
        asteroids_coordinates.append((row, column, asteroids[row][column]))

asteroid_visibility = defaultdict(set)
for asteroid_1 in asteroids_coordinates:
    for asteroid_2 in asteroids_coordinates:
        if asteroid_1 == asteroid_2:
            continue

        if asteroid_1[2] == "#" and asteroid_2[2] == "#":
            angle = math.atan2(asteroid_2[0] - asteroid_1[0], asteroid_2[1] - asteroid_1[1]) % (2 * math.pi)
            asteroid_visibility[asteroid_1].add(angle)




print(len(max(asteroid_visibility.values(), key=len)))
