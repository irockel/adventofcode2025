#
# This solves the first part of the Day 1 riddle
# It counts the amount of 0s where the safe knob ends.
#
pos = 50
silly_values = 0

with open('input.txt') as f:
    for line in f:
        ranges = line.split(",")
        for r in ranges:
            tokens = r.split("-")
            start = tokens[0]
            end = tokens[1]

            i = int(start)
            print("checking range %s to %s " % (start, end))
            while i <= int(end):
                str_i = str(i)
                len_i = len(str_i)
                first_half = str_i[:len_i // 2]
                second_half = str_i[len_i // 2:]
                if first_half == second_half:
                    #print("found silly value: %r" % i)
                    silly_values += i
                i+=1

print("The amount of silly values is %r." % silly_values)