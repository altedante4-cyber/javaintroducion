from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
    def __str__(self):
        return f"Nombre {self.__nombre} Apellido {self.__apellido}"
    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido(self):
        return self.__apellido
class Modulo:
    def __init__(self, nombre, horas_lectivas, es_optativo):
        self.__nombre = nombre
        self.__horas_lectivas = horas_lectivas
        self.__es_optativo = es_optativo
    def __str__(self):
        return f"Nombre {self.__nombre} Horas lectivas {self.__horas_lectivas} Es optativa {self.__es_optativo}"
    @property
    def nombre(self):
        return self.__nombre
class Ciclo:
    def __init__(self, nombre, tipo_grado, modulos):
        self.__nombre = nombre
        self.__tipo_grado = tipo_grado
        self.__modulos = modulos
    @property
    def nombre(self):
        return self.__nombre
    @property
    def modulos(self):
        return self.__modulos
    def __str__(self):
        return f"Ciclo: {self.__nombre}, Tipo: {self.__tipo_grado}"
class Grupo:
    def __init__(self, nombre, ciclo, curso_anio, tutor):
        self.__nombre = nombre
        self.__ciclo = ciclo
        self.__curso_anio = curso_anio
        self.__tutor = tutor
        self.__alumnos = []
        self.__modulos_profesores = {}
    @property
    def nombre(self):
        return self.__nombre
    @property
    def ciclo(self):
        return self.__ciclo
    def agregar_alumno(self, alumno):
        self.__alumnos.append(alumno)
    def eliminar_alumno(self, alumno):
        if alumno not in self.__alumnos:
            return
        self.__alumnos.remove(alumno)
    def asignar_profesor_modulo(self, modulo, profesor):
        self.__modulos_profesores[modulo] = profesor
    def mostrar_informacion(self):
        print(f"Grupo: {self.__nombre}")
        print(f"Ciclo: {self.__ciclo.nombre}")
        print(f"Curso: {self.__curso_anio}")
        print(f"Tutor: {self.__tutor}")
        print("Modulos impartidos:")
        for modulo, profesor in self.__modulos_profesores.items():
            print(f"  - {modulo.nombre}: {profesor.nombre} {profesor.apellido}")
        print(f"Alumnos ({len(self.__alumnos)}):")
        for alumno in self.__alumnos:
            print(f"  - {alumno.nombre} {alumno.apellido}")
class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, ciclo, grupo):
        super().__init__(nombre, apellido)
        self.__edad = edad
        self.__ciclo = ciclo
        self.__grupo = grupo
    @property
    def edad(self):
        return self.__edad
    @property
    def grupo(self):
        return self.__grupo
    def __str__(self):
        return f"{super().__str__()} Edad {self.__edad} Grupo {self.__grupo.nombre}"
class Profesor(Persona):
    def __init__(self, nombre, apellido, departamento):
        super().__init__(nombre, apellido)
        self.__departamento = departamento
    @property
    def departamento(self):
        return self.__departamento
    @departamento.setter
    def departamento(self, valor):
        if valor not in ["Informatica", "Empresa", "Ingles"]:
            self.__departamento = None
        else:
            self.__departamento = valor
    def __str__(self):
        return f"{super().__str__()} Departamento {self.__departamento}"
if __name__ == "__main__":
    modulo1 = Modulo("Programacion", 200, False)
    modulo2 = Modulo("Bases de Datos", 180, False)
    modulo3 = Modulo("Entornos", 100, False)
    ciclo1 = Ciclo("DAM", "Superior", [modulo1, modulo2, modulo3])
    profesor_tutor = Profesor("Ana", "Garcia", "Informatica")
    profesor1 = Profesor("Carlos", "Lopez", "Informatica")
    profesor2 = Profesor("Maria", "Martinez", "Empresa")
    grupo1 = Grupo("DAM1", ciclo1, "primero", profesor_tutor)
    grupo1.asignar_profesor_modulo(modulo1, profesor1)
    grupo1.asignar_profesor_modulo(modulo2, profesor2)
    alumno1 = Alumno("Juan", "Perez", 20, ciclo1, grupo1)
    alumno2 = Alumno("Maria", "Rodriguez", 17, ciclo1, grupo1)
    grupo1.agregar_alumno(alumno1)
    grupo1.agregar_alumno(alumno2)
    grupo1.mostrar_informacion()