def pontencia():
    base = int(input("Digite o valor da base: "))
    expoente = int(input("Digite o valor do expoente: "))

    cont = 0
    produto = 1
    while(cont<expoente):
        produto = produto*base
        cont = cont + 1
    print(base," elevado a",expoente," = ",produto)

pontencia()
