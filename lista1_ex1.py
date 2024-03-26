import numpy as np

def ordenar_vetor(vetor):
    array = np.array(vetor)
    array_ordenado = np.sort(array)
    return array_ordenado.tolist()

vetor_entrada = [5, 3, 1, 4, 2]
vetor_ordenado = ordenar_vetor(vetor_entrada)
print(vetor_ordenado)