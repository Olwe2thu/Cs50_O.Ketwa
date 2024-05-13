#import library
from cs50 import get_int

# #promt & validate user input
while True:
    height = get_int("Height: ")
    if 0 < height <= 8:
        break

# Print output
for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i)



