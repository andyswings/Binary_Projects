#!/usr/bin/python3

def convert():
    number = int(input("> ")) # Get the original number
    n = "" # Blank string to store the output
    while number > 0: # Loop until the original number is 0
        if number %2 == 0: # Number is even
            number = number / 2
            n += "0" # Add 0 to the end of the output string above
        else: # Number is odd
            number = (number -1) / 2
            n += "1" # Add 1 to the end of the output string above
    print(n[::-1]) # Output is backwards so we need to reverse it

convert() # Run our function
