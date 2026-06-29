#Reversing String

string=input("Enter something for a surprise: ")

reverse=" "
#A for loop which reverse the string by writing the last index first,
#till index 0 backwards one at a time.
for i in range(len(string)-1,-1,-1):
    reverse=reverse+string[i]
print(reverse)