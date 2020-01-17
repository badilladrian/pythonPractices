students = []


class Student:

	school_name = "Springfield Elementary"

	def __init__(self, name, student_id=332):
		self.name = name
		self.student_id = student_id
		students.append(self)

	def __str__(self):
		return "Student " + self.name

	def get_name_capitalize(self):
		return self.name.capitalize()

	def get_school_name(self):
		return self.school_name

		#I can refer to static variables from inherence
		#By these defining the value over again
		#And by overloading if create method with different logic

class Ejemplo(Student):
	school_name = "Nombre Escuela" # aqui lo redefini

	def get_school_name(self):
		return "Nombre de la escuela Ahora!"
		#utilizo el metodo para dar otro resultado
		#dentro de esta clase

	def get_name_capitalize(self):
		valorOriginal = super().get_name_capitalize()
		return valorOriginal + " Va al Trabajo!"


adriancito = Ejemplo("Adrian")
print(adriancito.get_name_capitalize())
