tecla = 's'
while (tecla == 's' or tecla == 'S'):
    i = 0
    tabuada = int(input("Digite um valor:"))
    while i <= 10:
        print(tabuada,'x',i,'=',tabuada*i)
        i = i + 1
    tecla = input("Deseja calcular uma nova tabuada? [s/n]")
    while (tecla != 'N' and tecla != 'S' and tecla != 'n' and tecla != 's'):
        tecla = input("Comando inválido, digite s ou n!")
else:
    print("Obrigado por usar o programa! :)")