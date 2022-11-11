from conta import Conta, transferir

print("".center(50, '*'))
print("CABEÇALHO".center(50, ' '))
print("".center(50, '*'))

conta1 = Conta(
    input("Digite o número da conta: "),
    input("Digite o nome do titular: "),
    float(input("Digite seu saldo: ")),
    float(input("Digite seu limite: "))
)

print("Primeiro extrato da Conta1".center(50, '*'))
print(conta1.gerarExtrato().center(50, ' '))
print("".center(50, '*'))

conta1.depositar(
    float(input("Digite o valor para ser depositado: "))
)

print("Segundo extrato da conta1".center(50, '*'))
print(conta1.gerarExtrato().center(50, ' '))
print("".center(50, '*'))

conta1.sacar(
    float(input("Digite o valor para ser sacado: "))
)

print("Terceiro extrato da conta1".center(50, '*'))
print(conta1.gerarExtrato().center(50, ' '))
print("".center(50, '*'))

conta2 = Conta(
    '478914',
    "Dono do banco",
    1000000,
    5000
)

print("Primeiro extrato da Conta2".center(50, '*'))
print(conta2.gerarExtrato().center(50, ' '))
print("".center(50, '*'))

conta2.transferir(
    float(input("Digite o valor para ser transferido da conta2 para a conta 1: ")),
    conta1
)

print("Ultimo extrato da conta1".center(50, '*'))
print(conta1.gerarExtrato().center(50, ' '))
print("".center(50, '*'))

print()
print("".center(50, '*'))
print()

print("Ultimo extrato da Conta2".center(50, '*'))
print(conta2.gerarExtrato().center(50, ' '))
print("".center(50, '*'))