#
# This solves the second part of the Day 1 riddle
# It counts the amount of 0s the safe knob passes or stops.
#
pos = 50
old_pos = 50
zero_count = 0

with open('input.txt') as f:
    for line in f:
        rotate_count = abs(int(line[1:]) // 100)
        if line[0] == "R":
            pos += int(line[1:]) % 100
        else:
            pos -= int(line[1:]) % 100

        zero_count += rotate_count
        if pos < 0:
            if old_pos != 0:
                zero_count += 1
            pos = pos + 100
        elif pos >= 100:
            zero_count += 1
            pos = pos - 100
        elif pos == 0:
            zero_count += 1

        old_pos = pos

print("The amount of zeros is %r." % zero_count)