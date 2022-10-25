def mediaIdade():
    soma = 0
    for i in pessoas:
        soma += i['idade']

    return soma/len(pessoas)

def contarM():
    soma = 0
    for i in pessoas:
        if i['sexo'] == False:

            soma += 1

    return soma

def listarMedia():
    lista1 = []
    for i in pessoas:
        if i['idade'] > mediaIdade():
            lista1.append(i["nome"])
    
    print(lista1)

pessoas = []

for i in range(3):
    nome = input("Digite seu nome: ")
    sexo = bool(int(input("Digite seu genero (0 = F ou 1 = M): ")))
    idade = int(input("Digite sua idade: "))
    print()
    pessoas.append(
        {
            'nome': nome,
            'sexo': sexo,
            'idade': idade
        }
    )

print(pessoas[0]['sexo'])
print(f"Total de pessoas cadastradas: {len(pessoas)}")
print(f"Media das idades das pessoas cadastradas: {mediaIdade()}")
print(f"Quantidade de mulheres cadastradas: {contarM()}")
listarMedia()