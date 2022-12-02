
# istruzione condizionale 'if'
#
# forma:
# if (condizione_booleana):
#       condizione vera
# else:
#       condizione falsa


# esecuzione semplificata
#
# forma:
# if (condizione_booleana):
#       condizione vera


# condizione in serie
#
# forma:
# if (condizione1):
#       cond1
# elif (condizione2):
#       cond2
# elif (condizione3):
#       cond3


# esempio

x = 7

if (x > 10):
    print('Vero ', x, ' è maggiore di 10')
else:
    print('Falso ', x, ' è minore di 10')

x = 15

if (x > 15):
    print('Sono nel caso 1')
elif (x == 15):
    print('Sono nel caso 2')
elif (x < 15):
    print('Sono nel caso 3')



# funzioni ricorsive: cioè una funzione può richiamare se stessa

# esempio

def contoArovescia(n):
    if n <= 0:
        print('Via!')
    else:
        print(n)
        contoArovescia(n - 1)


print(contoArovescia(5)) # stampa 5, 4, 3, 2, 1, Via!


# funzioni produttive
#
# funzioni che restituiscono un valore (tramite return)

# esempio

import math

def area(raggio):
    a = math.pi * raggio**2

    return a    # con il return in fase di runtime non verrà restituito 'None' ma il valore della variabile che passo

print(area(10))     # stampo 314.159...

