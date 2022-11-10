from conta import Conta

print("".center(50, '*'))
print("CABEÇALHO".center(50, ' '))
print("".center(50, '*'))

conta1 = Conta(
    input("Digite o número da conta: "),
    input("Digite o nome do titular: "),
    float(input("Digite seu saldo: ")),
    float(input("Digite seu limite: "))
)

print("".center(50, '*'))
print(f"{conta1.GetTitular()} - {conta1.GetNumero()} - {conta1.GetSaldo()}".center(50, ' '))
print("".center(50, '*'))

print("".center(50, '*'))
print(f'{conta1}'.center(50, ' '))
print("".center(50, '*'))

conta2 = Conta(
    input("Digite o número da conta: "),
    input("Digite o nome do titular: "),
    float(input("Digite seu saldo: ")),
    float(input("Digite seu limite: "))
)

print("".center(50, '*'))
print(f"{conta2.GetTitular()} - {conta2.GetNumero()} - {conta2.GetSaldo()}".center(50, ' '))
print("".center(50, '*'))

print("".center(50, '*'))
print(f'{conta2}'.center(50, ' '))
print("".center(50, '*'))