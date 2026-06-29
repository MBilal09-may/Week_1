#List Checker

orig_list=[]

unique_list=[]
item = ""
while item!="stop":
    item=input("Enter something in the list.Type stop to stop: ")
    if item == "stop":
        break
    else:
        
        orig_list.append(item)
   

#A for loop which only add item for the original list if it is not present.
for item in orig_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)