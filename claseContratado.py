from claseEmpleado import Empleado

class Contratado(Empleado):
    ValorHora = 250

    __FechaInicio = None
    __FechaFin = None
    __CantHoras = 0

    @classmethod
    def getValorHora (cls):
        return cls.ValorHora

    def __init__(self,dni,nombre,direccion,telefono,fechaI,fechaF,cantH):
        super().__init__(dni,nombre,direccion,telefono)
        self.__FechaInicio = fechaI
        self.__FechaFin = fechaF
        self.__CantHoras = cantH

    def __str__(self):
        print(super().__str__())
        return 'Fecha Inicio = {} Fecha Fin = {} Cant Horas = {}'.format(self.__FechaInicio,self.__FechaFin,self.__CantHoras)

    def getSueldo(self):
        return Contratado.getValorHora()*self.__CantHoras

    def actualizarHora (self,h):
        self.__CantHoras += h
