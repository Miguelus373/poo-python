from empleado import Empleado
from desarrollador import Desarrollador
from diseñador import Diseñador
from gerente import Gerente

empleados = [Desarrollador(), Diseñador(), Gerente()]

print("======Empleados======")
Empleado().mostrar_trabajar(empleados)
