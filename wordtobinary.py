#!/usr/bin/python3

dict = {"a": '0', "b": '1', "c": '2', "d": '3', "e": '4', "f": '5', "g": '6',
 "h": '7', "i": '8', "j": '9', "k": '10', "l": '11', "m": '12', "n": '13',
 "o": '14', "p": '15', "q": '16', "r": '17', "s": '18', "t": '19', "u": '20',
 "v": '21', "w": '22', "x": '23', "y": '24', "z": '25'}


def translate(word):
    string = ""
    number = 0
    for i in word:
        string = dict[i]
        number = number + int(string)
    return number

# Output the binary number
def tobinary(n):
    string = "" # Empty string to store our output
    number = int(n) # Change input to integer so we can operate on it
    while number > 0:                   # Loop until number is zero
        if not number%2 == 0:           # Check if the number is odd
            string += "1" # Add 1 to the end of the output string above
            number = (number -1) / 2
        else:                           # If the number is even
            string += "0" # Add 0 to the end of the output string above
            number = number / 2
    print(string[::-1]) # Output is backwards so we need to reverse it


tobinary(translate(input('> ').lower()))   #Get input, change to lower case,
                                        #run Functions
