# day6_pattern_triangle.py
# author: Srivani Devaravajjala

# input rows num from user:

rows = int(input("enter number of rows: "))

for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
    print()
    
