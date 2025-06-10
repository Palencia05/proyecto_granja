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

    def agregar_corral(self, corral):
        self.corrales.append(corral)
        print(f"Corral {corral.id_corral} agregado a la granja.")

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} contratado para la granja.")

    def cerrar(self):
        print("Cerrando la granja. Todos los empleados dejan de estar vinculados.")
        self.empleados.clear()

# Ejemplo de uso
if __name__ == "__main__":
    # Crear granja
    granja = Granja("El Buen Pastor")

    # Crear empleados
    emp1 = Empleado("Carlos", "Alimentación")
    emp2 = Empleado("Laura", "Vigilancia")
    granja.contratar_empleado(emp1)
    granja.contratar_empleado(emp2)

    # Registrar asistencia y tareas
    emp1.registrar_asistencia()
    emp1.realizar_tarea("Alimentar animales")
    emp1.reportar_incidencias("Gallina enferma")

    # Crear corrales
    corral1 = Corral(1)
    corral2 = Corral(2)
    granja.agregar_corral(corral1)
    granja.agregar_corral(corral2)

    # Crear animales
    vaca = Animal("Lola", "Vaca")
    cerdo = Animal("Porky", "Cerdo")
    gallina = Animal("Pepita", "Gallina")

    # Asignar animales a corrales
    corral1.asignar_animal(vaca)
    corral1.asignar_animal(cerdo)
    corral2.asignar_animal(gallina)

    # Acciones sobre animales
    vaca.alimentar()
    vaca.vacunar()
    vaca.registrar_peso(250)

    # Limpiar corrales
    corral1.limpiar()

    # Mostrar animales
    corral1.listar_animales()
    corral2.listar_animales()

    # Cierre de la granja
    granja.cerrar()
