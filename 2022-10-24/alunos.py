def calcMedia(*notas):
    media = sum(notas)/len(notas)
    situacao = "Aprovado" if media >= 7 else "Reporvado"
    return media, situacao

nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media, situacao = calcMedia(nota1, nota2, nota3)

print(f"Aluno {nome}:")
print(f"{nota1} + {nota2} + {nota3} =  {media}")
print(situacao)