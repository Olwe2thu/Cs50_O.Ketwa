#import library
from cs50 import get_int

#promt & get user input
while True:
    height = get_int("Height: ")
    if 0 < height <=8:
        break

#print output
for i in range(1,height+1):
    print(" " * (height-i) + "#" * i + "  " + "#" *i)
