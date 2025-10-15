import pytest
from pi_language import obtener_grupos_vocalicos, es_grupo_vocalico_ok, add_grupo_consonantes_delante

@pytest.mark.parametrize("grupo, car, esperado", [
    # --- Casos base (inicio de grupo) ---
    ("", "a", True),
    ("", "i", True),

    # --- Diptongos válidos ---
    # Cerrada + cerrada
    ("i", "u", True),   # ciudad
    ("u", "i", True),   # ruido

    # Abierta + cerrada
    ("a", "i", True),   # aire
    ("e", "i", True),   # peine
    ("o", "i", True),   # boina
    ("a", "u", True),   # causa
    ("e", "u", True),   # neutro
    ("o", "u", True),   # bou

    # Cerrada + abierta
    ("i", "a", True),   # tierra
    ("i", "e", True),   # cielo
    ("i", "o", True),   # vio
    ("u", "a", True),   # cuadro
    ("u", "e", True),   # bueno
    ("u", "o", True),   # cuota

    # --- Triptongos válidos ---
    ("ui", "a", True),  # guiais / guau / limpiais (inicio de triptongo)
    ("ui", "e", True),  # similar patron triptongal
    ("uai", "", True),  # guais
    ("iai", "", True),  # limpiais
    ("uau", "", True),  # guau

    # --- No forman grupo vocalico (hiatos o repeticiones) ---
    ("a", "a", False),
    ("e", "e", False),
    ("a", "e", False),
    ("e", "a", False),
    ("o", "a", False),
    ("a", "o", False),

])
def test_es_grupo_vocalico_ok(grupo, car, esperado):
    """
    Test que valida la correcta deteccion de formacion de diptongos y triptongos
    segun las reglas foneticas del espanol.
    """
    assert es_grupo_vocalico_ok(grupo, car) == esperado

import pytest

@pytest.mark.parametrize("palabra, grupos_vocalicos, esperado", [
    # --- 1. Palabras simples (una consonante delante) ---
    ("casa", ["a", "a"], ["ca", "sa"]),
    ("mesa", ["e", "a"], ["me", "sa"]),
    ("lobo", ["o", "o"], ["lo", "bo"]),

    # --- 2. Consonante inicial sin vocal previa ---
    ("pato", ["a", "o"], ["pa", "to"]),
    ("gato", ["a", "o"], ["ga", "to"]),

    # --- 3. Dos consonantes antes del grupo vocálico ---
    ("plato", ["a", "o"], ["pla", "to"]),     # grupo 'pl' inseparable
    ("fruta", ["u", "a"], ["fru", "ta"]),     # grupo 'fr' inseparable
    ("alto", ["a", "o"], ["a", "to"]),        # 'l' no se une, pertenece a sílaba anterior
    ("interior", ["i", "e", "io"], ["i", "te", "rio"]),

    # --- 4. Tres consonantes consecutivas ---
    ("transporte", ["a", "o", "e"], ["tra", "po", "te"]),
    ("instructor", ["i", "u", "o"], ["i", "tru", "to"]),
    ("extrano", ["a", "o"], ["e", "tra"]),

    # --- 5. Grupos inseparables especiales ---
    ("chico", ["i", "o"], ["chi", "co"]),
    ("llama", ["a", "a"], ["lla", "ma"]),
    ("perro", ["e", "o"], ["pe", "rro"]),

    # --- 6. Palabras con varias sílabas ---
    ("murcielago", ["u", "ie", "a", "o"], ["mu", "cie", "la", "go"]),
    ("problema", ["o", "e", "a"], ["pro", "ble", "ma"]),
    ("cristal", ["i", "a"], ["cri", "ta"]),

    # --- 7. Casos límite (sin consonantes delante) ---
    ("aereo", ["a", "e", "eo"], ["a", "e", "eo"]),
    ("uva", ["u", "a"], ["u", "va"]),
])

def test_add_grupo_consonantes_delante(palabra, grupos_vocalicos, esperado):
    """
    Test que valida la correcta union de consonantes iniciales con
    los grupos vocalicos segun las reglas del silabeo en espanol.
    No se incluyen las consonantes finales de cada silaba.
    """
    assert add_grupo_consonantes_delante(grupos_vocalicos, palabra) == esperado




@pytest.mark.parametrize("palabra, grupos_esperados", [
    # --- Vocales simples ---
    ("casa", ["a", "a"]),
    ("perro", ["e", "o"]),
    ("luz", ["u"]),

    # --- Diptongos crecientes (cerrada + abierta) ---
    ("tierra", ["ie", "a"]),
    ("cuadro", ["ua", "o"]),

    # --- Diptongos decrecientes (abierta + cerrada) ---
    ("aire", ["ai", "e"]),
    ("peine", ["ei", "e"]),

    # --- Diptongos de dos cerradas ---
    ("ciudad", ["iu", "a"]),
    ("viuda", ["iu", "a"]),

    # --- Triptongos (cerrada + abierta + cerrada) ---
    ("limpiais", ["iai"]),
    ("buey", ["uey"]),

    # --- Hiatos (vocales separadas) ---
    ("poeta", ["o", "e", "a"]),
    ("rio", ["i", "o"]),
    ("pais", ["a", "i"]),

    # --- 'y' como vocal ---
    ("hoy", ["oy"]),
    ("rey", ["ey"]),

    # --- 'y' como consonante ---
    ("ya", ["a"]),
    ("ayuda", ["ayu", "a"]),

    # --- Casos complejos / multiples grupos ---
    ("murcielago", ["u", "ie", "a", "o"]),
    ("guau", ["uau"]),
])
def test_grupos_vocalicos(palabra, grupos_esperados):
    """
    Test que valida la deteccion de grupos vocalicos en palabras del espanol.
    La funcion 'obtener_grupos_vocalicos' debe devolver una lista de grupos.
    """
    assert obtener_grupos_vocalicos(palabra) == grupos_esperados