# Crie uma lista apenas com elementos numéricos
numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mista = [42, 3.14, "Python", True, None, [1, 2, 3], (4, 5), {"chave": "valor"}]
# Imprima na tela apenas os 5 primeiros elementos da lista
print(numeros_primos[:5])
print(mista[:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
print(numeros_primos[::2])
print(numeros_primos)
# Remova da lista o último item
mista.pop()
mista.pop(2)
print(mista)
# Insira na lista um novo item
mista.append("chave_nova")
print(mista)
# Remova da lista um item específico
mista.remove(True)
print(mista)