from claseColeccion import Coleccion

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.registrarHora,
                            2:self.totalTarea,
                            3:self.ayudaEmpleados,
                            4:self.calcularSueldo,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op,empleados):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(empleados)
    def salir(self,empleados):
        print('Salir')

    def registrarHora(self,empleados):
        dni = input('Ingrese el dni del empleado CONTRATADO del cual quiere registrar hora: ')
        if dni.isdigit():
            empleados.registrarH(dni)
        else:
            print('Dni inválido.')

    def totalTarea(self,empleados):
        tarea = input('Ingrese la tarea de la que quiere saber el monto: ')
        if tarea.isalpha():
            empleados.montoTarea(tarea)
        else:
            print('Tarea inválida.')

    def ayudaEmpleados(self,empleados):
        empleados.Ayuda()

    def calcularSueldo(self,empleados):
        empleados.mostrarEmpleados()
