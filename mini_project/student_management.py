students = []

add_student= True

def std_details():
    std_dict={}
    std_dict["Student name"]=input("Enter student name: ")
    std_dict["Student id number"]=input("Enter student id number: ")
    std_dict["Student grade"]=input("Enter student grade: ")
    std_dict["Student average marks"]=input("Enter student average marks: ")
    students.append(std_dict)
   
def add_student():
    add_student=True

    while add_student:
        std_details()
        choice=input("Do you want to add another student.Type yes/no: ")
        choice_lower=choice.lower()
        if choice_lower == "no":
                add_student=False
                break
        elif choice_lower == "yes":

            continue

    
        else:
            print("Incorrect option!")
            break

#A function to view all students

def view_all():
    for student in students:
        print(student)

#A function to search student by their name and id

def view_by_name():
    name=input("Enter the student name you want to view details: ")
    student_id=input("Enter student id you want to view information: ")

    
    for student in students:
        if name == student.get("Student name") and student_id == student.get("Student id number"):
            print(student)
            break
    else:
        print("Student not found!")


   
    

#A function to update student details

def update_info():
    name=input("Enter name of student you want to update information: ")
    student_id=input("Enter student id you want to update informatiion: ")
    
    for student in students:
        if name == student.get("Student name") and student_id == student.get("Student id number"):
         
         student["Student grade"]=input("Enter student grade: ")
         student["Student average marks"]=input("Enter student average marks: ")
         student.update(student)

#A function to delete student's information
def delete_info():
    name=input("Enter name of student you want to delete information: ")
    student_id=input("Enter student id you want to delete informatiion: ")
    for student in students:
        if name == student.get("Student name") and student_id == student.get("Student id number"):
            students.remove(student)
            
            print("Student's informatiion has been deleted.")
            break
        else:
            print("Student's information not found")
            break

#Main function which asks for user input until it is stopped.
def main():
    print("Welcome!")
    
    while True:
        choice=input("Type '1' to add a student,'2' to view all student's information,\n'3' to view a single student information,'4' to update student info,\n'5' to delete student info and 'stop' to stop:")
        if choice == "stop":
            print("GoodBye!")
            break
        elif choice == "1":
            add_student()
        elif choice == "2":
            view_all()
        elif choice == "3":
            view_by_name()
        elif choice == "4":
            update_info()
        elif choice == "5":
            delete_info()
        else:
            print("Incorrect option!")
main()








    