# Reto: Lenguaje Pi y Silabeador en Python

## Descripción

En este reto programarás un **silabeador** para trabajar con el "lenguaje pi", el clásico juego infantil donde se intercalaba la sílaba "pi" delante de cada sílaba de una palabra o frase. Además, deberás implementar un traductor inverso que recupere el texto original.

## Objetivos

- Crear una clase `Silabeador` que separe correctamente las palabras en sílabas según reglas del castellano.
- Implementar un método que inserte la sílaba *pi* delante de cada sílaba (modo juego infantil).
- Implementar el método inverso para traducir frases desde el lenguaje pi al español normal.

## Reglas y Especificaciones

- **Separación en sílabas**: 
  - Buscar grupos de vocales.
  - Asignar a la vocal la consonante de su izquierda si existe.
  - Las letras que sobran se agrupan con la sílaba anterior.
- Considerar grupos especiales, diptongos, triptongos, pares de consonantes, y que la letra **y** puede ser vocal o consonante según contexto.
- Prestar atención a casos con el prefijo “in-” (por ejemplo, "inacción" debe ser "in-ac-ción", no "i-nac-ción").
- Ejemplo de funcionamiento:
  - Español: `Hola, me llamo Ramón`
  - Lenguaje pi: `pihopila, pime pillapimo pirrapimn`

## Ejemplo de uso esperado

```python
entrada = "Hola, me llamo Ramón"
salida = Silabeador().a_pi(entrada)
print(salida)
# pihopila, pime pillapimo pirrapimn

print(Silabeador().de_pi(salida))
# Hola, me llamo Ramón
```

## Extras

- Añade más ejemplos de palabras con grupos consonánticos y diptongos.
- Incluye pruebas automatizadas que validen ambos métodos.
- Documenta limitaciones y situaciones especiales que observes.

## Recursos  

Consulta el archivo original adjunto para detalles sobre las **reglas de silabeo**, grupos de letras, casos especiales y ejemplos.
