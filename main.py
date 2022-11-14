import csv



print("¡Bienvenido!")
print("1. Cargar un archivo csv con datos de 5 mascotas.")
print("2. Mostrar datos de mascotas cargadas en el sistema.")
print("3. Agregar mascota.")
print("4. Buscar mascota.")
print("5. Ordenar mascotas.")
print("6. Guardar mascotas en archivo CSV.")

opcion = int(input("Ingrese la opción que desee:"))

if opcion==1:
    print("Se cargaron los datos de 5 mascotas")
elif opcion==2:
    with open("pacientes.csv", encoding = 'utf-8') as f:
        archivo =csv.reader(f)
        for linea in archivo:
            print(linea)
elif opcion==3:
    print()
elif opcion==4:
    print()
elif opcion==5:
    print()
elif opcion==6:
    print()

else:
    print("Opción Incorrecta.")
