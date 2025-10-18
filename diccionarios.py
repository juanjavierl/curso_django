# MANEJO DE DICCIONARIOS
# MANEJO DE FUNCIONES
# CREACION DE CLASES

datos = {'nombre':'Maria','edad':25, 1:True, 'info': {'carrera':'sistemas'}}

#print(datos['edad'])

""" for i in datos:
    print(i, ": ",datos[i]) """
datos["info"] = "Activo"
""" 
for c, v in datos.items():
    print(c, ": ",v) """


""" print("total de items: ",len(datos))
print(datos.pop('informacion', "No existe datos"))
print(datos) """

s = ""
def nombre_en_mayuscula(nombre):
    return nombre.upper()

def saludar(nombre, edad, estado="Activo"):
    persona = nombre_en_mayuscula(nombre)
    print(persona)
    print("tu edad es:", edad, "estado: ", estado)
    print(s)

#saludar("Antonio", 25, "Inactivo")

def mi_suma():
    num = int(input("Ingrese un numero: "))
    suma = 0
    i = 1
    while i <= num:
        suma = suma + i
        i +=1

    return suma

resultado = mi_suma()
print(resultado)