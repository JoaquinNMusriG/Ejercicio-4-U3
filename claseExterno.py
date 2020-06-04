from claseEmpleado import Empleado

class Externo(Empleado):
    __Tarea = ''
    __FechaI = None
    __FechaF = None
    __MontoViatico = 0.0
    __CostoObra = 0.0
    __MontoSeguro = 0.0

    def __init__ (self,dni,nombre,direccion,telefono,tarea,fechaI,fechaF,montoV,costoO,montoS):
        super().__init__(dni,nombre,direccion,telefono)
        self.__Tarea = tarea
        self.__FechaI = fechaI
        self.__FechaF = fechaF
        self.__MontoViatico = montoV
        self.__CostoObra = costoO
        self.__MontoSeguro = montoS

    def __str__(self):
        print(super().__str__())
        return 'Tarea = {} Fecha Inicio = {} Fecha Fin = {} Monto Viatico = {} Costo Obra = {} Monto Seguro = {}'.format(self.__Tarea,self.__FechaI,self.__FechaF,self.__MontoViatico,self.__CostoObra,self.__MontoSeguro)

    def getTarea(self):
        return self.__Tarea.lower()

    def getFechaFin (self):
        return self.__FechaF

    def getCosto (self):
        return self.__CostoObra

    def getSueldo(self):
        return self.__CostoObra - self.__MontoViatico - self.__MontoSeguro
