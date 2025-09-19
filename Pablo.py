# Consulta el tamaño o la longitud de la variable "var_1" y calcula la división de ese numero entre "7" redondeado a 4 decimales
var_1 = "Módulo 1 de Python "
longitud_var_1 = len(var_1)
print(longitud_var_1)
print(round(longitud_var_1 / 7, 4))
# pedir al usuario que introduzca su edad, y después imprimir en la pantalla si es meyor de edad o no
edad = int(input("Introduce tu edad: "))
if edad >= 18 and edad < 120:
    print("Eres mayor de edad.")
elif edad >= 120:
    print("Estás muerto.")
else:
    print("No eres mayor de edad.")
