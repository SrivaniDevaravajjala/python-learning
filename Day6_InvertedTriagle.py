#Pattern 3: Inverted Triangle
#Day6_InvertedTriagle.py

rows = int(input("enter number of rows: "))

for i in range(rows,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
