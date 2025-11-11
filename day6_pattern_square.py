# Day 6 – Square Pattern
# Author: Sri

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()  # new line after each row


for i in range(rows):
    for j in range(rows):
        print(f"{i}", end=" ")
    print() # new line after each row