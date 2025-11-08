# Day 4 – Discount Checker
# Author: Srivani Devaravajjala

amount = float(input("Enter total purchase amount: "))

if amount >= 1000:
    print("🎉 You got a 20% discount!")
elif amount >= 500:
    print("👏 You got a 10% discount!")
else:
    print("💰 No discount, but thank you for shopping!")