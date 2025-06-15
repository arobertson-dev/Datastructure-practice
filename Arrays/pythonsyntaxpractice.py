""" if (5 > 2):
    print("Five is greater than two!")
elif (5 < 2):
    print("Five is less than two!")
else:
    
"""
# This is a block comment


userOne = input("Enter the first number: ").replace(" ", "")
userTwo = input("Enter the second number: ").replace(" ", "")
f1 = int(userOne)
f2 = int(userTwo)
if f1 % 2 == 0:
    print("The first number is even")
else:
    print("The first number is odd")
if f2 % 2 == 0:
    print("The second number is even")
else:
    print("The second number is odd")



f3 = f1 + f2
print(f3)
print("student one's number is", f1)
if f1 >= 90:
    print("You got an A")
elif f1 >= 80:
    print("You got a B")
elif f1 >= 70:
    print("You got a C") 
elif f1 >= 60:
    print("You got a D")
else:
    print("You got an F")
          
print("student two's number is", f2)
if f2 >= 90:
    print("You got an A")
elif f2 >= 80:
    print("You got a B")
elif f2 >= 70:
    print("You got a C") 
elif f2 >= 60:
    print("You got a D")
else:
    print("You got an F")

inputX = int(input("Enter a number: "))

 
for i in range(1, inputX+1):


