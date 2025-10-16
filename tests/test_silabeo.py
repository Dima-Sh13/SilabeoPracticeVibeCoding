import pytest
from pi_language import silabear

def test_silabear_basicos():
    # hola → ho-la
    assert silabear("hola") == ["ho", "la"]
    
    # palabra vacía → lista vacía
    assert silabear("") == []

def test_silabear_palabras_silabeadas():
    # cotarte → co-tar-te
    assert silabear("cotarte") == ["co", "tar", "te"]
    
    # caucho → cau-cho
    assert silabear("caucho") == ["cau", "cho"]
    
   
    
    # fluye → flu-ye
    assert silabear("fluye") == ["flu", "ye"]

@pytest.mark.parametrize(
    "palabra,esperado",
    [
        ("hola", ["ho", "la"]),
        ("cotarte", ["co", "tar", "te"]),
        ("caucho", ["cau", "cho"]),
       
        ("fluye", ["flu", "ye"]),
    ],
)
def test_silabear_parametrizado(palabra, esperado):
    assert silabear(palabra) == esperado