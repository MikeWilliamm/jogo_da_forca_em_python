from time import sleep
from random import randint

print('-'*42)
print('FORCA'.center(42))
print('-'*42)
#Sorteio da palavra
lista_palavras = ['teclado', 'mouse', 'computador', 'software', 'moto', 'carro', 'casa', 'janela', 'porta']
num = randint(0,len(lista_palavras))
palavra = lista_palavras[num]
#Criando campos
campos = list("_"*len(palavra))
#contar as letras acertar
conta_acertos = 0
lista_acertos = []
#verificador para finalizar o jogo
finalizar_jogo = False

while True:
    #printa estádo dos campos
    print(f'Letras já digitas: {lista_acertos}\n'.replace("'",""))
    print('Palavra: ', end='')
    for i in campos:
        print(i, end=' ')
    
    #entrada do usuario
    char = str(input('\nDigite a letra: ')).strip()[0]
    index = 0
    acertou = 0
    #verifica se a letra existe na palavra
    for letra in palavra:
        if char == letra:
            campos[index] = str(char)
            acertou = 1
            conta_acertos+=1
        index+=1
        #verifica se acertou a letra ou não
        
    if acertou == 1:
        if char not in lista_acertos:
            print('Você acertou!\n')
            lista_acertos.append(char)
        else:print('Letra já escolhida anteriormente!\n')
        
    else: 
        print('Você errou!\n')
        lista_acertos.append(char)
        #Verifica se falta apenas 2 caracters para acertar a palavra
        
    if conta_acertos >= len(palavra)-2:
        while True:
            print(f'Letras já digitas: {lista_acertos}\n'.replace("'",""))
            print('Palavra: ', end='')
            for i in campos:
                print(i, end=' ')
            print()

            for c in range(5,0, -1):
                print(f'{c} segundos para a resposta...')
                sleep(0.5)

            resp = str(input('\nDigite a palavra: '))
            if resp == palavra:
                print('Você venceu o jogo!!! :D\n')
                finalizar_jogo = True
                break
            else: 
                print('Você errou!!! :(\n')
                sleep(0.5)
                    
        if finalizar_jogo == True:
            sleep(5)
            break
    if finalizar_jogo == True:
            sleep(5)
            break