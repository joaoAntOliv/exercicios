# exercicios
#Faça um programa que leia uma lista de números e retorne uma nova lista contendo apenas os números que aparecem mais de uma vez na lista original.
# lê a lista de números
numeros = input("Digite uma lista de números separados por espaço: ").split()

# converte cada elemento da lista para int
numeros = [int(num) for num in numeros]

# cria uma nova lista para armazenar os números repetidos
numeros_repetidos = []

# itera sobre a lista de números e verifica se cada número aparece mais de uma vez
for num in numeros:
    if numeros.count(num) > 1 and num not in numeros_repetidos:
        numeros_repetidos.append(num)

# imprime a lista de números repetidos
print("Números repetidos:", numeros_repetidos)
