from fatores_primos import fatores_primos

def test_deve_retornar_os_fatores_primos_de_10():
    assert fatores_primos(10) == [2, 5]

def test_deve_retornar_os_fatores_primos_de_30():
    assert fatores_primos(30) == [2, 3, 5]

def test_deve_retornar_os_fatores_primos_de_72():
    assert fatores_primos(72) == [2, 2, 2, 3, 3]

def test_deve_retornar_os_fatores_primos_de_56():
    assert fatores_primos(56) == [2, 2, 2, 7]

def test_deve_retornar_os_fatores_primos_de_9():
    assert fatores_primos(9) == [3, 3]

def test_deve_retornar_os_fatores_primos_de_2():
    assert fatores_primos(2) == [2]

def test_deve_retornar_os_fatores_primos_de_3():
    assert fatores_primos(3) == [3]

def test_deve_retornar_os_fatores_primos_de_4():
    assert fatores_primos(4) == [2, 2]

def test_deve_retornar_os_fatores_primos_de_5():
    assert fatores_primos(5) == [5]

def test_deve_retornar_os_fatores_primos_de_6():
    assert fatores_primos(6) == [2, 3]

def test_deve_retornar_os_fatores_primos_de_7():
    assert fatores_primos(7) == [7]

def test_deve_retornar_os_fatores_primos_de_8():
    assert fatores_primos(8) == [2, 2, 2]

def test_deve_retornar_os_fatores_primos_de_11():
    assert fatores_primos(11) == [11]

def test_deve_retornar_os_fatores_primos_de_12():
    assert fatores_primos(12) == [2, 2, 3]

def test_deve_retornar_os_fatores_primos_de_13():
    assert fatores_primos(13) == [13]

def test_deve_retornar_os_fatores_primos_de_14():
    assert fatores_primos(14) == [2, 7]

def test_deve_retornar_os_fatores_primos_de_15():
    assert fatores_primos(15) == [3, 5]

def test_deve_retornar_os_fatores_primos_de_16():
    assert fatores_primos(16) == [2, 2, 2, 2]

def test_deve_retornar_os_fatores_primos_de_17():
    assert fatores_primos(17) == [17]

def test_deve_retornar_os_fatores_primos_de_18():
    assert fatores_primos(18) == [2, 3, 3]

def test_deve_retornar_os_fatores_primos_de_19():
    assert fatores_primos(19) == [19]

def test_deve_retornar_os_fatores_primos_de_20():
    assert fatores_primos(20) == [2, 2, 5]

def test_deve_retornar_os_fatores_primos_de_84():
    assert fatores_primos(84) == [2, 2, 3, 7]