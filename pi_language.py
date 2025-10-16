CONSONANTES = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "ll", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "z")
VOCALES_ABIERTAS = ("a", "e", "o")
VOCALES_CERRADAS = ("i", "u")
SEMIVOCALES = ("y",)
PARES_CONSONANTES = ("bl", "cl", "fl", "gl", "kl", "pl", "tl", "br", "cr", "dr", "fr", "gr", "kr", "pr", "tr", "ch", "ll", "rr")

def es_vocal(caracter: str) -> bool:
    """
    Devuelve True si `caracter` es una vocal (abierta o cerrada).

    Asume que `caracter` es una cadena (normalmente de longitud 1).
    """
    return caracter in VOCALES_ABIERTAS or caracter in VOCALES_CERRADAS

def es_diptongo(grupo: str) -> bool:
    """
    Determina si los dos primeros caracteres de `grupo` forman un diptongo.

    Reglas consideradas:
    - abierta + cerrada
    - cerrada + abierta
    - cerrada + cerrada

    Asume que `grupo` tiene al menos 2 caracteres.
    Devuelve True o False.
    """
    if grupo[0] in VOCALES_ABIERTAS and grupo[1] in VOCALES_CERRADAS:
        return True
    elif grupo[0] in VOCALES_CERRADAS and grupo[1] in VOCALES_ABIERTAS:
        return True
    elif grupo[0] in VOCALES_CERRADAS and grupo[1] in VOCALES_CERRADAS:
        return True
    return False

def es_triptongo(grupo: str) -> bool:
    """
    Comprueba si los tres primeros caracteres de `grupo` forman un triptongo.

    Patrón: cerrada, abierta, cerrada.
    Asume que `grupo` tiene al menos 3 caracteres.
    """
    return grupo[0] in VOCALES_CERRADAS and grupo[1] in VOCALES_ABIERTAS and grupo[2] in VOCALES_CERRADAS

def es_grupo_vocalico_ok(grupo: str, caracter: str) -> bool:
    """
    Decide si `caracter` puede añadirse al `grupo` vocálico actual.

    - Si `grupo` está vacío, devuelve True (se puede iniciar un grupo).
    - Si la concatenación `grupo + caracter` forma un diptongo o triptongo, devuelve True.
    - En cualquier otro caso devuelve False.

    Asume que `grupo` y `caracter` contienen vocales.
    """
    # Asumimos que tanto grupo como caracter solo pueden estar formados por vocales y que caracter siempre va informado (con una vocal)
    if grupo == "": 
        return True
    
    if es_diptongo(grupo + caracter):
        return True
    if es_triptongo(grupo + caracter):
        return True
    
    return False


def obtener_grupos_vocalicos(palabra: str) -> list:
    """
    Extrae y devuelve una lista con los grupos vocálicos de `palabra`.

    Cada elemento de la lista es una cadena con una secuencia válida de vocales
    (vocal simple, diptongo o triptongo) encontrada en la palabra, en orden.
    """
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

def es_grupo_consonantico(anterior: str, caracter: str) -> str:
    """
    Devuelve la cadena resultante al combinar `anterior` y `caracter` si forman
    un par consonántico permitido; en caso contrario devuelve solo `caracter`.

    Se usa para construir grupos consonánticos compuestos (por ejemplo 'br', 'pl').
    """
    if anterior + caracter in PARES_CONSONANTES:
        return anterior + caracter
    else:
        return caracter

def add_grupo_consonantes_delante(grupos_vocalicos: list, palabra: str) -> list:
    """Distribuye las consonantes que preceden a cada grupo vocálico.

    Toma la lista `grupos_vocalicos` (como la devuelta por `obtener_grupos_vocalicos`)
    y recorre `palabra` para asociar las consonantes anteriores a cada grupo, devolviendo
    una lista de protosílabas (consonantes + grupo vocálico) en el mismo orden.

    No modifica la lista original (trabaja con una copia).
    """
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
    


def completar(grupos_protosilabicos: list, palabra: str) -> None:
    """
    Rellena las protosílabas incompletas recorriendo la palabra.

    Modifica la lista `grupos_protosilabicos` en sitio añadiendo caracteres
    que faltan según la posición en `palabra`. No devuelve nada.
    """
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


def silabear(palabra: str) -> list:
    """
    Divide `palabra` en protosílabas siguiendo el algoritmo:

    1. Extrae grupos vocálicos válidos con `obtener_grupos_vocalicos`.
    2. Asocia las consonantes anteriores a cada grupo con `add_grupo_consonantes_delante`.
    3. Completa las protosílabas con `completar`.

    Devuelve la lista final de protosílabas/sílabas.
    """
    grupos_vocalicos = obtener_grupos_vocalicos(palabra)
    grupos_protosilabicos = add_grupo_consonantes_delante(grupos_vocalicos, palabra)
    completar(grupos_protosilabicos, palabra)
    return grupos_protosilabicos






def normal_a_pi(palabra: str) -> str:
    """
    Convierte `palabra` al dialecto 'pi' prefijando 'pi' a cada sílaba.

    Usa `silabear` para obtener las sílabas y concatena 'pi' + sílaba para cada una.
    Devuelve la palabra transformada.
    """
    silabas = silabear(palabra)
    piSilabas = []
    
    for silaba in silabas:
        piSilabas.append("pi" + silaba)
    pipalabra = "".join(piSilabas)
    return pipalabra     

    
"""
def pi_a_normal(palabra):
    silabasNormal= []
    ix_pi = 0
    silaba_anterior =    
    for i in silabear(palabra)[1]:
        
    palabraNormal = "".join(silabasNormal)        


   

    return palabraNormal
"""
    
if __name__ == "__main__":
    print(pi_a_normal("pihopila"))