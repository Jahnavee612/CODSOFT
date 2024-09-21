print("~~~~~Calculator~~~~~")

num1 = float(input("Enter first number here: "))
num2 = float(input("Enter second number here: "))

operator = input("Enter the (+,-,*,/): ") 

if operator  == "+":
    print ("The addition of given two numbers is", num1 + num2)
elif operator == "-":
    print ("The subtraction of given two numbers is", num1 - num2)
elif operator == "*":
    print ("The multiplication of given two numbers is", num1 * num2)
elif operator == "/":
    print ("The division of given two numbers is", num1 / num2)
else:
    print ("Invalid Input")
