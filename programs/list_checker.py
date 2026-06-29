#List Checker

orig_list=[0,2,2,3,4,"A","B","A",0,3]

unique_list=[]
#A for loop which only add item for the original list if it is not present.
for item in orig_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)