'''

'''

while True: 
    n1 = int(input('Digite um número: '))
    n2= int(input('Até onde a tabuada vai: '))
    for i in range(n2):
        i+=1
        print(f'{n1} x {i} = {n1 * i}')
    

    continuar = input('Quer geraar outra tabuada? \n[S]Sim\nQualquer outra tecla para não\n').strip().lower()

    if continuar == 's':
        continue
    else:
        print("Fechando calculadora...")
        break