print("Digite 3 valores para a equação a*x²+b*x+c")
a=float(input("Digite o valor de a: "))
b=float(input("Digite o valor de b: "))
c=float(input("Digite o valor de c: "))
d=(b*b)-(4*a*c)

if a==0:
    print("Não é equação de 2o grau!")
elif d<0:
    d=(b*b)-(4*a*c)
    print("Não existem raízes reais!")
else:
    x1=((-b)+(d**(1/2)))/(2*a)
    x2=((-b)-(d**(1/2)))/(2*a)
    print("As raízes são {:.2f} e {:.2f}.".format(x1,x2))
