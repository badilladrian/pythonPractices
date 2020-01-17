"""Variables objetos referencias y memorias
Si usamos x = 500 
si usamos x = 1000
si usamos y = x
si luego cambiamos x = 1000"""

x = 500
print (id(x))
x = 1000
# then the reference in memory for 500 is still existing, 
# until the garbage collector cleans it
y = x 
print (id(x))
print(id(y))

"""PYTHON ONLY HAVE
NAMED REFERENCES TO OBJECTS"""
