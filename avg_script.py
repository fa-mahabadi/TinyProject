import sys

total = 0

for i in (1, len(sys.argv)):
    total += int(i)

avg = total / len(sys.argv)
print(avg)
