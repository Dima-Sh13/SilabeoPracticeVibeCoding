# Reglas de Silabeo en Español

## 1. Introducción

El silabeo es el proceso de separar una palabra en sílabas siguiendo reglas fonéticas del idioma español. Las siguientes reglas te ayudarán a dividir correctamente las palabras para distintos fines, como el juego del "lenguaje pi".

## 2. Tipos de Letras

- **Consonantes**: b, c, d, f, g, h, j, k, l, ll, m, n, ñ, p, q, r, s, t, v, w, x, z
- **Vocales Abiertas**: a, e, o
- **Vocales Cerradas**: i, u
- **Semivocales**: y (según posición, puede ser vocal o consonante)

## 3. Diptongos y Triptongos

- **Diptongos**: 
  - Vocal cerrada + vocal cerrada (ej: ciudad)
  - Vocal abierta + vocal cerrada (ej: buey)
  - Vocal cerrada + vocal abierta (ej: cuadro)
- **Triptongos**: Vocal cerrada + vocal abierta + vocal cerrada (ej: limpiáis)

## 4. Pares de Consonantes

Los siguientes pares se agrupan y no se separan en sílabas distintas:
- bl, cl, fl, gl, kl, pl, tl
- br, cr, dr, fr, gr, kr, pr, tr
- ch, ll, rr

## 5. Algoritmo Básico de Separación

1. Buscar grupos de vocales para comenzar la sílaba.
2. Asignar a la vocal la consonante inmediatamente a su izquierda, si existe (y no forma parte de los pares especiales).
3. Cuando sobran letras (consonantes), se añaden a la sílaba anterior.
4. Repetir hasta que se terminen las letras.

## 6. Ejemplos de Separación

| Palabra      | Separación en sílabas |
|:------------:|:--------------------:|
| cotarte   | co-tar-te               |
| caucho    | cau-cho                 |
| inacción  | in-ac-ción              |
| fluye     | flu-ye                  |

## 7. Casos Especiales y Excepciones

- La **y** puede funcionar como vocal (soy) o consonante (yo).
- El prefijo **in-**: en palabras como inacción, el algoritmo básico podría fallar (producir i-nac-ción en vez de in-ac-ción).
- Existen otras excepciones con palabras de origen extranjero o compuestas, así que revisa y ajusta según contexto.

## 8. Consejos

- Prueba el silabeo con palabras que incluyan diptongos, triptongos y grupos de consonantes.
- Si tienes duda, consulta la separación oficial en diccionarios académicos.
