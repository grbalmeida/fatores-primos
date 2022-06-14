from fatores_primos import fatores_primos, fatores_primos_multiplicacao

def test_deve_retornar_os_fatores_primos_de_10():
    assert fatores_primos(10) == [2, 5]
    assert fatores_primos_multiplicacao(10) == '10 = 2 * 5'

def test_deve_retornar_os_fatores_primos_de_30():
    assert fatores_primos(30) == [2, 3, 5]
    assert fatores_primos_multiplicacao(30) == '30 = 2 * 3 * 5'

def test_deve_retornar_os_fatores_primos_de_72():
    assert fatores_primos(72) == [2, 2, 2, 3, 3]
    assert fatores_primos_multiplicacao(72) == '72 = 2 * 2 * 2 * 3 * 3'

def test_deve_retornar_os_fatores_primos_de_56():
    assert fatores_primos(56) == [2, 2, 2, 7]
    assert fatores_primos_multiplicacao(56) == '56 = 2 * 2 * 2 * 7'

def test_deve_retornar_os_fatores_primos_de_9():
    assert fatores_primos(9) == [3, 3]
    assert fatores_primos_multiplicacao(9) == '9 = 3 * 3'

def test_deve_retornar_os_fatores_primos_de_2():
    assert fatores_primos(2) == [2]
    assert fatores_primos_multiplicacao(2) == '2 = 2'

def test_deve_retornar_os_fatores_primos_de_3():
    assert fatores_primos(3) == [3]
    assert fatores_primos_multiplicacao(3) == '3 = 3'

def test_deve_retornar_os_fatores_primos_de_4():
    assert fatores_primos(4) == [2, 2]
    assert fatores_primos_multiplicacao(4) == '4 = 2 * 2'

def test_deve_retornar_os_fatores_primos_de_5():
    assert fatores_primos(5) == [5]
    assert fatores_primos_multiplicacao(5) == '5 = 5'

def test_deve_retornar_os_fatores_primos_de_6():
    assert fatores_primos(6) == [2, 3]
    assert fatores_primos_multiplicacao(6) == '6 = 2 * 3'

def test_deve_retornar_os_fatores_primos_de_7():
    assert fatores_primos(7) == [7]
    assert fatores_primos_multiplicacao(7) == '7 = 7'

def test_deve_retornar_os_fatores_primos_de_8():
    assert fatores_primos(8) == [2, 2, 2]
    assert fatores_primos_multiplicacao(8) == '8 = 2 * 2 * 2'

def test_deve_retornar_os_fatores_primos_de_11():
    assert fatores_primos(11) == [11]
    assert fatores_primos_multiplicacao(11) == '11 = 11'

def test_deve_retornar_os_fatores_primos_de_12():
    assert fatores_primos(12) == [2, 2, 3]
    assert fatores_primos_multiplicacao(12) == '12 = 2 * 2 * 3'

def test_deve_retornar_os_fatores_primos_de_13():
    assert fatores_primos(13) == [13]
    assert fatores_primos_multiplicacao(13) == '13 = 13'

def test_deve_retornar_os_fatores_primos_de_14():
    assert fatores_primos(14) == [2, 7]
    assert fatores_primos_multiplicacao(14) == '14 = 2 * 7'

def test_deve_retornar_os_fatores_primos_de_15():
    assert fatores_primos(15) == [3, 5]
    assert fatores_primos_multiplicacao(15) == '15 = 3 * 5'

def test_deve_retornar_os_fatores_primos_de_16():
    assert fatores_primos(16) == [2, 2, 2, 2]
    assert fatores_primos_multiplicacao(16) == '16 = 2 * 2 * 2 * 2'

def test_deve_retornar_os_fatores_primos_de_17():
    assert fatores_primos(17) == [17]
    assert fatores_primos_multiplicacao(17) == '17 = 17'

def test_deve_retornar_os_fatores_primos_de_18():
    assert fatores_primos(18) == [2, 3, 3]
    assert fatores_primos_multiplicacao(18) == '18 = 2 * 3 * 3'

def test_deve_retornar_os_fatores_primos_de_19():
    assert fatores_primos(19) == [19]
    assert fatores_primos_multiplicacao(19) == '19 = 19'

def test_deve_retornar_os_fatores_primos_de_20():
    assert fatores_primos(20) == [2, 2, 5]
    assert fatores_primos_multiplicacao(20) == '20 = 2 * 2 * 5'

def test_deve_retornar_os_fatores_primos_de_84():
    assert fatores_primos(84) == [2, 2, 3, 7]
    assert fatores_primos_multiplicacao(84) == '84 = 2 * 2 * 3 * 7'

def test_deve_retornar_os_fatores_primos_de_2205():
    assert fatores_primos(2205) == [3, 3, 5, 7, 7]
    assert fatores_primos_multiplicacao(2205) == '2205 = 3 * 3 * 5 * 7 * 7'

def test_deve_retornar_os_fatores_primos_de_13958():
    assert fatores_primos(13958) == [2, 7, 997]
    assert fatores_primos_multiplicacao(13958) == '13958 = 2 * 7 * 997'

def test_deve_retornar_os_fatores_primos_de_139581():
    assert fatores_primos(139581) == [3, 3, 13, 1193]
    assert fatores_primos_multiplicacao(139581) == '139581 = 3 * 3 * 13 * 1193'

def test_deve_retornar_os_fatores_primos_de_20000():
    assert fatores_primos(20000) == [2, 2, 2, 2, 2, 5, 5, 5, 5]
    assert fatores_primos_multiplicacao(20000) == '20000 = 2 * 2 * 2 * 2 * 2 * 5 * 5 * 5 * 5'