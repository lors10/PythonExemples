
# un 'valore' è uno degli elementi di base che un programma è in grado di elaborare

# un 'tipo' rappresenta una categoria di valori

# una 'variabile' è un nome che fa riderimento ad un valore

# un'istruzione di assegnazione serve a creare una nuova variabile, specificando il nome e assegnando un valore.
# i 'nomi' possono essere lunghi a piacere e possono contenere sia lettere che numeri, ma non possono iniziare con un numero.
# per i 'nomi di variabili' è conveniente usare solo lettere minuscole.
# per i nomi l'uso di lettere minuscole o maiscole sono diversi.
# il trattino basso o underscore (_), può far parte di un nome.

# esempi:

n = 10

messaggio = 'Ciao'

MESSAGGIO = 'come stai?'

il_mio_nome = 'Lorenzo!'

#1cognome = 'Salvi' # Error

print(n, messaggio, MESSAGGIO, il_mio_nome)


# stringhe
#
# una stringa è una sequenza di caratteri
# è possibile accedere ai singoli caratteri usando le parentesi quadre []
#
# funzione 'len': è una funzione predefinita che restituisce il numero di caratteri contenuti in una stringa
#
# ciclo for per eseguire un'attraversamento di una stringa
#
# slicing: per poter selezionare un pezzo (slice) di una stringa. ATTENZIONE AGLI INDICI
#
# esempio: Ciao --- Gli indici sono 0 'C' 1 'i' 2 'a' 3 'o' 4
#
# metodi delle stringhe
# metodo 'upper': prende una stringa e crea una stringa con lettere maiscole
# metodo 'find': per cercare una lettera specifica all'interno di una parola
#
# operatore 'in': è un operatore booleano che confronta due stringhe e restituisce True se la prima è una sottostringa della seconda
#



# esempi

frutto = 'Banana'

letteraMaiuscola = frutto[0]
letteraMinuscola = frutto[1]

print(letteraMaiuscola + ' ' + letteraMinuscola)    # stampa: B a
print(len(frutto))  # stampa 6

lunghezzaStringa = len(frutto)
ultimaLettera = frutto[lunghezzaStringa-1]  # corrisponde a frutto[5]

print(ultimaLettera)    # stampa: a

for lettera in frutto:
    print(lettera)      # stampa: B a n a n a


stringaEsempio = 'New York'

print(stringaEsempio[0:3])      # stampa: New
print(stringaEsempio[4:8])      # stampa York

print(stringaEsempio.upper())   # stampa: NEW YORK

print(frutto.find('a'))     # stampa: 1

print('a' in frutto)    # stampa: True
print('ca' in frutto)   # stampa: False



