#Student Marks Average Calculator

subject=int(input("Enter number of subjects: "))
index = str(subject)
count=1
total = 0

while count <= subject:
    marks =int(input("Enter marks: "))
    total=total+marks
    count+=1
average =round(total/subject,2)
print(f"The total marks of the student is {total} out of {subject*100},the average marks of the student is {average}")