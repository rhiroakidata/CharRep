entrada = input("Digite a string: \n")

def maiorValor(dicionario):
    '''
    dicionario: dicionario tendo as chaves como os caracteres diferentes um do outro e
    valores como suas respectivas quantidades.

    returns: A chave com o maior valor
    '''
    maior = 0
    chave_maior = None
    for chave, valor in dicionario.items():
        if valor > maior:
            maior = valor
            chave_maior = chave

    return chave_maior

# Elimina repetição na string, ajudando nessa lista a ter só caracteres diferentes um do outro
listaChar = list(set(entrada))

# Lista que vai conter a quantidade do respectivo caracter
qtdChar = []

# Vai percorrer em cada caracter da listaChar e verificar quantos tem dele na string de entrada
for letra in range(0, len(listaChar)):
    count = 0
    for i in range(0, len(entrada)):
        if listaChar[letra] == entrada[i]:
            count += 1
    qtdChar.append(count)

# Forma dicionário ao juntar as listas listaChar e qtdChar
dicionario = dict(zip(listaChar,qtdChar))

# Verifica qual o caracter mais frequente na string de entrada passando como parâmetro o dicionário formado
letraMaisFreq = maiorValor(dicionario)

# Verifica qual é o primeiro índice do caracter mais frequente
for i in range(0,len(entrada)):
    if letraMaisFreq == entrada[i]:
        indice = i
        break

# Saída
print('A letra mais frequente é: ',letraMaisFreq)
print("O primeiro índice de '%s' é: %s" % (letraMaisFreq, indice))