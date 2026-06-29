#Student management System

#A function to add student details
def details():
    
    name =input("Enter student name: ")
    identity=input("Enter student id: ")
    grade =input("Enter student grade: ")
    marks = input("Enter student average marks: ") 
    std_details = {"name":name,
                   "identity":identity,
                   "grade":grade,
                   "marks":marks}
    return std_details


#A function to view a student detail
def view(std_details):
    print(f"{std_details['name']}/{std_details['identity']} is in grade {std_details['grade']}.They got average {std_details['marks']}.")
    


#A function to view all students
def view_all(students):
    for student in students:
        print(student)

#A function to view student details if their name or id matches

def view_by_details(students):
    std_name=input("Enter student name: ")
    std_id=input("Enter student id number: ")
    for student in students:
        if std_name == student.get("name") and std_id == student.get("identity"):
            view(student)
        else:
            print("Student not found")

#A function to update the student's information

def update_info(students):
    std_name=input("Enter the sudent's name you want to update information: ")
    std_id=input("Enter student id number: ")
    new_dict =
    for student in students:
        if std_name == student.get("name") and std_id == student.get("identity"):
            pass

def main():
    students =[]
    student=details()
    students.append(student)
    print(students)
main()
