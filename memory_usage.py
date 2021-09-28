import psutil
import json


def get_mem_data():
    mem = psutil.virtual_memory()
    total_mem=(((mem.total/1024)/1024)/1024)
    available_mem=(((mem.available/1024)/1024)/1024)
    used_mem=(((mem.used/1024)/1024)/1024)
    return total_mem,available_mem,used_mem

def show_mem_data():
    x,y,z=get_mem_data()
    dict2 = {
        "MEMORY USAGE":{
            "Total Memory":"",
            "Total Available Memory":"",
            "Total Used Memory":""
        }
    }
    
    dict2["MEMORY USAGE"]["Total Memory"]=str(x)+" GB"
    dict2["MEMORY USAGE"]["Total Available Memory"]=str(y)+" GB"
    dict2["MEMORY USAGE"]["Total Used Memory"]=str(z)+" GB"

    mem_out=json.dumps(dict2,indent=4)
    return mem_out

out = show_mem_data()
print(out)


    
