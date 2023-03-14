import json
import re
import random
import time

#def _get_schedulable_node(v1_client):
#    node_list = _get_ready_nodes(v1_client)
#    if not node_list:
#        return None
#    available_nodes = list(set(node_list))
#    return random.choice(available_nodes)



def _get_ready_nodes():

    ready_nodes = ["docker-desktop", "slave-one", "slave-two"]

    return ready_nodes

#node_list = _get_ready_nodes()     #node_list = ['docker-desktop', 'slave-one', ''slave-two]
#print(node_list[0])        stampa: docker desktop
#print(node_list[1])        stampa: slave-one
#print(node_list[2])        stampa: slave-two

#avalaible_node = list(set(node_list))  #available_node = [''slave-two', 'slave-one', 'docker-desktop']
#print(avalaible_node)

#random_node = random.choice(avalaible_node)
#print(random_node)

# apro il file json
#read_file = open('folder/file.json')

# restituisco l'oggetto json come dizionario
#data = json.load(read_file)

# stampo il valore riferito al campo specificato
#print(data['datetime'])
#print(data['pod-name'])
#print(data['node-name'])

# chiudo il file
#read_file.close()

# estraggo i valori dei nodi in available_node e faccio un matching
# con il valore del campo node-name estratto dal dizionario data in
# riferimento ai campi del file jsos
#specific_node = [item for item in avalaible_node
#                     if re.search(data['node-name'], item) is not None]

#print(specific_node)        # stampa: ['docker-desktop']

# trasformo oggetto in stringa
#node = " ".join(specific_node)
#print(node)     # stampa: docker-desktop

def _get_schedulable_node():

    node_list = _get_ready_nodes()  # array
    if not node_list:
        return None

    avalaible_node = list(set(node_list))   # array ordinato

    read_file = open('folder/file.json')    # apro file.json
    data = json.load(read_file)     # restituisco l'oggetto json come dizionario
    read_file.close()   # chiudo file.json

    specific_node = [item for item in avalaible_node
                    if re.search(data['node-name'], item) is not None]

    node = " ".join(specific_node)  # trasformo oggetto in stringa

    #time.sleep(60)  # timer di 60 sec

    return node


print(_get_ready_nodes())   # stampa: ['docker-desktop', 'slave-one', 'slave-two']
print(_get_schedulable_node())  # stampa: docker-desktop

#####################

# per leggere il contenuto di un file e
# sovrascriverlo successivamente

# legge il contenuto del file
read_data = open('folder/podname.txt', 'r')
print(read_data.read())
read_data.close()

# sovrascrive il nuovo contenuto nello stesso file
new_pod_name = "annotation-second-scheduler-four"
write_data = open('folder/podname.txt', 'w')
write_data.write(new_pod_name)
write_data.close()

read_data = open('folder/podname.txt', 'r')
print(read_data.read())

#####################

# per aprire due file e copiare il contenuto di uno nell'altro

# per aprire i due file
with open('folder/file.json', 'r') as firstfile, open('templates/data.json', 'w') as secondfile:

    # legge il contenuto dal primo file
    for line in firstfile:
        # copia il contenuto nel secondo file
        secondfile.write(line)


