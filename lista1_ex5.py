# Solicita ao usuário que insira uma lista de números inteiros
numeros = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))

# Inicializa contadores para positivos, negativos e zeros
positivos = 0
negativos = 0
zeros = 0

# Percorre a lista de números
for numero in numeros:
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1

# Imprime a contagem de números positivos, negativos e zeros
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Zeros: {zeros}")
