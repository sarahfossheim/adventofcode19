min = 152085
max = 670283

matches = []

for number in range(min, max + 1):
    is_increasing = True
    has_double = False

    previous = ""

    for character in str(number):
        if character < previous:
            is_increasing = False
            break
        if character == previous:
            has_double = True

        previous = character

    if is_increasing and has_double:
        matches.append(number)

print(len(matches))