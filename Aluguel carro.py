AluguelDias = int(input("Quantos dias você ficou com o carro ? "))
KmRodados = float(input("Qual é a quantidade de quilômetros rodados? "))

valorAlguel = (AluguelDias*60)+(KmRodados*0.15)

print("O valor do alguel no total é: {:.2f}".format(valorAlguel))