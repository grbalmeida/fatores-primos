from fatores_primos import proximo_numero_primo

def test_proximo_numero_primo():
    assert proximo_numero_primo(2, 5) == 5
    assert proximo_numero_primo(3, 10) == 5
    assert proximo_numero_primo(2, 9) == 3