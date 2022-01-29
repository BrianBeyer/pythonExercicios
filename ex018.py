import math

n = float(input('Digite o valor do angulo: '))
# o  valor precisa ser convertido em radiano
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))

print('O valor do seno é {:.3f}, o valor cosseno é {:.3f} e o valor da tangente é {:.3f}' .format(sen,cos,tan))