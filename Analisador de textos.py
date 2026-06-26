nome_completo = input("Digite seu nome completo: ").strip()

maiusculo = nome_completo.upper()
print("O nome com tudo maiúsculo é {}".format(maiusculo))

minusculo = nome_completo.lower()
print("O nome com tudo minúsculo é {}".format(minusculo))

letras_total = len(nome_completo) - nome_completo.count(" ")
print("O número de letras que esse nome possui é: {}".format(letras_total))

letras_nome1 = nome_completo.split()
print("O seu primeiro nome é: {}".format(letras_nome1[0]))