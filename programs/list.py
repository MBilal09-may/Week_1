#Finding largest number in the list

new_list=[]
while True:
    choice=input("Enter '1' to start.'2' to view list.'3'to exit:")
    
    if choice == "1":
        number=int(input("Enter a number in the list:"))
        new_list.append(number)    
    elif choice =="2":
        print(new_list)
        
    elif choice == "3":
        
        break
    else:
        print("Incorrect choice!")
largest=new_list[0]
for num in new_list:
    if num > largest:
        largest=num
print(f"The largest number in the list is {largest}")