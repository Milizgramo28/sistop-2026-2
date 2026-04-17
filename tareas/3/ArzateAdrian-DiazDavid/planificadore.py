import random 
from collections import deque 
import copy
from dataclasses import dataclass

@dataclass
class Proceso:
    nombre: str
    tiempo_llegada: int
    tiempo_servicio: int 

    tiempo_restante: int = 0
    tiempo_retorno: int = 0
    tiempo_espera: int = 0

    def __post_init__(self):
        if self.tiempo_restante == 0:
            self.tiempo_restante = self.tiempo_servicio

def proceso_aleatorio(num_procesos):
    procesos = []
    for i in range(num_procesos):
        nombre = chr(65 + i)

        tiempo_llegada = random.randint(0,10)
        tiempo_servicio = random.randint(1,5)
        procesos.append(Proceso(nombre, tiempo_llegada, tiempo_servicio))
    procesos.sort(key=lambda p: p.tiempo_llegada)
    return procesos

print(proceso_aleatorio(5))