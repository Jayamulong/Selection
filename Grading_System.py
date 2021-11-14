#Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description

import math

#Steps:
# 1. Ask the grade, roundoff, convert and store.
Grade = round(float(input("Insert Grade: ")))

# 2. Test 97 - 100
if Grade >=97 and Grade <=100:
    print(f"Input Grade: {Grade}")
    print("Grade/Mark: 1.0")
    print("Description: Excellent")

# 3. Test 94 - 96
elif Grade >=94 and Grade <=96:
    print(f"Input Grade: {Grade}")
    print("Grade/Mark: 1.25")
    print("Description: Excellent")

# 4. Test 91 - 93
elif Grade >=91 and Grade <=93:
    print(f"Input Grade: {Grade}")
    print("Grade/Mark: 1.5")
    print("Description: Very Good")

# 5. Test 88 - 90
elif Grade >=88 and Grade <=90:
    print(f"Input Grade: {Grade}")
    print("Grade/Mark: 1.75")
    print("Description: Very Good")

# 6. Test 85 - 87
elif Grade >=85 and Grade <=87:
    print(f"Input Grade: {Grade}")
    print("Grade/Mark: 2.0")
    print("Description: Good")

# 7. Test 82 - 84
elif Grade >=82 and Grade <=84:
    print(f"Input Grade: {Grade}")
    print("Grade/Mark: 2.25")
    print("Description: Good")

# 8. Test 79 - 81
elif Grade >=79 and Grade <=81:
    print(f"Input Grade: {Grade}")
    print("Grade/Mark: 2.5")
    print("Description: Satisfactory")

# 9. Test 76 - 78
elif Grade >=76 and Grade <=78:
    print(f"Input Grade: {Grade}")
    print("Grade/Mark: 2.75")
    print("Description: Satisfactory")

# 10. Test 75
elif Grade ==75:
    print(f"Input Grade: {Grade}")
    print("Grade/Mark: 3.0")
    print("Description: Passing")

# 11. Test 65 - 74
elif Grade >=65 and Grade <=74:
    print(f"Input Grade: {Grade}")
    print("Grade/Mark: 5.0")
    print("Description: Failure")

# 12. If lower print Inc., W, or D
else:
    print("Inc. or Incomplete")
    print("W or Withdrawn")
    print("D or Dropped")
