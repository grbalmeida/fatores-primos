from unicode_table import unicode_table

def fatores_primos(numero):
    fatores = []
    fator_primo_inicial = 2

    while numero != 1:
        if numero % fator_primo_inicial == 0:
            fatores.append(fator_primo_inicial)
            numero = numero // fator_primo_inicial
        else:
            fator_primo_inicial = proximo_numero_primo(fator_primo_inicial, numero)
            fatores.append(fator_primo_inicial)
            numero = numero // fator_primo_inicial

    return fatores

def fatores_primos_multiplicacao(numero):
    fatores = fatores_primos(numero)
    fatores_str = [str(x) for x in fatores]

    return f'{numero} = {" * ".join(fatores_str)}'

def fatores_primos_exponenciacao(numero):
    aparicoes = {}
    fatores = fatores_primos(numero)
    aparicoes_exponencial = []

    for n in fatores:
        if not aparicoes.get(n):
            aparicoes[n] = 1
        else:
            aparicoes[n] += 1

    for k, v in aparicoes.items():
        if v > 1:
            aparicoes_exponencial.append(f'{k}{obter_numero_unicode(v)}')
        else:
            aparicoes_exponencial.append(f'{k}')

    return f'{numero} = {" * ".join(aparicoes_exponencial)}'


def proximo_numero_primo(numero_primo_atual, numero_atual):
    numero_primo_atual += 1

    for n in range(numero_primo_atual, numero_atual + 1):
        if e_primo(numero_primo_atual) and numero_atual % n == 0:
            return n

        numero_primo_atual += 1

    return numero_primo_atual

def e_primo(numero):
    numero_divisores = 0

    for n in range(1, numero + 1):
        if numero % n == 0:
            numero_divisores += 1

    return numero_divisores <= 2

def obter_numero_unicode(numero):
    numero_str = str(numero)

    return_str = ''

    for n in numero_str:
        return_str += unicode_table[n]

    return return_str