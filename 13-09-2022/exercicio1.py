numero = int(input("Digite um número: "))
calculo = numero % 2

print("{} % por 2 = {}".format(numero, calculo))
if calculo == 0:
    print("O número é par")
else:
    print("O número é impar")
