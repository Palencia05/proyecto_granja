# Clase Animal
class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.peso = 0

    def alimentar(self):
        print(f"{self.tipo} {self.nombre} ha sido alimentado.")

    def vacunar(self):
        print(f"{self.tipo} {self.nombre} ha sido vacunado.")

    def registrar_peso(self, peso):
        self.peso = peso
        print(f"Peso de {self.tipo} {self.nombre} registrado: {self.peso} kg")

    def __str__(self):
        return f"{self.tipo} llamado {self.nombre}"

# Clase Corral (agrega animales)
class Corral:
    def __init__(self, id_corral):
        self.id_corral = id_corral
        self.animales = []

    def asignar_animal(self, animal):
        self.animales.append(animal)
        print(f"{animal} asignado al corral {self.id_corral}.")

    def quitar_animal(self, animal):
        if animal in self.animales:
            self.animales.remove(animal)
            print(f"{animal} retirado del corral {self.id_corral}.")

    def limpiar(self):
        print(f"Corral {self.id_corral} ha sido limpiado.")

    def listar_animales(self):
        print(f"Corral {self.id_corral} contiene:")
        for animal in self.animales:
            print(f" - {animal}")

# Clase Empleado (parte de la composición con Granja)
class Empleado:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def realizar_tarea(self, tarea):
        print(f"{self.nombre} está realizando la tarea: {tarea}")

    def registrar_asistencia(self):
        print(f"Asistencia registrada para {self.nombre} ({self.rol})")

    def reportar_incidencias(self, incidencia):
        print(f"{self.nombre} ha reportado: {incidencia}")

# Clase Granja (composición: contiene empleados)
class Granja:
    def __init__(self, nombre):
        self.nombre = nombre
        self.corrales = []
        self.empleados = []
