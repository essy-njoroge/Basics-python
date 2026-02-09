#a python program that allows the user enter a random  and checks whether the number is even or odd

number = int(input("Enter a number: "))

if number == 0:
    print("Number is neutral")

elif number % 2 == 0:
    print("The number is even.")

else:
    print("The number is odd.")



