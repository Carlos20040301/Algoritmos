import gspread
import random


#Array para guardar los números obtenidos
arr = []

#Array para convertirlos a enteros
enteros = []
enteros_2 = []
enteros_3 = []

#Uso de la clave para acceder al documento 
gc = gspread.service_account(filename="clave") #Se elimino la clave para proteccion de la cuenta 

#Abrir por titulo
sh = gc.open('Conexion')

#Seleccionar hoja
wks = sh.get_worksheet(0)

#Cambiar aspecto
wks.format("C1:F11", {
    "backgroundColor": {
      "red": 160.0,
      "green": 160.0,
      "blue": 255.0
    },
    "horizontalAlignment": "CENTER",
    "textFormat": {
      "foregroundColor": {
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
      },
      "fontSize": 11,
      "bold": True
    }
})

#Titulo de la celda
wks.update("C1", "Random")

#Ciclo que genera numeros aleatorios
for i in range(2 , 12):
    wks.update("C" + str(i), random.randrange(100))

#Obtener numeros 
for i in range(2, 12):
    val = wks.acell('C'+str(i)).value
    arr += [val]

#Mostrar arreglo 
print("Arreglo tipo string")
print(arr)
print("")

#Convertir el array inicial en enteros (String a int)
for element in arr:
    enteros.append(int(element)) 
    enteros_2.append(int(element))
    enteros_3.append(int(element))  

#Arreglo convertido a enteros
print("Primer arreglo convertido a enteros")
print(enteros)
print("")
print("Segundo arreglo convertido a enteros")
print(enteros_2)
print("")
print("Tercer arreglo convertido a enteros")
print(enteros_3) 
print("")


#Titulo de la celda
wks.update("D1", "Bubble sort")

#Bubble sort
for i in range(len(enteros)):
    for j in range(len(enteros)-i-1):
        if enteros[j] < enteros[j + 1]:
            temp = enteros[j]
            enteros[j] = enteros[j+1]
            enteros[j+1] = temp
            

print("Arreglo ordenado con bubble")
print(enteros)
print("")

#Ciclo para colocar Bubble sort 
j = 0
for y in range(2, 12):
    if j >= 0 and j < 11 :
        wks.update("D" + str(y), enteros[j])
        j += 1
            

#Titulo de la celda
wks.update("E1", "Selection sort")

#Selection sort
for ind in range(len(enteros_2)):
        min_indice = ind
 
        for j in range(ind + 1, len(enteros_2)):
            if enteros_2[j] > enteros_2[min_indice]:
                min_indice = j
        
        (enteros_2[ind], enteros_2[min_indice]) = (enteros_2[min_indice], enteros_2[ind])

print("Arreglo ordenado con Selection")
print(enteros_2)
print("")        

#Ciclo para colocar Selection sort
j = 0
for y in range(2, 12):
    if j >= 0 and j < 11 :
        wks.update("E" + str(y), enteros[j])
        j += 1


#Titulo de la celda
wks.update("F1", "Insertion Sort")

#Insertion sort
for step in range(1, len(enteros_3)):
        key = enteros_3[step]
        j = step - 1
                
        while j >= 0 and key > enteros_3[j]:
            enteros_3[j + 1] = enteros_3[j]
            j = j - 1
        
        enteros_3[j + 1] = key

print("Arreglo ordenado con Insertion")
print(enteros_3)
print("")        

#Ciclo para colocar Insertion sort 
j = 0
for y in range(2, 12):
    if j >= 0 and j < 11 :
        wks.update("F" + str(y), enteros_3[j])
        j += 1
