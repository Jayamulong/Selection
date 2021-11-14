#Create a program that ask for an age of a person
#Display the life stages of the person

#Steps
# 1. Ask the and store
Age = int(input("Insert your age: "))

# 2. Test if life stage of a kid
if Age >= 0 and Age <= 12:
    print("Kid")

# 3. Test if life stage of a teen
elif Age >=13 and Age <= 17:
    print("Teen")

# 4. Test if Debut
elif Age == 18:
    print("Debut")

# 5. if 19 and above, print adult
else:
    print("Adult")