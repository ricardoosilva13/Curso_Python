#Um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a=float(input('Digite o angulo: '))
seno=math.sin(math.radians(a))
print('O angulo de {} tem o seno de {}'.format(a,seno))
cosseno=math.cos(math.radians(a))
print('O angulo de {} tem o cosseno de {}'.format(a,cosseno))
tangente=math.tan(math.radians(a))
print('O angulo de {} tem a tangente de {}'.format(a,tangente))