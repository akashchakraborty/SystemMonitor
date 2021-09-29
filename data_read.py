import json
from lpu_usage import get_lpu_usage
from memory_usage import show_mem_data

def read_data():

    #Memory Usage
    memdata = show_mem_data()
    memdict=json.loads(memdata)

    




    #Total Memory
    print("Total Memory: {}".format(memdict["MEMORY USAGE"]["Total Memory"]))
    #Memory In USe
    print("In Use Memory: {}".format(memdict["MEMORY USAGE"]["Total Used Memory"]))
    #Available Memory
    print("Aailable Memory: {}".format(memdict["MEMORY USAGE"]["Total Available Memory"]))
    

read_data()