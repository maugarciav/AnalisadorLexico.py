# AnalisadorLexico.py

Instrucciones

Hacer un programa que reciba como entrada en consolar el nombre de un archivo de texto que contenga expresiones aritméticas y comentarios. El programa generará una tabla donde en cada renglón se mostrará el token reconocido (en el orden en que fue encontrado) e indicando de qué tipo es.

Tipos de tokens

Las expresiones aritméticas sólo podrán contener los siguientes tipos de tokens:

Enteros
Flotantes (Reales)
Operadores:
Asignación
Suma
Resta
Multiplicación
División
Potencia
Identificadores:
Variables
Símbolos especiales:
(
)
Comentarios:
// seguido de caracteres hasta que se acabe el renglón

Función principal

El programa podrá estar formado con las funciones que requiera, pero la función principal tendrá la siguiente firma:

def lexerAritmetico(nombre_archivo)

donde nombre_archivo es el nombre del archivo que contiene las expresiones a ser analizadas (el nombre debe incluir la extensión, por ejemplo, expresiones.txt).

Entrada

Un archivo tipo texto que contenga una o más expresiones aritméticas, una por renglón.
Los tokens no necesariamente deben estar separados por un blanco, o pueden tener separación de más de un blanco
Por ejemplo:

b=7

a = 32.4 \*(-8.6 - b)/ 6.1E-8

d = a ^ b // Esto es un comentario

Salida

Debe entregar la siguiente salida:

Token

Tipo

b

Variable

=

Asignación

7

Entero

a

Variable

=

Asignación

32.4

Real

-

Multiplicación

(

Paréntesis que abre

-8.6

Real

-

Resta

b

Variable

)

Paréntesis que cierra

/

División

6.1E-8

Real

d

Variable

=

Asignación

^

Potencia

b

Variable

// Esto es un comentario

Comentario

Reglas de formación de algunos tokens

Variables:
Deben empezar con una letra (mayúscula o minúscula).
Sólo están formadas por letras, números y underscore (‘\_’).
Números reales (de punto flotante):
Pueden ser positivos o negativos
Pueden o no tener parte decimal pero deben contener un punto (e.g. 10. o 10.0)
Pueden usar notación exponencial con la letra E, mayúscula o minúscula, pero después de la letra E sólo puede ir un entero positivo o negativo (e.g. 2.3E3, 6.345e-5, -0.001E-3, .467E9).
Comentarios:
Inician con // y todo lo que sigue hasta que termina el renglón es un comentario

Algoritmo

El reconocimiento de tokens se debe hacer por medio de la tabla de transición de un Autómata Finito Determinístico.
El diseño del autómata debe ser parte fundamental de la documentación (utilice alguna herramienta computacional para dibujarlo, no lo haga a mano).

Documentación:

Manual del usuario, indicando cómo correr su programa.
El autómata que resuelve el problema: diagrama de transiciones y definción formal de la máquina.
