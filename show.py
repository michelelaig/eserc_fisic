from numpy import *
import math
import matplotlib.pyplot as plt

t = linspace(0, 2*math.pi, 400)
a = math.pi/2+sin(t)
b = math.pi/2+sin(12*t)
c = a + b
plt.grid()
plt.plot(t, a, 'r') # plotting t, a separately 
plt.plot(t, b, 'b') # plotting t, b separately 
#plt.plot(t, c, 'g') # plotting t, c separately 
plt.show()

'''
Certo, ecco una possibile implementazione:

```python
import matplotlib.pyplot as plt
import numpy as np

def plot_sine_cosine():
    x = np.linspace(0, 2*np.pi, 100)  # generiamo 100 punti sull'intervallo [0, 2*pi]
    y_sin = np.sin(x)  # valori del seno di x
    y_cos = np.cos(x)  # valori del coseno di x

    plt.plot(x, y_sin, label='sin(x)')  # grafico del seno
    plt.plot(x, y_cos, label='cos(x)')  # grafico del coseno

    plt.xlabel('x')  # etichetta sull'asse x
    plt.ylabel('y')  # etichetta sull'asse y
    plt.title('Sine and cosine functions')  # titolo del grafico

    plt.legend()  # mostra la legenda con i nomi delle funzioni

    plt.show()  # mostra il grafico a video
```

La funzione `plot_sine_cosine` usa il modulo `numpy` per generare un array `x` di 100 punti sull'intervallo `[0, 2*pi]`. Poi calcola il seno e il coseno di ciascun punto e li salva in due array `y_sin` e `y_cos`. Infine disegna i due grafici sovrapposti con `plt.plot` e mostra il risultato con `plt.show()`. La legenda con i nomi delle funzioni viene creata con `plt.legend()`.

Per chiamare questa funzione basta scrivere:

```python
plot_sine_cosine()
```

e verrà visualizzato il grafico delle due funzioni.
'''

