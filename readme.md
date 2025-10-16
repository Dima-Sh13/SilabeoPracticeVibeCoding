# Proyecto: Traductor al "idioma pi"

Descripción
-----------

Este proyecto implementa un algoritmo para traducir palabras del castellano al llamado "idioma pi" —el juego infantil en el que se añade la sílaba "pi" delante de cada sílaba de una palabra— y utilidades para dividir palabras en protosílabas.

## Objetivos


## Reglas y Especificaciones

  - Buscar grupos de vocales.
  - Asignar a la vocal la consonante de su izquierda si existe.
  - Las letras que sobran se agrupan con la sílaba anterior.
  - Español: `Hola, me llamo Ramón`
  - Lenguaje pi: `pihopila, pime pillapimo pirrapimn`
Qué hace
---------

- Separa una palabra en grupos vocálicos y consonánticos según reglas sencillas de silabeo en castellano.
- Construye las protosílabas (consonantes + grupo vocálico) y las completa para obtener la partición en sílabas.
- Traduce una palabra normal al "idioma pi" prefijando "pi" a cada sílaba.

Archivo principal
-----------------

El código principal está en `pi_language.py`. Funciones útiles:

- `silabear(palabra)` — devuelve una lista con las protosílabas/sílabas de la palabra.
- `normal_a_pi(palabra)` — devuelve la palabra transformada al idioma pi (prefijo "pi" en cada sílaba).
Ejemplo rápido
--------------

En Python puedes usar las funciones del módulo así:

```python
from pi_language import normal_a_pi, silabear

print(silabear("hola"))         # ejemplo de salida: ['ho', 'la']
print(normal_a_pi("hola"))      # -> 'pihola' (dependiendo de la implementación exacta)
```

Nota: hay un esbozo de función inversa (`pi_a_normal`) en el repositorio pero no está implementada completamente.

Limitaciones y supuestos
------------------------

- El algoritmo asume entradas en minúsculas y caracteres alfabéticos simples; puede no manejar correctamente puntuación, mayúsculas o caracteres no latinos sin limpiarlos antes.
- Algunas funciones asumen longitudes mínimas al indexar cadenas (por ejemplo para comprobar diptongos/triptongos). Si quieres, puedo añadir validaciones adicionales.

Cómo contribuir
----------------

- Añade/ajusta reglas de silabeo si detectas casos que no se tratan correctamente (diptongos especiales, hiatos, etc.).
- Implementa la función inversa completa `pi_a_normal` y añade tests en la carpeta `tests/`.
- Mejora la normalización de entrada (gestión de mayúsculas, acentos y signos de puntuación).

Ejemplo de tests sugeridos
-------------------------

- Palabras simples: `hola`, `casa`.
- Palabras con diptongo/triptongo: `huevo`, `Uruguay`.
- Grupos consonánticos: `pluma`, `brisa`.

Si quieres, puedo generar un README más detallado con instrucciones para ejecutar los tests y ejemplos adicionales.
