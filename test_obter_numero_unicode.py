from re import A
from fatores_primos import obter_numero_unicode
from unicode_table import ZERO, UM, DOIS, TRES, QUATRO, CINCO, SEIS, SETE, OITO, NOVE

def test_obter_numero_um_digito():
    assert obter_numero_unicode(0) == ZERO
    assert obter_numero_unicode(1) == UM
    assert obter_numero_unicode(2) == DOIS
    assert obter_numero_unicode(3) == TRES
    assert obter_numero_unicode(4) == QUATRO
    assert obter_numero_unicode(5) == CINCO
    assert obter_numero_unicode(6) == SEIS
    assert obter_numero_unicode(7) == SETE
    assert obter_numero_unicode(8) == OITO
    assert obter_numero_unicode(9) == NOVE

def test_obter_numero_dois_digitos():
    assert obter_numero_unicode(17) == f'{UM}{SETE}'
    assert obter_numero_unicode(23) == f'{DOIS}{TRES}'
    assert obter_numero_unicode(35) == f'{TRES}{CINCO}'