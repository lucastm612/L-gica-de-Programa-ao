compra = float(input("Digite o valor da compra: "))
valor1 = compra*1.45
valor2 = compra*1.30
if compra<20.00:
    print("Essse deve ser o valor da venda:",valor1)
else:
    print("Essse deve ser o valor da venda:",valor2)
