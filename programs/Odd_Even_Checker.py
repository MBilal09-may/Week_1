#Odd/Even Checker
print("Welcome to Even and Odd Checker!")
while True:
    choice = input("Type '1' to check number,'2' to exit:")

    if choice =="2":
        print("GoodBye!")
        break
    else:

        number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("It is an Even Number!")
    else:
        print("It is an Odd Number!")


