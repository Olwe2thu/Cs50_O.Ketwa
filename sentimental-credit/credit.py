from cs50 import get_int
import re

def main():
#variables
    multipliedNums,addedNums=0,0

    #prompt user input
    while True:
        number = int(input("Number: "))
        if number > 0:
            break

    #finding len
    length = len(str(number))
    strNum= str(number)

    #looping throught  card number & multiplying
    for i in range(length -2, -1,-2):
        digit = int(strNum[i]) * 2
        if digit >=10:
            digit= digit // 10 + digit % 10
        multipliedNums+=digit
        
    #looping throught  card number & adding
    for i in range(length -1,-1 ,-2):
        addedNums+=int(strNum[i])

    temp_total = (addedNums + multipliedNums) % 10
    round(temp_total)

    #calling method
    checkType(number,temp_total)

#check and print card type
def checkType(number,temp_total):
    str_number = str(number)

    #searching starting vallues of string
    v = re.search("^4",str_number)
    m = re.search("^51|^52|^53|^54|^55",str_number)
    a = re.search("^37",str_number)

    if v  and round(temp_total) == 0 and len(str_number) >10:
        print("VISA")
    elif m and round(temp_total) == 0:
        print("MASTERCARD")
    elif a  and round(temp_total) == 0:
        print("AMEX")
    else:
        print("INVALID")

if __name__ == "__main__":
    main()
