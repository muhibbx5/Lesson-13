print("Do you want to make a floyd triangle")
n=int(input("Please enter numbers and rows to make floyd triangle: "))
num=1
for i in range(1,n+1):
      for j in range(1,i+1):
            print(num , end=" ") 
            num=num+1
      print()
      