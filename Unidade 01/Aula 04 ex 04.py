print("Digite os lados de um triângulo:")
a=float(input("Lado 1: "))
b=float(input("Lado 2: "))
c=float(input("Lado 3: "))

if a<(b+c) and b<(a+c) and c<(a+b):
    if a==b and b==c:
        print("O triângulo é equilátero!")
    else:
        if a==b or a==c or b==c:
            print("O triângulo é isósceles!")
        else:
            print("O triângulo é escaleno!")
else:
    print("Não é um triângulo!")
