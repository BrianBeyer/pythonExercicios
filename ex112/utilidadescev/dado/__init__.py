def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '': # se é alfanumerica
            print(f'\033[0;31mERRO: {entrada} é um valor invalido...\033[m ')
        else:
            valido = True
            return float(entrada)
