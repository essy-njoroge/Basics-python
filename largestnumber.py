
first = int(input("Enter a number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

if first > second and first > third:
    print("The largest number is ", first)

elif second > first and second > third:
    print("The largest number is ", second)

else:
    print("The largest number is ", third)

