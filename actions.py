caracteres = 'abcdefghijklmnopqrstuvwxyz'
tamanho = len(caracteres)


def criptografando(texto_puro, casas=0):
    texto_puro = texto_puro.lower()
    texto_crifrado = ""
    for c in texto_puro:
        if c in caracteres:
            n = caracteres.find(c)
            n = n + casas
            if n >= tamanho:
                n = n - tamanho
            elif n < 0:
                n = n + tamanho
            texto_crifrado = texto_crifrado + caracteres[n]
        else:
            texto_crifrado = texto_crifrado + c
    return texto_crifrado


def descriptografando(texto_cifrado, casas=0):
    texto_cifrado = texto_cifrado.lower()
    texto_decifrado = ''
    for c in texto_cifrado:
        if c in caracteres:
            n = caracteres.find(c)
            n = n - casas
            texto_decifrado = texto_decifrado + caracteres[n]
        else:
            texto_decifrado = texto_decifrado + c
    return texto_decifrado
