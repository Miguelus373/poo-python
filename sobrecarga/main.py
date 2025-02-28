from vector import Vector
from transformador import Transformador

norma2d = Vector().calcular_norma(4, 3)
norma3d = Vector().calcular_norma(4, 4, 2)

suma = Transformador().transformar(3, 5, 2, 6, 4, 7, 4)
lista = Transformador().transformar(3, 5, 2, 6, 4, 7, 4, factor = 3)

print("======Vectores======")
print(norma2d) # 5.0
print(norma3d) # 6.0

print("======Transformador======")
print(suma) # 31
print(lista) # [9, 15, 6, 18, 12, 21, 12]