import csv

with open("pacientes.csv", encoding = 'utf-8') as f:
    archivo =csv.reader(f)
    
    
    
    
    
    
  
print("¡Bienvenido! Ingrese los datos de mascota.")
name=input("Ingrese el nombre de la mascota:")
age=input("Ingrese la edad de la mascota:")
dueño=input("Ingrese el nombre del dueño:")
DNIdueño=input("Ingrese DNI de el dueño:")
