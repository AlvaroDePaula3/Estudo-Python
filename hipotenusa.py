from math import hypot
catetoOposto = float(input("Digite o cateto oposto: "))
catetoAdjacente = float(input("Digite o cateto adjacente: "))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print("{:.2f}".format(hipotenusa))

#Ambos fazem a mesma coisa, porém o debaixo faz o cálculo puro, o de cima utiliza a biblioteca mesmo
co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("{:.2f}".format(hi))