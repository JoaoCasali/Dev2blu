from animal import Animal
def main():
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
    print(f"{animal1.especie} - {animal1.raca} - {animal1.porte} - {animal1.cor}".center(50, ' '))
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
    print(f"{animal2.especie} - {animal2.raca} - {animal2.porte} - {animal2.cor}".center(50, ' '))
    print("".center(50, '*'))

    print("".center(50, '*'))
    print(f'{animal2}'.center(50, ' '))
    print("".center(50, '*'))

main()