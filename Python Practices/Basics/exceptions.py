Exceptions

student = {
"name": "Adrian",
"student_id": 123436,
"feedback": None
}

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