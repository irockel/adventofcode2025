#
# This solves the first part of the Day 1 riddle
# It counts the amount of 0s where the safe knob ends.
#
pos = 50
zero_count = 0

with open('input.txt') as f:
    for line in f:
        if line[0] == "R":
            pos += int(line[1:])
        else:
            pos -= int(line[1:])

        pos = abs(pos % 100)

        if pos == 0:
            zero_count += 1

print("The amount of zeros is %r." % zero_count)