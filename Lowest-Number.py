#Create a program that ask 3 numbers.
#Find the lowest number using if-else Statement
#Display the lowest number

#Steps
# 1. Gather the 3 numbers and store
First = float(input("Insert First Number: "))
Second = float(input("Insert Second Number: "))
Third = float(input("Insert Third Number: "))

# 2. Test the first number to second and third number
if First < Second and First < Third:
    print(f"The Lowest Number is {First}")

# 3. Test the second number to first and third number
elif Second < First and Second < Third:
    print(f"The lowest Number is {Second}")

# 4. If the first and second number is higher than the third number. Display the third number
else:
    print(f"The lowest Number is {Third}")