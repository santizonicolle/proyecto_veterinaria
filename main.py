import csv

print("¡Bienvenido!")
print("1. Cargar un archivo csv con datos de 5 mascotas.")
print("2. Mostrar datos de mascotas cargadas en el sistema.")
print("3. Agregar mascota.")
print("4. Buscar mascota.")
print("5. Ordenar mascotas.")
print("6. Guardar mascotas en archivo CSV.")

while True:
    opcion = int(input("Ingrese la opción que desee:"))

    if opcion==1:
        print("Se cargaron los datos de 5 mascotas")

    elif opcion==2:
        with open("pacientes.csv", encoding = 'utf-8') as f:
            archivo =csv.reader(f)
            for linea in archivo:
                print(linea)

    elif opcion==3:
        name=input("Ingrese el nombre de la mascota:")
        raza=input("Ingrese la raza:")
        age=input("Ingrese la edad de la mascota:")
        dueño=input("Ingrese el nombre del dueño:")
        dni_dueño=input("Ingrese DNI de el dueño:")

        add_mascota=[name,raza,age,dueño,dni_dueño]
        with open('pacientes.csv', 'a', encoding = 'utf-8') as f:
            archivo = csv.writer(f)
            archivo.writerow(add_mascota)
            f.close()

    elif opcion==4:
        print(f"¡Busca a la mascota!\n 1. Nombre de mascota \n 2. Raza\n 3. Edad \n 4. Nombre del Dueño\n 5. DNI dueño\n")
        option_search=input("Elige tu método de búsqueda:")
        if option_search == "1":
            name=input("Ingrese el nombre de la mascota a buscar:")
            with open("pacientes.csv", encoding = 'utf-8') as f:
                archivo =csv.reader(f)
                for linea in archivo:
                    if linea[0] == name:
                        print(linea[0:5])
                        
        print()
    elif opcion==5:
        print()
    elif opcion==6:
        print()

    else:
        print("Opción Incorrecta. Elige un número válido.")
