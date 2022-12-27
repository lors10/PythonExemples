import random
import re


#ready_nodes = ["control-plane", "slave-one", "slave-two"]
#print(ready_nodes[0])
#print(ready_nodes[1])
#print(ready_nodes[2])

def _get_ready_nodes():
    ready_nodes = ["control-plane", "slave-one", "slave-two"]

    return ready_nodes


def _get_schedulable_node():
    node_list = _get_ready_nodes()

    #print(node_list[0])
    if not node_list:
        return None
    available_nodes = list(set(node_list))

    #print(available_nodes)

    specific_node = [item for item in available_nodes
                     if re.search("control-plane", item) is not None]

    #my_string = " ".join(my_sentence)

    node = " ".join(specific_node)

    return node


print(_get_ready_nodes())
print(_get_schedulable_node())