# Day 4 – Eligibility Check (enhanced validation)
# Author: Sri

age = int(input("Enter your age: "))

if age < 18:
    print("❌ You are too young to drive.")
else:
    # Ask until valid response
    while True:
        has_license = input("Do you have a valid driving license (yes/no)? ").strip().lower()

        if has_license == "yes":
            print("✅ You can legally drive.")
            break
        elif has_license == "no":
            print("⚠️ You need a valid license to drive.")
            break
        else:
            print("❌ Invalid input. Please type 'yes' or 'no'.")