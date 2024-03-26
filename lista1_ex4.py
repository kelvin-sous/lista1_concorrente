import numpy as np

def transpor_matriz(matriz):
    return np.transpose(matriz)

# Exemplo de uso

a= input("Entre com um valor A\n")
b= input("Entre com um valor B\n")
c= input("Entre com um valor C\n")
d= input("Entre com um valor D\n")
e= input("Entre com um valor E\n")
f= input("Entre com um valor F\n")

matriz_original = np.array([[a,b,c], [d,e,f]])
matriz_transposta = transpor_matriz(matriz_original)

print("Matriz Original:")
print(matriz_original)

print("\nMatriz Transposta:")
print(matriz_transposta)
