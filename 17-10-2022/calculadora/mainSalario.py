from controller import *
wages = []
customizedPrint('== CALCULADORA DE SALÁRIOS ==')
for i in range(1, 5):
    wages.append(float(input(f"Digite o seu {i}º salário: ")))

customizedPrint(f"== {GREEN}RESULTADO{CLEANCOLOR} ==", True)
tablePrint(f'{wages[0]:.2F} + {wages[1]:.2F} + {wages[2]:.2F} + {wages[3]:.2F}')
tablePrint(f'Total: {wagesSum(wages):.2F}')
customizedPrint()