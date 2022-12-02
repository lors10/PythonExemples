
# "un'espressione" è una combinazione di valori, variabili e operatori.

# "un'istruzione" è una porzione di codice che l'interprete python può eseguire e che ha un effetto.

# esempio

n = 17 # istruzione di assegnamento

print(n) # istruzione di stampa


#
# ordine delle operazioni aritmetiche
#
# parentesi: hanno il livello di precedenza più elevato
# elevamento a potenza (**): ha la priorità successiva
# moltiplicazione e divisione: hanno la priorità superiore ad addizione e sottrazione
# operatori con la stessa priorità: vengono valutati da sx a dx


# operazioni sulle stringhe
#
# in generale non è possibile effettuare operazioni matematiche su stringhe.
# operatori importanti:
# '+': esegue il concatenamento
# '*': esegue la ripetizione

# esempi:

parola_uno = 'Sono'
parola_due = 'una'
parola_tre = 'stringa'

print(parola_uno + ' ' + parola_due + ' '+ parola_tre) # stampa: Sono una stringa
print(parola_uno *3) # stampa SonoSonoSono

# operatori di divisione intera e modulo
# // è l'operatore di divisione intera: divide due numeri e arrotonda il risultato all'interno inferiore
# % è l'operazione di modulo: che restituisce il resto dell'operazione di divisione tra due numeri interi

# esempio

minuti = 105
ore1 = minuti / 60
ore2 = minuti // 60

print(minuti, ' minuti in ore, sono: ', ore1) # stampa: '105 minuti in ore, sono: 1,75'
print(minuti, ' minuti in ore, sono: ', ore2, '(con operazione di div. intera)') # stampa: '105 minuti in ore, sono: 1 (con operazione di div. intera)'

# esempio

resto = minuti % 60

print(resto)    # stampa 45


# espressioni booleane: sono espressioni che possono valere 'vero' o 'falso'
# gli operatori sono: '==', '!=', '>', '>=', '<', '<='

print(5 == 5)   # True
print(5 == 7)   # False
print(16 > 5)   # True

# operatori logici
# sono 'and', 'or', 'not'





