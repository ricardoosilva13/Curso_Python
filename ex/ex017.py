#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
c1=float(input('Digite o compriento do cateto : '))
c2=float(input('Digite o compriento do cateto oposto : '))
h1=math.hypot(c1,c2)
print('A hipotenusa do triangulo é {}'.format(h1))