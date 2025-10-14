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
    word = list(palabra)
    silabas = []
    posVoc = {}
    contador = 0
    while any(x is not None for x in word):
        for i in word:
            if i  in vocales_abiertas or i in vocales_cerradas:
                pos= word.index(i)
                
                
                if word[pos-1]:
                    nl = word[pos -1]
                    silabas.append(nl + i)
                    posVoc[pos] = nl + i
                    word[pos] = None
                    word[pos-1] = None 
                    
                else:
                   silabas.append(i)
            if contador >= 1 and i in consonantes:
                consPos= word.index(i)
                posVoc[consPos-1] = posVoc[consPos-1] + i
                word[consPos] = None

        contador += 1    

    silabas = [x for i,x in posVoc.items()]

        
                
    return silabas               

                
print(silabear("cotarte"))                   

   
    


def normal_a_pi(palabra: str) -> str:
    pass

    

def pi_a_normal(palabra: str) -> str:
    pass
    
    
