from animal import Animal

print("".center(50, '*'))
print("CABEÇALHO".center(50, ' '))
print("".center(50, '*'))

animal1 = Animal(
    input("Digite a especie: "),
    input("Digite a raca: "),
    input("Digite a cor: "),
    input("Digite o porte: ")
)

print("".center(50, '*'))
print(f"{animal1.GetEspecie()} - {animal1.GetRaca()} - {animal1.GetPorte()} - {animal1.GetCor()}".center(50, ' '))
print("".center(50, '*'))

print("".center(50, '*'))
print(f'{animal1}'.center(50, ' '))
print("".center(50, '*'))

animal2 = Animal(
    input("Digite a especie: "),
    input("Digite a raca: "),
    input("Digite a cor: "),
    input("Digite o porte: ")
)

print("".center(50, '*'))
print(f"{animal2.GetEspecie()} - {animal2.GetRaca()} - {animal2.GetPorte()} - {animal2.GetCor()}".center(50, ' '))
print("".center(50, '*'))

print("".center(50, '*'))
print(f'{animal2}'.center(50, ' '))
print("".center(50, '*'))