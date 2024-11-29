#FROM BINARY TO OCTAL,DECIMAL AND HEXADECIMAL

def number_to_decimal(number, base):

    decimal = int(number, base)
    
    octal = oct(decimal)
    hexadecimal = hex(decimal)

    print("decimal: " + str(decimal))
    
    print("octal: " + str(octal[2:]))
    print("hexadecimal: " + str(hexadecimal[2:]))

number = str(input("Enter a number in binary: "))
base = 2

number_to_decimal(number,base)


# Function to convert decimal to binary, hexadecimal, and octal
def convert_decimal(number):
    # Convert decimal to binary, hex, and octal
    binary = bin(number)[2:]  # bin() returns a string with '0b' prefix, so we slice it off
    hexadecimal = hex(number)[2:].upper()  # hex() returns a string with '0x' prefix, remove it and convert to uppercase
    octal = oct(number)[2:]  # oct() returns a string with '0o' prefix, remove it

    # Print the results
    print(f"Decimal: {number}")
    print(f"Binary: {binary}")
    print(f"Hexadecimal: {hexadecimal}")
    print(f"Octal: {octal}")


# Take input from the user
decimal_number = int(input("Enter a decimal number: "))
convert_decimal(decimal_number)
