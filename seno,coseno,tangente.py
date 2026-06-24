import math
angulo = float(input("Digite um angulo qualquer: "))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O seno do ângulo {}, tem o valor de: {:.2f}".format(angulo, seno))
print("O coseno do ângulo {}, tem o valor de: {:.2f}".format(angulo, coseno))
print("A tangente do ângulo {}, tem o valor de: {:.2f}".format(angulo, tangente))