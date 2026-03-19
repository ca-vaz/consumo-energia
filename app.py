# Programa de cálculo do consumo de energia
# Autor: Carolina Vaz

#Entrada
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Insira a potência do aparelho, em Watts: "))
tempo_horas = float(input("Insira o tempo de uso, em horas, do aparelho: "))

#Processamento
consumo_mensal = (potencia * tempo_horas * 30) / 1000
valor_consumo_mensal = (consumo_mensal * 0.75)

#Saída
print(f'Aparelho: {aparelho}')
print(f'Consumo estimado: {consumo_mensal}kWh')
print(f'Valor estimado da conta: R${valor_consumo_mensal:.2f}')
