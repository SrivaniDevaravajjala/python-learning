# Day 3 – Boolean & Comparison Practice

age = int(input("Enter your age: "))
has_license = input("Do you have a driving license (yes/no)? ")

# convert text to boolean
has_license = has_license.lower() == "yes"

print(f"Age >= 18: {age >= 18}")
print(f"Has license: {has_license}")
print(f"Can drive? {age >= 18 and has_license}")