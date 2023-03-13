import json
import re
import random

#def _get_schedulable_node(v1_client):
#    node_list = _get_ready_nodes(v1_client)
#    if not node_list:
#        return None
#    available_nodes = list(set(node_list))
#    return random.choice(available_nodes)



def _get_ready_nodes():

    ready_nodes = ["docker-desktop", "slave-one", "slave-two"]

    return ready_nodes

node_list = _get_ready_nodes()     #node_list = ['docker-desktop', 'slave-one', ''slave-two]
#print(node_list[0])        stampa: docker desktop
#print(node_list[1])        stampa: slave-one
#print(node_list[2])        stampa: slave-two

avalaible_node = list(set(node_list))  #available_node = [''slave-two', 'slave-one', 'docker-desktop']
#print(avalaible_node)

#random_node = random.choice(avalaible_node)
#print(random_node)

# apro il file json
read_file = open('file.json')

# restituisco l'oggetto json come dizionario
data = json.load(read_file)

# stampo il valore riferito al campo specificato
#print(data['datetime'])
#print(data['pod-name'])
#print(data['node-name'])

# chiudo il file
read_file.close()

# estraggo i valori dei nodi in available_node e faccio un matching
# con il valore del campo node-name estratto dal dizionario data in
# riferimento ai campi del file jsos
specific_node = [item for item in avalaible_node
                     if re.search(data['node-name'], item) is not None]

print(specific_node)        # stampa: ['docker-desktop']

# trasformo oggetto in stringa
node = " ".join(specific_node)
print(node)     # stampa: docker-desktop

def _get_schedulable_node():

    node_list = _get_ready_nodes()  # array
    if not node_list:
        return None

    avalaible_node = list(set(node_list)) # array ordinato

    return