# Day 2 - Type Conversion Practice
# Author: Sri

# 1️⃣ Ask user for input (string by default)
age_input = input("Enter your age: ")
height_input = input("Enter your height in meters: ")

# 2️⃣ Convert to proper data types
age = int(age_input)
height = float(height_input)

# 3️⃣ Display original types
print(f"The type of age_input is {type(age_input)}")
print(f"The type of age after conversion is {type(age)}")
print(f"The type of height after conversion is {type(height)}")

# 4️⃣ Use converted values in calculations
next_age = age + 1
bmi_sample = 65 / (height ** 2)

# 5️⃣ Print formatted output
print(f"\nHi, next year you’ll be {next_age} years old!")
print(f"Sample BMI if your weight is 65 kg: {bmi_sample:.2f}")

print(f"Your age as string is '{str(age)}'")
print(f"Is your height > 1.5 meters? {height > 1.5}")