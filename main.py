print ("Half pyramid pattern of * ")
n=int(input("Please enter the number of rows you want: "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()