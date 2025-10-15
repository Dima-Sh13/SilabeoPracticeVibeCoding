CONSONANTES = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "ll", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "z")
VOCALES_ABIERTAS = ("a", "e", "o")
VOCALES_CERRADAS = ("i", "u")
SEMIVOCALES = ("y",)
PARES_CONSONANTES = ("bl", "cl", "fl", "gl", "kl", "pl", "tl", "br", "cr", "dr", "fr", "gr", "kr", "pr", "tr", "ch", "ll", "rr")

def es_vocal(caracter):
    return caracter in VOCALES_ABIERTAS or caracter in VOCALES_CERRADAS

def es_diptongo(grupo):
    if grupo[0] in VOCALES_ABIERTAS and grupo[1] in VOCALES_CERRADAS:
        return True
    elif grupo[0] in VOCALES_CERRADAS and grupo[1] in VOCALES_ABIERTAS:
        return True
    elif grupo[0] in VOCALES_CERRADAS and grupo[1] in VOCALES_CERRADAS:
        return True


def es_grupo_vocalico_ok(grupo, caracter):
    # Asumimos que tanto grupo como caracter solo pueden estar formados por vocales y que caracter siempre va informado (con una vocal)
    if grupo == "": 
        return True
    
    if es_diptongo(grupo + caracter):
        return True
    if es_triptongo(grupo + caracter):
        return True
    
    return False

def es_triptongo(grupo):
    return grupo[0] in VOCALES_CERRADAS and grupo[1] in VOCALES_ABIERTAS and grupo[2] in VOCALES_CERRADAS

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
    return caracter


def add_grupo_consonantes_delante(grupos_vocalicos, palabra):
    ix_grupo_vocalico = 0
    grupos_protosilabas = grupos_vocalicos[:] #para no modificar el original, buena practica
    consonante_anterior = ""
    for caracter in palabra:
        if caracter in grupos_protosilabas[ix_grupo_vocalico]:
            grupos_protosilabas[ix_grupo_vocalico] = consonante_anterior + grupos_protosilabas[ix_grupo_vocalico]
            ix_grupo_vocalico += 1
            consonante_anterior = ""
        else:
            consonante_anterior = es_grupo_consonantico(consonante_anterior, caracter)

    return grupos_protosilabas
    
def silabear(palabra):
    memoria = ""    
    resultado = []
    for caracter in palabra:
        if caracter in VOCALES_ABIERTAS or caracter in VOCALES_CERRADAS:
            resultado.append(memoria + caracter)
        memoria = caracter

def normal_a_pi(palabra):
    pass

def pi_a_normal(palabra):
    pass