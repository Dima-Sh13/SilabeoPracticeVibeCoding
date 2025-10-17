from enum import Enum

CONSONANTES = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "ll", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "z")
VOCALES_ABIERTAS = ("a", "e", "o")
VOCALES_CERRADAS = ("i", "u")
SEMIVOCALES = ("y",)
PARES_CONSONANTES = ("bl", "cl", "fl", "gl", "kl", "pl", "tl", "br", "cr", "dr", "fr", "gr", "kr", "pr", "tr", "ch", "ll", "rr")

class ES_PI(Enum):
    NO_HAY_PI = 0
    SOLO_P = 1
    YA_HAY_PI = 2

class TipoCaracter(Enum):
    LETRA = 1
    ESPACIO = 2
    OTRO = 3


def es_vocal(caracter):
    return caracter in VOCALES_ABIERTAS or caracter in VOCALES_CERRADAS

def es_diptongo(grupo):
    if grupo[0] in VOCALES_ABIERTAS and grupo[1] in VOCALES_CERRADAS:
        return True
    elif grupo[0] in VOCALES_CERRADAS and grupo[1] in VOCALES_ABIERTAS:
        return True
    elif grupo[0] in VOCALES_CERRADAS and grupo[1] in VOCALES_CERRADAS:
        return True

def es_triptongo(grupo):
    return grupo[0] in VOCALES_CERRADAS and grupo[1] in VOCALES_ABIERTAS and grupo[2] in VOCALES_CERRADAS

def es_grupo_vocalico_ok(grupo, caracter):
    # Asumimos que tanto grupo como caracter solo pueden estar formados por vocales y que caracter siempre va informado (con una vocal)
    if grupo == "": 
        return True
    
    if es_diptongo(grupo + caracter):
        return True
    if es_triptongo(grupo + caracter):
        return True
    
    return False


def obtener_grupos_vocalicos(palabra):
    grupos_vocalicos = []
    grupo = ""
    for caracter in palabra:
        if es_vocal(caracter):
            if es_grupo_vocalico_ok(grupo, caracter):
                grupo += caracter
            else:
                grupos_vocalicos.append(grupo)
                grupo = caracter
        elif grupo:
            grupos_vocalicos.append(grupo)
            grupo = ""

    if grupo:
        grupos_vocalicos.append(grupo)

    
    return grupos_vocalicos

def es_grupo_consonantico(anterior, caracter):
    if anterior + caracter in PARES_CONSONANTES:
        return anterior + caracter
    else:
        return caracter

def add_grupo_consonantes_delante(grupos_vocalicos, palabra):
    ix_grupo_vocalico = 0
    grupos_protosilabas = grupos_vocalicos[:] #para no modificar el original, buena practica
    consonante_anterior = ""

    for caracter in palabra:
        if ix_grupo_vocalico >= len(grupos_protosilabas):
            break
        if caracter in grupos_protosilabas[ix_grupo_vocalico]:
            grupos_protosilabas[ix_grupo_vocalico] = consonante_anterior + grupos_protosilabas[ix_grupo_vocalico]
            ix_grupo_vocalico += 1
            consonante_anterior = ""
        else:
            consonante_anterior = es_grupo_consonantico(consonante_anterior, caracter)

    return grupos_protosilabas
    

def completar(grupos_protosilabicos, palabra):
    ix_grupo = 0
    ix_dentro_grupo = 0

    for caracter in palabra:
        if ix_dentro_grupo < len(grupos_protosilabicos[ix_grupo]) and \
           caracter == grupos_protosilabicos[ix_grupo][ix_dentro_grupo]:
            ix_dentro_grupo +=1
            continue
        else:
            if ix_grupo < len(grupos_protosilabicos)-1  and \
               caracter == grupos_protosilabicos[ix_grupo + 1][0]:
                ix_grupo += 1
                ix_dentro_grupo = 1
            else:
                grupos_protosilabicos[ix_grupo] += caracter



def silabear(palabra):
    grupos_vocalicos = obtener_grupos_vocalicos(palabra)
    grupos_protosilabicos = add_grupo_consonantes_delante(grupos_vocalicos, palabra)
    completar(grupos_protosilabicos, palabra)
    return grupos_protosilabicos

def normal_a_pi(palabra):
    if palabra == "":
        return ""
    silabas = silabear(palabra)
    resultado = ""
    for silaba in silabas:
        resultado += "pi" + silaba
    return resultado

def pi_a_normal(palabra):
    resultado = ""
    pi_en_construccion = ES_PI.NO_HAY_PI
    for caracter in palabra:
        if caracter == "p" and pi_en_construccion == ES_PI.NO_HAY_PI:
            pi_en_construccion = ES_PI.SOLO_P
            continue

        if caracter == "i" and pi_en_construccion == ES_PI.SOLO_P:
            pi_en_construccion = ES_PI.YA_HAY_PI
            continue

        pi_en_construccion = ES_PI.NO_HAY_PI
        resultado += caracter

    return resultado

def tokenizar(frase: str) -> list[str]:
    """
    Divide una frase en tokens según las reglas del modelo:
    - Letras válidas: las definidas en las constantes del sistema.
    - También se aceptan números.
    - Espacios y signos de puntuación se devuelven como tokens independientes.
    """
    if not frase:
        return []

    LETRAS_VALIDAS = set(
        sum([list(CONSONANTES), list(VOCALES_ABIERTAS), list(VOCALES_CERRADAS), list(SEMIVOCALES)], [])
    )

    tokens = []
    token_actual = ""
    tipo_actual = None  # Será un valor de TipoCaracter

    def tipo_de_caracter(c):
        if c.lower() in LETRAS_VALIDAS:
            return TipoCaracter.LETRA
        elif c.isspace():
            return TipoCaracter.ESPACIO
        else:
            return TipoCaracter.OTRO

    for caracter in frase:
        tipo = tipo_de_caracter(caracter)

        if tipo_actual is None:
            token_actual = caracter
            tipo_actual = tipo
        elif tipo == tipo_actual:
            token_actual += caracter
        else:
            tokens.append(token_actual)
            token_actual = caracter
            tipo_actual = tipo

    if token_actual:
        tokens.append(token_actual)

    return tokens

def es_token_procesable(token):
    """
    Devuelve True si el token está formado solo por letras válidas o números,
    según las constantes definidas en el sistema (CONSONANTES, VOCALES, SEMIVOCALES).
    """
    if not token:
        return False

    letras_validas = set(
        sum([list(CONSONANTES), list(VOCALES_ABIERTAS), list(VOCALES_CERRADAS), list(SEMIVOCALES)], [])
    )

    for c in token.lower():
        if c not in letras_validas:
            return False

    return True


def procesar_tokens(tokens, funcion_transformacion):
    """
    Recorre los tokens y aplica la función indicada (normal_a_pi o pi_a_normal)
    solo a aquellos que sean procesables (palabras o alfanuméricos).
    El resto de tokens se dejan sin modificar.
    """
    if not tokens:
        return []

    resultado = []
    for token in tokens:
        if es_token_procesable(token):
            resultado.append(funcion_transformacion(token))
        else:
            resultado.append(token)

    return resultado

def reconstruir_frase(tokens):
    """
    Toma una lista de tokens y devuelve una cadena con todos ellos concatenados
    en el mismo orden. No altera los tokens ni introduce separadores.
    """
    if not tokens:
        return ""

    return "".join(tokens)

def frase_a_pi(frase):
    """
    Convierte una frase completa al lenguaje pi usando el pipeline:
    tokenizar -> procesar_tokens(normal_a_pi) -> reconstruir_frase
    """
    if not frase:
        return ""

    tokens = tokenizar(frase)
    tokens_procesados = procesar_tokens(tokens, normal_a_pi)
    return reconstruir_frase(tokens_procesados)


def pi_a_frase(frase):
    """
    Convierte una frase completa del lenguaje pi al español normal usando el pipeline:
    tokenizar -> procesar_tokens(pi_a_normal) -> reconstruir_frase
    """
    if not frase:
        return ""

    tokens = tokenizar(frase)
    tokens_procesados = procesar_tokens(tokens, pi_a_normal)
    return reconstruir_frase(tokens_procesados)