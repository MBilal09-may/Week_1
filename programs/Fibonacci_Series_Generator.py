#Fibonacci Series Generator
#Asking how many numbers does the user wants to generate
number=int(input("How many numbers do you want to generate:"))

#Initialising first two numbers
first_num=0
second_num=1

#A loop which runs from the range 1 to number and prints the number

for i in range(1,number+1):
    print(first_num)
    next=first_num+second_num
    first_num=second_num
    second_num=next
