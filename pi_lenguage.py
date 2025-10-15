consonantes = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "ll",
    "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "z"
]

vocales_abiertas = ["a", "e", "o"]

vocales_cerradas = ["i", "u"]

consonantesDobles = ["bl", "cl", "fl", "gl", "kl", "pl", "tl",
                "br", "cr", "dr", "fr", "gr", "kr", "pr", "tr",
                "ch", "ll", "rr"]

def silabear(palabra:str) -> list:
    listaPalabra = list(palabra)
    posicionVocal = {}
    contador = 0
    
    while any(x is not None for x in listaPalabra):
                   
        for letra in listaPalabra:
                    
            if letra  in vocales_abiertas or letra in vocales_cerradas:
                pos= listaPalabra.index(letra)
                if listaPalabra[pos-1]:
                    nl = listaPalabra[pos -1]
                    posicionVocal[pos] = nl + letra
                    listaPalabra[pos] = None
                    listaPalabra[pos-1] = None 
                
                else:
                    nl = listaPalabra[pos + 1] 
                    posicionVocal[pos] = letra

            if contador >= 1 and letra in consonantes:
                posicionVocal[listaPalabra.index(letra)-1] = posicionVocal[listaPalabra.index(letra)-1] + letra
                listaPalabra[listaPalabra.index(letra)] = None
                

        contador += 1    
    silabas = [x for i,x in posicionVocal.items()]
                
    return silabas               

 
 
                

                
                

   
    


def normal_a_pi(palabra: str) -> str:
    pass

    

def pi_a_normal(palabra: str) -> str:
    pass
    
    
