
> En matemáticas, un número primo es un número natural mayor que 1 que tiene únicamente dos divisores positivos distintos: él mismo y el 1.

Sabiendo la definición de los números primos podemos idear diferentes tipos de algoritmos para la comprobación:

- Trial Division 
- GNFS & Sieve of eratosthenes
- Dijkstra

Según el algoritmo utilizado obtendremos:
- Uso eficiente de memoria ( Trial division )
- Eficiencia de ejecución ( GNFS, Sieve of eratosthenes )
- Eficiencia de ejecución y uso de memoria. ( Dijkstra )

Podemos pensar en el algoritmo de Dijkstra como un punto intermedio entre los otros dos algoritmos implementados anteriormente. 

En este caso intentaremos optimizar el algoritmo *Trial Division* lo máximo posible.

## Fórmula de Willans

En 1964 Willans concibió una formula generadora de números primos. 
$$p_{n} = 1 + \sum_{i=1}^{2^n}\left \lfloor \left (  \frac{n}{\sum_{j=1}^{i}\left \lfloor (\cos \pi \frac{(j-1)!+1}{j})^2 \right \rfloor}\right )^\frac{1}{n} \right \rfloor$$

Esta formula es bastante astuta ya que utiliza funciones algebraicas para expresar condiciones.

### Funcionamiento de la formula de Willans

Empecemos con la parte más interna que demuestra un patrón interesante:
$
\frac{(j-1)!+1}{j}
$
Al aplicar esta formula a diferentes números resulta que obtenemos dos tipos de valores. Enteros y Reales. Los enteros los obtenemos cuando *j* es un número primo
$
j = 5
$
$
(5-1)! = 1 · 2 · 3 · 4 · 5 = 24
$
$
\frac{24+1}{5} = \frac{25}{5} = 5
$
$
j = 6
$
$
(6-1)! = 1·2·3·4·5 = 120
$
$
\frac{120+1}{6} = \frac{121}{6}
$
Aquí una tabla con los primeros 10 números. Como se puede observar el resultado es cada vez más grande. Esto será problemático si queremos utilizar esta fórmula para calcular el número primo *n*.

| $J$   | $Resultado$     | $J$    | $Resultado$           |
| ----- | --------------- | ------ | --------------------- |
| $$1$$ | $$2$$           | $$6$$  | $$\frac{121}{6}$$     |
| $$2$$ | $$1$$           | $$7$$  | $$103$$               |
| $$3$$ | $$1$$           | $$8$$  | $$\frac{5041}{8}$$    |
| $$4$$ | $$\frac{7}{4}$$ | $$9$$  | $$\frac{40321}{9}$$   |
| $$5$$ | $$5$$           | $$10$$ | $$\frac{362881}{10}$$ |
Esta fórmula hace uso del teorema de Wilson:

> $(j-1)!+1$ Será divisible por $j$ siempre y cuando $j$ sea un primo o $1$

#### Conversión algebraica de Entero a Booleano ( 0 / 1 )

Para convertir los valores enteros obtenidos de antes a un booleano, es decir, 0 o 1 podemos introducir el resultado de la operación anterior en la función $\cos\pi x$ dónde *x* es el resultado obtenido. Esto nos dará una valor entre 1 y -1. Para solventarlo elevaremos al cuadrado para eliminar los número negativos y aplicaremos la función de *floor* o piso para truncar los valores a 1 o a 0.

[Este video](https://www.youtube.com/watch?app=desktop&v=j5s0h42GfvM) explica muy bien el funcionamiento entero de la fórmula


Anteriormente se mencionó que intentar usar la formula de willans seria un problema. Esto es porque la división entera de números tan grandes no es posible. Los procesadores, hasta ahora nada más manejan enteros de un máximo de 64 bits.

Al usar factorización los números crecen de tal forma que alrededor de 150~170 ya estamos llegando al máximo.

El código utilizando la fórmula de Willans seria siguiente:

```python
def factorial(n):
    if n < 0:
        print("No hay factorial de 0")
        return 0
    elif n <= 1:
        return 1
    else:
        last = n*factorial(n-1)
        return last

def checkIfPrime(n):
    primeNum = math.pow(math.cos(math.pi*((factorial(n-1)+1)//n)), 2)
    if primeNum < 1:
        print(f"{n} is not prime, res: {primeNum:.5}")
    else:
         print(f"{n} is prime, res: {primeNum:.5}")
         
if __name__ == "__main__":
    for i in range(1,150):
        (checkIfPrime(i))
```

## Trial Division

Nos centraremos en el algoritmo de *Trial división* que consiste en ir dividiendo de $n$ hasta $2$ y revisando si el resto es o no 0.

Se probará cada de iteración del algoritmo tal que los números usados consistan de $(1,10^{a})$ donde $a$ es el número de la prueba. Se repetirá la prueba un total de 5 veces, y se hará media de los resultados.

La primera iteración de este algoritmo es bastante sencilla:

```python
# First iteration of Trial Division
def trial_division(n):
	if (n <= 1):
		return print(False)
    if (n <= 3):
        return print(True)
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
          return print(False)
    return print(True)
```

```
==== Averages ====
Average for 10^1 ran 5 times: 0.000730300 seconds
Average for 10^2 ran 5 times: 0.006454820 seconds
Average for 10^3 ran 5 times: 0.069088780 seconds
Average for 10^4 ran 5 times: 0.783162400 seconds
Average for 10^5 ran 5 times: 17.813185760 seconds
Average for 10^6 ran 5 times: 989.166863780 seconds
```

La primera optimización que podemos utilizar es intercambiar el rango que estamos revisando. El rango va de $$2$ a $n \div 2 + 1$ .  Esto se puede cambiar para que el número vaya de $2$ a $\sqrt{n}$ . Esto especialmente bueno cuando se trata de números grandes.

Esta optimización es posible gracias a lo siguiente:
- Si $n$ no es primo, entonces $n = ab$ donde $a < n$ y  $a < b$, estos factores no pueden ser mayores que $\sqrt{n}$. De tal forma podemos parar de buscar cuando llegamos a $\sqrt{n}$
- Si tuviesemos un facto donde $f > \sqrt{n}$ entonces $$
$$f':= \frac{n}{f} < \frac{n}{\sqrt{n}} = \sqrt{n}$$

También es un factor.
 
```python
import math
def trial_division_2(n):
    if (n <= 1):
        return print(False)
    if (n <= 3):
        return print(True)
    for i in range(2, math.sqrt(n)):
        if (n % i == 0):
          return print(False)
    return print(True)
```

```
==== Averages ===
Average for 10^1 ran 5 times: 0.000717680 seconds
Average for 10^2 ran 5 times: 0.006448400 seconds
Average for 10^3 ran 5 times: 0.065594860 seconds
Average for 10^4 ran 5 times: 0.673308800 seconds
Average for 10^5 ran 5 times: 6.679914820 seconds
Average for 10^6 ran 5 times: 67.815453180 seconds

```

La siguiente optimización que podemos hacer tiene que ver con que números nos podemos saltar. Si, podemos saltar más números. Como cualquier numero terminado en $0, 2, 4, 6, 8$ Es fácilmente divisible entre $2$ pues podemos simplemente no tomarlos en cuenta. También ya tenemos el caso de $0,1,2$ revisado por ende podemos hacer la siguiente optimización.

```python
def trial_division_3(n):
    if (n <= 1):
        return print(False)
    if (n <= 3):
        return print(True)
    if (n % 2 == 0):
        return print(False)
    for i in range(3, int(math.sqrt(n)),2):
        if (n % i == 0):
          return print(False)
    return print(True)
```

```
==== Averages ====
Average for 10^1 ran 5 times: 0.000567840 seconds
Average for 10^2 ran 5 times: 0.006635700 seconds
Average for 10^3 ran 5 times: 0.069064380 seconds
Average for 10^4 ran 5 times: 0.646215160 seconds
Average for 10^5 ran 5 times: 6.412785520 seconds
Average for 10^6 ran 5 times: 65.024313720 seconds

```

Haremos la misma optimización para los números que sean divisibles entre 3 y 5.

```python
def trial_division_4(n):
    if (n <= 1):
        return print(False)
    if (n <= 3):
        return print(True)
    if (n % 2 == 0):
        return print(False)
    if (n % 3 == 0):
        return print(False)
    if (n % 5 == 0):
        return print(False)
    for i in range(3, int(math.sqrt(n)),2):
        if (n % i == 0):
          return print(False)
          #return False
    return print(True)
```

```
==== Averages ====
Average for 10^1 ran 5 times: 0.000736660 seconds
Average for 10^2 ran 5 times: 0.006261100 seconds
Average for 10^3 ran 5 times: 0.061439100 seconds
Average for 10^4 ran 5 times: 0.644016080 seconds
Average for 10^5 ran 5 times: 6.422764340 seconds
Average for 10^6 ran 5 times: 64.943864680 seconds
```

Podemos ir más rápido. Intentemos con **C**. Utilizaremos la opción de compilación `-Ofast` y utilizaremos `gcc` como compilador. 

```C
void trialDivision(int n){
    if (n <= 1)
    {
        printf("false\n");  
    } else if (n <= 3)
    {
        printf("false\n");
    } else
    {
    for(size_t m = 3; m < sqrt(n); m+=2)
        {
            if(n % m == 0)
            {
               printf("false\n");
            }
        }
    }
    printf("true\n");
}
```

```
==== Averages ====
Result for 10^1: 0.001000000000
Result for 10^2: 0.009600000000
Result for 10^3: 0.114800000000
Result for 10^4: 1.402200000000
Result for 10^5: 16.78920000000
Result for 10^6: 196.5500000000
```

Interesantemente, **C** es bastante mas lento que python. O no, realmente la lentitud se debe a imprimir el resultado en pantalla.

Cambiamos el código a:
```C
int trialDivisionNoPrint(int n){
    if (n <= 1)
    {
        //printf("false\n");
        return 0;  
    } else if (n <= 3)
    {
        //printf("false\n");
        return 0;
    } else
    {
    for(size_t m = 3; m < sqrt(n); m+=2)
        {
            if(n % m == 0)
            {
               //printf("false\n");
               return 0;
            }
        }
    }
    //printf("true\n");
    return 1;
}
```

Mucho mas acorde a lo que se espera de **C**

```
Result for 10^1: 0.000000000000
Result for 10^2: 0.000000000000
Result for 10^3: 0.000000000000
Result for 10^4: 0.001000000000
Result for 10^5: 0.013000000000
Result for 10^6: 0.322000000000
```

Curiosamente el algoritmo tarda aproximadamente 2 horas en procesar 10^9 números
```
==== Test Number 1 ====
Result for 10^1: 0.000000000000
Result for 10^2: 0.000000000000
Result for 10^3: 0.000000000000
Result for 10^4: 0.001000000000
Result for 10^5: 0.013000000000
Result for 10^6: 0.324000000000
Result for 10^7: 8.833000000000
Result for 10^8: 241.773000000000
Result for 10^9: 6793.016000000001
```
