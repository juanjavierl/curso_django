class Persona:
    def __init__(self, ci):
        self.ci = ci
    

class Empleado(Persona):
    def __init__(self, nombre, edad, ci):
        self.nombre = nombre
        self.edad = edad
        super().__init__(ci)
    
    def __str__(self):
            #print(f"{self.nombre} tu edad es: {self.edad}")
        return f"{self.nombre} tu edad es: {self.edad}"


emp = Empleado("Maria", 25, 12345678)

print(emp.ci)
    