
caracteres = 'abcdefghijklmnopqrstuvwxyz'
tamanho = len(caracteres)


def descriptografando(texto_cifrado, casas):
    for c in texto_cifrado:  # Decifrando o código
        if c in caracteres:
            n = caracteres.find(c)
            if n >= tamanho:
                n = n - tamanho
            elif n < 0:
                n = n + tamanho
            n = n-casas
            texto_decifrado = texto_decifrado + caracteres[n]
        else:
            texto_decifrado = texto_decifrado + c
    return texto_decifrado
