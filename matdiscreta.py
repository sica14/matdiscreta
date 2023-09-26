def calculo_somatorio():
    soma = 0
    lista = []

    for n in range(1, 10):
        resultado = 2 * n + 1
        lista.append(resultado)
        soma += resultado

    print("Lista:", lista)
    print("Soma:", soma)

calculo_somatorio()