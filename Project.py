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


# Convert Hexadecimal to binary, octal and decimal
decimal_number = int(input("Enter a decimal number: "))
convert_decimal(decimal_number)

def hex_to_decimal(hex_num):
    """Convert hexadecimal to decimal."""
    return int(hex_num, 16)

def decimal_to_binary(decimal_num):
    """Convert decimal to binary."""
    return bin(decimal_num).replace("0b", "")

def decimal_to_octal(decimal_num):
    """Convert decimal to octal."""
    return oct(decimal_num).replace("0o", "")

def hex_to_all(hex_num):
    """Convert hexadecimal to decimal, binary, and octal."""
    decimal_num = hex_to_decimal(hex_num)
    binary_num = decimal_to_binary(decimal_num)
    octal_num = decimal_to_octal(decimal_num)
    return decimal_num, binary_num, octal_num

# Input from user
hex_input = input("Enter a hexadecimal number: ")
decimal_output, binary_output, octal_output = hex_to_all(hex_input)

# Display the results
print(f"Hexadecimal: {hex_input}")
print(f"Decimal: {decimal_output}")
print(f"Binary: {binary_output}")
print(f"Octal: {octal_output}")
