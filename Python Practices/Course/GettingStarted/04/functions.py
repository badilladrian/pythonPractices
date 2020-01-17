student = {"name": "Adrian", "student_id": 123}
students = []

def get_students_titlecase():
	students_titlecase = []
	for student in students:
		students_titlecase.append(student["name"].title())
	return students_titlecase


def print_students_titlecase():
	students_titlecase = get_students_titlecase()
	print(students_titlecase)


def add_student(name, student_id=332):
	student = {"name": name, "student_id": student_id}
	students.append(student)


def save_file(student):
	try:
		f = open("students.txt", "a")
		f.write(student + "\n")
		f.close()
	except Exception:
		print("Could not save file")



print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)
print(students)
save_file(student_name)


