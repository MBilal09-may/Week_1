#Factorial Calculator 
print("Welcome!")
number = int(input("Enter the number to calculate its factorial calculation:"))
#set the minimal value to 1 as it is a neutral value
result = 1
#A for loop which starts from 1 to the actual number
for i in range(1,number+1):
    result = result * i #Number keeps multiplying till it reaches the final number
    print(result)
