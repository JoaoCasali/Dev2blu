from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

pessoa_fisica = PessoaFisica("1232", "João", "98745238901", 1200)

print("-- Pessoa Fisica --".center(50, "="))
print(f"{pessoa_fisica}")
print()

pessoa_fisica.segundo_titular = "Ana"
print("-- Pessoa Fisica com auterações--".center(50, "="))
print(f"{pessoa_fisica}")
print()

pessoa_juridica = PessoaJuridica("2321", "Megasul", "12876590865412", 1200)

print("-- Pessoa Juridica --".center(50, "="))
print(f"{pessoa_juridica}")
print()

pessoa_juridica.segundo_titular = "Cooper"
print("-- Pessoa Juridica com auterações--".center(50, "="))
print(f"{pessoa_juridica}")