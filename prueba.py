datos = [ [14,25,72,27], [16,26,52,65],[24, 24, 45, 23],[26 ,35 ,51 ,27] , [17 ,31, 72, 21],[18 ,51 ,23, 14]
]
suma = 0
Lista = []
columna = int(input("Numero: "))
for fila in datos:
    suma = suma + fila [columna]
for dato in datos [columna]:
    Lista.append(dato)
print("Suma de la columna ",columna,": ", suma)
print("Mayor de la fila",columna,": ",max(Lista))
