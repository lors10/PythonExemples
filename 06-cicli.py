
# ciclo while
#
# forma:
# while (condizione):
#       evento
#
# in modo più formale, questo è il flusso di esecuzione di un'istruzione while:
# 1. determina se la condizione è vera (True) o falsa (False)
# 2. se la condizione è falsa, esce dal ciclo while e continua l'esecuzione della prima istruzione successiva
# 3. se la condizione è vera, esegue il blocco di istruzioni nel corpo del ciclo while e vi rimaene, ritrnando al punto 1

# esempio

def contoallarovescia(n):
    while (n > 0):
        print(n)
        n = n - 1


#contoallarovescia(3)   # stampo: 3, 2, 1
#print('Via!')


# istruzione break: per interrompere l'esecuzione di un flusso nel bel mezzo del corpo

def noncontareuno(n):
    while(n > 0):
        print(n)
        n = n - 1

        if (n == 1):
            break   # esco dal ciclo while

noncontareuno(5)    # Stampo: 5, 4, 3, 2

print('Via!')


# ciclo for
#
# permette di eseguire un'attraversamento (ad esempio di stringhe)
# forma
# for 'sottostringa' in 'stringa':
#       condizione


def niente_e(stringa, lettera):

    lunghezzaStringa = len(stringa)
    #lettera = 'o'
    i = 0

    valoreReturn = True

    while (i <= (lunghezzaStringa-1)):

        if (stringa[i] != lettera):

            print(stringa[i])

            valoreReturn = True
        else:

            print('La lettera ' + lettera + ' è presente nella parola: ' + stringa)
            valoreReturn = False
            break

        i = i + 1


    print(valoreReturn)


niente_e('amido','o')

# istruzione try per gestire eccezioni
# si comincia con l'eseguire la clausola try. Se tutto va bene, tralascia la clausola except e procede.
# se si verifica un'eccezione, salta fuori dalla clausola try e va ad eseguire la clausola execpt
# forma:
# try:
#   condizione
# except:
#   condizione





