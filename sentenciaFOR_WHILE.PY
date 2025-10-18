# SENTENCIAS FOR WHILE EN PYTHON
# MANEJO DE CADENAS
# MANEJO DE LISTAS
# MANEJO DE DICCIONARIOS
# MANEJO DE FUNCIONES
# CREACION DE CLASES
            #(desde, hasta, incremento/decremento)
""" for (int i; i<5; i++){ en lenguaje de c++

} """
#Entrada 6 proceso: 1+2+3+4+5 salida 21

""" num = int(input("Ingrese un numero: "))
suma = 0
for i in range(num+1):
    suma = suma + i
    #suma +=1
print(suma) """

""" num = int(input("Ingrese un numero: "))
suma = 0
i = 1
while i <= num:
    suma = suma + i
    i +=1

print(suma) """

#manejo de cadenas
""" nombre = "HOLA"
print(nombre.lower())
for i in range(0, len(nombre),1):
    print(nombre[i], end="") """


edades = [23,15,35,21, True]


for i in edades:
    print(i, end=" ")


""" edades.insert(0,1000)
valor = edades.pop(1)
print("Menor elemento: ", max(edades))
print("velor que se quito de la lista", valor)
#print(type(edades))
#print(edades)

for i in edades:
    print(i, end=" ")
print()
for i in range(0, len(edades),1):
    print(edades[i], end=" ") """
