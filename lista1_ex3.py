from collections import Counter

def contar_palavras(texto):
    # Dividir o texto em palavras e converter para minúsculas
    palavras = texto.lower().split()
    # Contar as ocorrências de cada palavra
    contagem = Counter(palavras)
    return contagem

# Exemplo de uso
texto = (input("Entre com o texto:"))
contagem_palavras = contar_palavras(texto)

# Imprimir a contagem de cada palavra
for palavra, contagem in contagem_palavras.items():
    print(f"{palavra}: {contagem}")
