#
# Faça um programa em que o usuário informe o salário recebido e o total gasto com despesas. Deverá ser exibido na tela
# “Gastos dentro do orçamento” caso o valor gasto não ultrapasse o valor do salário e “Orçamento estourado” se o valor
# gasto ultrapassar o valor do salário.

print("\t ---- Satatus do orçamento ---- ")

salario = float(input("Digite o valor do salário recebido: R$"))
despesa = float(input("Digite o valor gastos com as despesas: R$"))

if despesa < salario:
    print("Gastos dentro do orçamento")

elif despesa == salario:
    print("Gasto = Salário !")

else:
    print("Orçamento Estourado!")
