# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
# pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
d=float(input('Quantos dias alugou o carro: '))
k=float(input('Quantos Km rodou com o carro: '))
pap=60*d
pap2=0.15*k
papf=pap+pap2
print(' No total fica {:.2f}£'.format(papf))