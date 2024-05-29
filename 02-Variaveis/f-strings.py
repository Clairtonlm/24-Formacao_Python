# Formataçãop de Variaveis
nome = 'ClairtonLima'
altura = 1.80
peso = 95
imc = (peso / (altura * altura))

formatar_variavel = f'Olá, {nome}! voce tem uma altura de {altura:.2f}m e peso de {peso} assim seu IMC é {imc:.2f}'

print(formatar_variavel)