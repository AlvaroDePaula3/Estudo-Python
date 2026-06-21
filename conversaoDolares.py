carteira = float(input('Digite qual é o valor que você possui na sua carteira: R$'))

conversaoDolares = carteira/3.27
print("Você pode comprar US${:.2f} dólares".format(conversaoDolares))