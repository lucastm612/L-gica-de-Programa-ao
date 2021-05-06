n = int(input('Digite a quantidade de nomes para armazenar: '))

while n < 4 or n > 9:
    n = int(input('Digite a quantidade de nomes para armazenar: '))

L = []

for x in range (1, n+1):
    nome = str(input('Digite o nome: '))
    L.append(nome)

L.insert(3, 'Teste')
print(L)

del L[2]
print(L)

if L.count('Ana') == 0:
    print('Nome Ana não apareceu na lista.')
else:
    print('O nome Ana apareceu',L.count('Ana'),'vez(es) na lista. Primeira ocorrência - índice:',L.index('Ana'))

L.sort()
print(L)
