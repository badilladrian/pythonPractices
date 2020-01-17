x = 500
print (x + "referencia en memoria: " + id(x))
x = 1000
# then the reference in memory for 500 is still existing, until the garbace collector cleans it
y = x 
print ("Ahora ambos objetos refieren al mismo valor en memoria: "
+ id(x) + " "+ id(y))

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Norwegian Blue")