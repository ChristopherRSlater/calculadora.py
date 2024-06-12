import re

print("The magical calculator")
print("Escribe 'quit' para poder salir\n")

previus = 0
run = True

def performMath():
    global run
    global previus
    equation = ""
    if previus ==0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previus))
        
        
    if equation == 'quit': 
        print("Goodbye")
        run = False
    else:
        euation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previus== 0:
            previus = eval(equation)
        else:
            previus = eval(str(previus)+ equation)

while run:
    performMath()