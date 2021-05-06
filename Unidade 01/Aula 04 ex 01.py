a=int(input("Digitem um número inteiro: "))
b=int(input("Digite outro número inteiro: "))
c=int(input("Digite o último número inteiro: "))

if a<c and a<b:
    print("O número {} é o menor de todos.".format(a))
elif b<c:
    print("O número {} é o menor de todos.".format(b))
else:
    print("O número {} é o menor de todos.".format(c))
