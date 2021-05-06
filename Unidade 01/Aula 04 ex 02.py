num1=int(input("Digite um número inteiro: "))
num2=int(input("Digite outro número inteiro: "))
num3=int(input("Digite um último número inteiro: "))

if num1<num2 and num2<num3:
    a=num1
    b=num2
    c=num3
elif num1<num2 and num3<num2:
    a=num1
    b=num3
    c=num2
elif num2<num1 and num1<num3:
    a=num2
    b=num1
    c=num3
elif num2<num3 and num3<num1:
    a=num2
    b=num3
    c=num1
elif num3<num1 and num1<num2:
    a=num3
    b=num1
    c=num2
else:
    a=num3
    b=num2
    c=num1
print("A ordem crescente dos valores é {}, {} e {}".format(a,b,c))
