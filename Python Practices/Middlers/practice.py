#Declare Variables first student dictionary
student = {"name": "Adrian",
    "student_id": 123436,
    "feedback": None}
    
#Students list
students = []

#Try and Catch
def catchError ():
    student["last_name"]= "Badilla"
    try:
        last_name = student["last_name"]
        numbered_last_name = 3 + last_name
    except KeyError:
        print("Error finding that last name.")
    except TypeError as error:
        print("No puedo sumar un numero y un apellido! ")
        print(error)
    print("Aunque hay errores, se ejecuta el codigo.")

#Nested Functions
def get_students():
    try:
        def get_students_tittlecase():
            student_tittlecase = []
            for x in students:
                student_tittlecase.append(x["name"].title())
            return student_tittlecase
        student_tittlecase_names = get_students_tittlecase()
        print(student_tittlecase_names)
    except Exception as error:
        print(error)

#Print the list of existing students
def print_students_tittlecase():
    students_list = get_students()
    print (students_list)

#Function to add student
def add_student(name, student_id):
    student = {
        "name": name,
        "student_id": student_id
    }
    students.append(student)

#print 2 parameters in which one is a KEYWORD Arguments (Dictorionary)
def var_args(name, **kwargs):
    print(name)
    print(kwargs["programmer"])
#How kwargs are use in a Function
#var_args("Adrian", description="LovesPython", feedback=None, programmer=True)

add_student(name="Mark", student_id=15)
add_student(name="John", student_id=18)
add_student(student["name"], student["student_id"])
print(students)
print_students_tittlecase()

