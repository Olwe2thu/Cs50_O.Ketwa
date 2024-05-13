from cs50 import get_string

def main():
    text = input("Text:")

    # calculating grade index using formula
    letterAvg = letterCount(text) / wordCount(text) * 100
    sentenceAvg = sentenceCount(text) / wordCount(text) * 100
    index = round(0.0588 * letterAvg - 0.296 * sentenceAvg - 15.8)

    printIndex(index)

#print index
def printIndex(index):
    if index <= 0:
        print("Before Grade 1")
    elif index <= 16:
        print("Grade {index}", index)
    else:
        print("Grade 16+")

#letter count method
def letterCount(text):
    lCount = 0

    for i in range(0,len(text)):
        if text[i].isalpha():
            lCount += 1
    return lCount

#word count method
def wordCount(text):
    wCount = 0

    for i in range(0,len(text)):
        if text[i] == " ":
            wCount +=1
    return wCount +1

# sentence count method
def sentenceCount(text):
    sCount = 0

    for i in range(0,len(text)):
        if text[i] == "." or text[i] == "?" or text[i] ==  "!":
            sCount += 1
    return sCount

# checks if script is run directly/imported.Call main
if __name__ == "__main__":
    main()
