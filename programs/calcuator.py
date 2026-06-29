#Simple calculator

#Function for addition

def add(x,y):
    return x + y

# Function for subraction

def sub(x,y):
    return x - y 

#Function for multiplication

def mul(x,y):
    return x * y 

#Function for division

def div(x,y):
    return x / y 


    
     

#Main function which performs all tasks
def main():
    #While loop runs the calculator unless it is exited
    while True:
        print("Welcome!")
        print("Type '1' to add")
        print("Type '2' to subtract")
        print("Type '3' to multiply")
        print("Type '4' to divide")
        print("Type '5' to exit")

        choice = input("Enter choice:")

    
    #Exit loop if choice is 5
        if choice == "5":
            print("GoodBye!")
            break

        #Ask the user for two numbers
        num_1=int(input("Enter first number:"))
        num_2=int(input("Enter second number:"))   


        if choice == "1":
            print(add(num_1,num_2))
        elif choice == "2":
            print(sub(num_1,num_2))
        elif choice == "3":
            print(mul(num_1,num_2))
        elif choice == "4":
            print(div(num_1,num_2))
        else:
            print("Invaid Option!")


main()

