from time import sleep

def contador(inicio, fim, passo):

    if inicio < fim:

        for i in range(inicio, fim+1, passo):
            print(f'{i}-', end='', flush= True)
            sleep(0.3)

    else:

        for i in range(inicio, fim-1, -passo):
            print(f'{i}-', end='', flush= True)
            sleep(0.3)

    print()

contador(
    int(input("Digite o inicio do contador: ")),
    int(input("Digite o fim do contador: ")),
    int(input("Digite o passo: "))
)