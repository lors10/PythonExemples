
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