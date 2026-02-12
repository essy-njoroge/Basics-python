
firstnumber = float(input("Enter your first number: "))
operator = input("+ ,- ,* ,/ : ")
secondnumber = float(input("Enter your second number: "))

# Simple calculator program


if operator == "+":
    print("Result:", firstnumber + secondnumber)

elif operator == "-":
    print("Result:", firstnumber - secondnumber)

elif operator == "*":
    print("Result:", firstnumber * secondnumber)

elif operator == "/":
    print("Result:", firstnumber / secondnumber)

else:
    print("Invalid operator")





