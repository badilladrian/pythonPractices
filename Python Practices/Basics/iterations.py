# REPL READ EVAL PRINT LOOP 
# import module
# from module import function as alias
#//-----------------------------------------**---------------
name = "Eric"
age = 74
print (f"Hello, {name}. You are {age}.")
#//-----------------------------------------**---------------
"El asunto es que yo me llamo {0}. Y mi apellido es {1}".format(name,apellido)
f"El asunto es que yo me llamo {name}. Y mi apellido es {apellido}"
#//-----------------------------------------**---------------
prefix r"" is raw string 
#//-----------------------------------------**---------------
aliens_found - None
#//-----------------------------------------**---------------
student_names = ["MARK","JAMES","PETER"]
#//-----------------------------------------**---------------
student_names.append("HOMER")
#//-----------------------------------------**---------------
"Mark" in student_names == True
#//-----------------------------------------**---------------
"bigger" if a > b else"smaller" 
#//-----------------------------------------**---------------
len()==4 , del student_names[2]
#//-----------------------------------------**---------------
for variable in student_names:
    print("The studdent name is {0}").format(variable))
#//-----------------------------------------**---------------
x = 0
for index in range(10):
    x += 10
    print (f"The value of the number is {x}")
#//-----------------------------------------**---------------
student_names = ["MARK","JAMES","PETER","JUAN", "SMITH"]
for name in student_names:
    if name == "Bort":
        continue
        print ("Found him! "+ name)
    print ("Currently testing " + name)
#//-----------------------------------------**---------------
num = 10
while True:
    if num ==42:
        break;
    print ("Voy por el numero {0}".format(num))
    num= num+1;
#//-----------------------------------------**---------------
c = 5   #explicit
while c!=0:
    print(c)
    c -= 1

#//-----------------------------------------**---------------
while c:   #implicit
    print(c)
    c -=1
#//-----------------------------------------**---------------






