from cs50 import get_float

#declare variables
quarters,dimes,nickels,pennies,count = 0.25, 0.10, 0.05, 0.01, 0

#prompt and get user input
while True:
    change = get_float("Chage owed: ")
    if change > 0:
        break
#calculate the change
while change > 0:
    if change >= quarters:
        change =round(change-quarters,2)
        count+=1
    elif change >= dimes:
        change =round(change- dimes,2)
        count+=1
    elif change >= nickels:
        change = round(change- nickels,2)
        count+=1
    else:
        change =round(change- pennies,2)
        count+=1

#print user change
print(f" {count}")
