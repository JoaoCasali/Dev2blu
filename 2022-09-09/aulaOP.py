idade = int(input("Digite sua idade: "))

# ------------------
print(" "*15, 'Expressão de igualdade', ' '*15)
validador = ( idade == 18 )
print(validador)
# ------------------
print(" "*15, 'Expressão de diferença', ' '*15)
validador = ( idade != 18 )
print(validador)
# ------------------
print(" "*15, 'Expressão de maior', ' '*15)
validador = ( idade > 18 )
print(validador)
# ------------------
print(" "*15, 'Expressão de menor', ' '*15)
validador = ( idade < 18 )
print(validador)
# ------------------
print(" "*15, 'Expressão de maior e igual', ' '*15)
validador = ( idade >= 18 )
print(validador)
# ------------------
print(" "*15, 'Expressão de menor e igual', ' '*15)
validador = ( idade <= 18 )
print(validador)