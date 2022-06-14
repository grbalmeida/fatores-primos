from fatores_primos import e_primo

def test_e_primo():
    assert e_primo(2) == True
    assert e_primo(3) == True
    assert e_primo(5) == True
    assert e_primo(7) == True
    assert e_primo(11) == True
    assert e_primo(13) == True
    assert e_primo(17) == True
    assert e_primo(19) == True

def test_nao_e_primo():
    assert e_primo(4) == False
    assert e_primo(6) == False
    assert e_primo(8) == False
    assert e_primo(9) == False
    assert e_primo(10) == False
    assert e_primo(12) == False
    assert e_primo(14) == False
    assert e_primo(15) == False
    assert e_primo(16) == False