def num_par():#funcao para solicitar ao usuario um numero para verificacao dos numeros impares ou pares
    while True:#cria um loop infinito com todos os numeros inseridos pelo usuario
        try:#linha de codigo que permite definirmos exceçoes, neste caso a exceçao e para converter as entradas de dados do usuario de caracteres para numeros
            val = int(input("Digite um numero para verificararmos é par ou impar: "))#nesta linha estamos salvando a entrada de dados do usuario dentro da varivel val e ao mesmo tempo forcando com o try com que as entradas de dados do usuario sejam inteiras, ou seja sem caracteres
            return val#se o valor inserido pelo usuario for confirmado como um valor inteiro essa linha retorna o valor a variavel assim dando continuidade a proxima funcao
        except ValueError:#se o usuario inserir algo que nao possa ser convertido em valores inteiros esta linha de codigo entra em acao mostrando a mensagem a baixo na tela do usuario
            print("Por favor digite um numero inteiro")#esta linha de codigo mostra ao usuario que o valor inserido pelo mesmo nao pode ser convertido na variavel inteiro

def verifica_pariedade(): #criamos uma função para verificar se os nbumeros são pares ou impares
    Var = num_par() #estamos pedindo ao usuario para inserir um valor numerico para iniciarmos a comparação
    par = 0 #definimos que par é zero para que o valor que o usuario definir seja colocado no lugar do zero
    impar = 0  #definimos que impar é zero para que o valor que o usuario definir seja colocado no lugar do zero
    for aux in range(Var): #esta linha cria um loop dos numeros para que o codigo possa conta-lo
        if aux % 2 == 0: #estamos definindo que se o valor inserido pelo usuario se quando dividido por 2 o resto da divisão for 0 este numero sera par
            par = par + aux # estamos definindo que a variavel par é igual a par mais a variavel aux assim par recebera o resultado da divisão presente na variavel aux
            print(aux, "é par")#aqui estamos mostrando na tela do usuario que o numero inserido por ele é par, se todos os fatores acima forem validados
        else: #se os fatores acima nao forem validados entao os comandos a baixo serao executados
            impar = impar + aux #impar sera igual a impar mais aux recebendo entao os valores do resto da divisao acima
            print(aux, "é ímpar")#mostraremos na tela do usuario que o numero inserido por ele é impar

def geral():#aqui temos a funcao geral que rodara todas as outras funcoes
    verifica_pariedade()#uma função para verificar se os nbumeros são pares ou impares

geral()
