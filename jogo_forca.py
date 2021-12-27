from random import randint

#define o nome do arquivo que possui as palavras a serem descobertas, no meu caso o arquivo é 'palavras.txt'
arquivo = open('palavras.txt', 'r')
#le a primeira linha do arquivo
linha = arquivo.readline()
arquivo.close()

#transforma as palavras desta linha para uma lista utilizando o espaco
listaPalavras = linha.split()
arquivo.close()

#descobriu o total de palavras
totalPalavras = len(listaPalavras)

sorteio = randint(0,totalPalavras-1)

palavra = listaPalavras[sorteio]

#numero de tentativas vai depender das regras de cada usuario, no meu caso sera 5
tentativasRestantes = 5
letrasTentadas = []

print("=== JOGO DA FORCA ===")

#cria a mascara de exibicao da quantidade de letras referente a palavra escolhida
qtdeAsterisco = len(palavra)
mascara = list(qtdeAsterisco * '*')

while (tentativasRestantes != 0 and qtdeAsterisco != 0):
    print(f"\nTentativas restantes: {tentativasRestantes}")
    print(f"Letras tentadas: {' '.join(letrasTentadas)}")
    print(f"\nPalavra a ser descoberta: {' '.join(mascara)} \n")
#usamos o .lower() para converter a letra para minusculo caso o usuario digite uma letra maiuscula, já que nosso programa so reconhece letras minusculas
    letra = input("Digite uma letra: ").lower()
    acertou = False
    letrasTentadas.append(letra)
    for l in range(len(palavra)):
        if palavra[l] == letra:
            mascara[l] = palavra[l]
            acertou = True

    if (acertou == False):
        tentativasRestantes -= 1

    qtdeAsterisco = mascara.count("*")

if(qtdeAsterisco == 0):
    print("Parabéns você descobriu a palavra!!!")
    print(f"A palavra é {palavra}")

else:
    print("Infelizmente você perdeu!!!")