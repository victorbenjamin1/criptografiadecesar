
caracteres = 'abcdefghijklmnopqrstuvwxyz'
tamanho = len(caracteres)


def criptografando(texto_puro, casas):
    for c in texto_puro:
        if c in caracteres:
            n = caracteres.find(c)
            if n >= tamanho:
                n = n - tamanho
            elif n < 0:
                n = n + tamanho
            n = n+casas
            texto_cifrado = texto_cifrado + caracteres[n]
        else:
            texto_cifrado = texto_cifrado + c
    return texto_cifrado

