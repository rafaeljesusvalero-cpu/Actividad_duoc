import os
os.system("cls")
import time
# ETAPAS:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.
try:
    edad = int(input("Ponga su edad \n"))
    if edad >= 18:
        print ("Eres mayor de edad")
    else:
        print ("Eres menor de edad")
except:
    print("Ingrese valor numérico")

time.sleep(3)

# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1

user1 = "pedro"
passwd1 = "1234"
user2 = "angel"
passwd2 = "a4s1"

user = input("Ingrese su nombre de usuario \n")
passwd = input ("Ingrese su contraseña\n")
if user == user1 and passwd == passwd1 or user == user2 and passwd == passwd2:
    print(f"Hola {user}, puede acceder al sistema")
else:
    print("No puede acceder")

time.sleep (3)
# Solicitar el ingreso de 3 notas por pantalla, 
# luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), 
# finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

cantidad = 3 
acum = 0
for x in range(3): 
    nota= float(input(f"Ingrese nota ({x+1})\n"))
    acum = acum + nota 
promedio = acum / cantidad
if promedio >= 4 :
    print("Aprobado")
else:
    print("Reprobado")
    
time.sleep(3)