quantidade = int(input("Digite quantas maças comprou:"))
valor1 = quantidade*1.30
valor2 = quantidade*1.00
if quantidade<12:
    print("Você gastou:",valor1)
else:
    print("Você gastou:",valor2)
