first= input("Enter your first number: ")
operator= input("enter operator (+,-,*,/,&v): ")
second= input("Enter your second nnumber: ")

first= int(first)
second= int(second)

if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "*":
    print(first*second)
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("invalid operator") 