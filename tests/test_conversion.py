import pytest
from pi_language import normal_a_pi, pi_a_normal

def test_normal_a_pi_basicos():
    assert normal_a_pi("hola") == "pihopila"
    assert normal_a_pi("") == ""

def test_normal_a_pi_palabras_silabeadas():
    # cotarte = co-tar-te → pi intercalado
    assert normal_a_pi("cotarte") == "picopitarpite"
    
    # caucho = cau-cho
    assert normal_a_pi("caucho") == "picaupicho"
    """
    # inacción = in-ac-ción
    assert normal_a_pi("inacción") == "piinpiacpición"
    """
    
def test_pi_a_normal_reversion():
    # Verifica que la conversión inversa funcione correctamente
    assert pi_a_normal("pihopila") == "hola"
    assert pi_a_normal("picopitarpite") == "cotarte"
    assert pi_a_normal("picaupicho") == "caucho"
    assert pi_a_normal("piinpiacpición") == "inacción"
    assert pi_a_normal("piflupiye") == "fluye"

@pytest.mark.parametrize(
    "pi_texto,esperado",
    [
        ("pihopila", "hola"),
        ("picopitarpite", "cotarte"),
        ("picaupicho", "caucho"),
        #("piinpiacpición", "inacción"),
       
    ],
)
def test_pi_a_normal_reversion(pi_texto, esperado):
    assert pi_a_normal(pi_texto) == esperado