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