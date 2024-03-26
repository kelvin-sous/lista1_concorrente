def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n-1)

num = int(input("Informe um valor:")) # Exemplo de número para calcular o fatorial

# Verifica se o número é negativo
if num < 0:
    print("Desculpe, o fatorial não existe para números negativos")
elif num == 0:
    print("O fatorial de 0 é 1")
else:
    print("O fatorial de", num, "é", recur_factorial(num))
