import math

co = float(input('Digite o comprimento do cateto oposto do triangulo:'))
ca = float(input('Digite o comprimento do cateto adjacente do triangulo: '))
h = math.sqrt(co**2 + ca**2)
#h = math.hypot(co,ca) tambem calcula a hipotennusa
print('O comprimento da hipotenusa é {:.2f}' .format(h))