
salario1 = float(input("Digite seu primeiro salário: "))
salario2 = float(input("Digite seu segundo salário: "))
salario3 = float(input("Digite seu terceiro salário: "))
salario4 = float(input("Digite seu quarto salário: "))

salarioTotal = salario1 + salario2 + salario3 + salario4
print('='*8, 'Calculadora', '='*8)
print('Primeira variável: {}\nSegunda variável: {}\nTerceira variável: {}\nQuarta variável: {}\nSoma: {:.2f}'.format(salario1,salario2, salario3, salario4, salarioTotal))
