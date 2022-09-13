constante = 8
poli = "="*8
print(f'{poli} INICIO LAÇO {poli}')

listaNumeros = []
soma = 0
for i in range(3):
    numero = int(input(f"Digite o {i+1}º número: "))
    soma += numero
    listaNumeros.append(numero)

print("{} + {} + {} = {}".format(listaNumeros[0], listaNumeros[1], listaNumeros[2], soma))
print(f'{poli} FIM LAÇO {poli}')

print(f'{poli} INICIO CONDIÇÃO {poli}')
if soma > 10:
    print("A soma é maior que 10")
elif soma == 10:
    print("A soma é igual a 10")
else: 
    print("A soma é menor que 10")
    
print(f'{poli} FIM CONDIÇÃO {poli}')