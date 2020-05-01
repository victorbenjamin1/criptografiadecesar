from actions import *

texto_puro = 'eu te amo JESSICA, testando o x da xuxa'
casas = 1
# tipo = 0

print("----------------- CRIPTOGRAFIA DE JULIO CESAR -----------------\n")
tipo = input("O que você quer fazer? Digite [0] para CRIPTOGRAFAR ou [1] para DESCRIPTOGRAFAR: ")

if tipo == '0':
    mensagem = input("OK, vamos criptografar! Digite a mensagem: ")
    casas = int(input("Quantas casas nós vamos usar para criptografar essa mensagem? "))
    texto_cifrado = criptografando(mensagem, casas)
    print("Aqui está seu texto criptografado: ", texto_cifrado)

elif tipo == '1':
    mensagem = input("OK, vamos decifrar! Digite a mensagem: ")
    casas = int(input("Com quantas casas a mensagem foi criptografada? "))
    texto_decifrado = descriptografando(mensagem, casas)
    print("Essa é a sua mensagem: ", texto_decifrado)
else:
    print("Essa opção não é válida. Tchau!")



