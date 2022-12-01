
# chiamata di funzione
#
# esempio: type(42)
# l'espressione tra parentesi è chiamata 'argomento della funzione'
# type è il 'nome' della funzione
# il risultato della funzione è chiamato 'valore di ritorno'

print(type(42)) # stampa il tipo di valore dell'argomento


# funzioni matematiche
#
# un 'modulo' è un file che contiene una raccolta di funzioni correlate
# prima di poter usare le funzioni di un modulo, le dobbiamo importare tramite l'istruzione 'import'
# l'oggetto modulo contiene le funzioni e le variabili definite all'interno del modulo stesso.
# per accedere a una funzione del modulo, bisogna specificare, nell'ordine, il nome del modulo e il nome della funzione
# separati da un punto (notazione a punto)

import math

gradi = 45
radianti = gradi / 180.0 * math.pi
print(math.sin(radianti)) # stampa 0.7071067811865475


# definizione di una funzione
#
# permette di specificare il nome di una nuova funzione e la serie di istruzioni che viene eseguita quando la funzione viene chiamata
# 'def' è la parola chiave per la definizione di una nuova funzione
# il nome è stampa_brani
# le parentesi vuote indicano che la funzione non accetta alcun argomento


# esempio

def stampa_brani():
    print('Terror di tutta la foresta egli è,')
    print("Con l'ascia in mano si sente un re.")


#print(stampa_brani())  # stampa:
                            # Terror di tutta la foresta egli è,
                            # Con l'ascia in mano si sente un re.

def ripeti_brani():
    stampa_brani()
    stampa_brani()

#print(ripeti_brani())  # stampa:
                            # Terror di tutta la foresta egli è,
                            # Con l'ascia in mano si sente un re.
                            # Terror di tutta la foresta egli è,
                            # Con l'ascia in mano si sente un re.


# parametri e argomenti
#
# i 'parametri' sono gli argomenti che vengono passati alla funzione
#

# esempio

def stampa2volte(stringa):
    print(stringa)
    print(stringa)


#print(stampa2volte('Ciao'))    # stampa:
                                    # Ciao
                                    # Ciao

#print(stampa2volte('ciao'*2))  # stampa
                                    # ciaociao
                                    # ciaociao

#print(stampa2volte('Pippo' + 'Pluto'))     # stampa:
                                                # PippoPluto
                                                # PippoPluto


# quando create una variabile in una funzione, essa è locale, cioè esiste solo all'interno della funzione.

# esempio

cat = 'Ciao'    # variabile cat con scope globale

def cat2volte(parte1, parte2):
    cat = parte1 + parte2  # variabile cat con scope locale
    stampa2volte(cat)

var1 = 10
var2 = 20

stringa_uno = 'Lorenzo'
stringa_due = 'Salvi'

print(cat2volte(var1,var2))     # stampa:
                                    # 30
                                    # 30

print(cat2volte(stringa_uno, stringa_due))      # stampa:
                                                    # LorenzoSalvi
                                                    # LorenzoSalvi

print(cat)  # stampa: Ciao





