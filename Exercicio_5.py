# Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do novo salário reajustado de
# acordo com a tabela abaixo:
# Salário atual     	      Reajuste
# Abaixo de R$500,00    	    15%
# de R$500,00 até R$1000,00	    10%
# Acima de R$1000,00	         5%

print("\t ---- Conversor de Salário ----")

salario = float(input("Digite o salário atual: "))

if 0< salario <500:
    salario = salario * 1.15
    print("O valor do salário reajustado é de R${}".format(salario))

elif 500 <= salario < 1000:
    salario = salario * 1.1
    print("O valor do salário reajustado é de R${}".format(salario))

elif salario >=1000:
    salario = salario * 1.05
    print("O valor do salário reajustado é de R${}".format(salario))
else:
    print("Entrada invalida")

