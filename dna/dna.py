import csv
import re
from sys import argv


def main():

    # TODO: Check for command-line usage
    if len(argv) !=3:
        print(f"Missing Arguments")
        exit(1)

    # TODO: Read database file into a variable
    #initialize lists to store data
    records = []
    header = []

    with open(argv[1], 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

    #read each row
        for row in reader:
            records.append(row)

    # TODO: Read DNA sequence file into a variable
    sequence = []

    #access and read file
    with open(argv[2], 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            seq = row

            sequence.append(seq)
    #convert list of list into string
    innerList = sequence[0]
    strSequence = ''.join(innerList)

    # TODO: Find longest match of each STR in DNA sequence -
    counters={}

    for STR in header[1:]:
        countMax = longest_match(strSequence, STR)
        # keeping value of the longest match
        counters[STR]=countMax


    # TODO: Check database for matching profiles
    match_found = False
    for record in records:
        name = record[0]
        #-keeping str counts foreach str
        counts = [int(count) for count in record[1:]]
        # Compare the extracted counts with the counts obtained from the DNA sequence- comparing
        if counts == [counters[STR] for STR in header[1:]]:
            print(f"{name}")
            match_found = True
            break

    #if not match after looping throught all records
    if match_found == False:
        print("No match")

    # End of main function
    return

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0
        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
