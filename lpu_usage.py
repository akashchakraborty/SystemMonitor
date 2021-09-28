import psutil
import sys
import os
import json


def get_lpu_freq():
    data=psutil.cpu_freq(percpu=True)
    lpu1f=data[0][0]
    lpu2f=data[0][1]
    lpu3f=data[0][2]
    return lpu1f,lpu2f,lpu3f

def get_lpu_usage():
    dictCPU={
        "CPU USAGE":{
        "Logical Processor 1":{
            "User Utilization":"",
            "System Utilization":"",
            "Idle":"",
            "Interrupts":"",
            "DPC":""},
        "Logical Processor 2":{
            "User Utilization":"",
            "System Utilization":"",
            "Idle":"",
            "Interrupts":"",
            "DPC":""},
        "Logical Processor 3":{
            "User Utilization":"",
            "System Utilization":"",
            "Idle":"",
            "Interrupts":"",
            "DPC":""},
        "Logical Processor 4":{
            "User Utilization":"",
            "System Utilization":"",
            "Idle":"",
            "Interrupts":"",
            "DPC":""}
    },
        "CPU FREQUENCY":
        {
            "Current Frequency":"",
            "Max Frequency":"",
            "Min Frequency":""
        }
    }
    f1,f2,f3= get_lpu_freq()
    data = (psutil.cpu_times_percent(interval=2, percpu=True))
    # LPU 1 Data
    lpu1=data[0]
    uu1=data[0][0]
    su1=data[0][1]
    ii1=data[0][2]
    int1=data[0][3]
    dpc1=data[0][4]
    dictCPU["CPU USAGE"]["Logical Processor 1"]["User Utilization"]=str(uu1) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 1"]["System Utilization"]=str(su1) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 1"]["Idle"]=str(ii1) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 1"]["Interrupts"]=str(int1) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 1"]["DPC"]=str(dpc1) + " %"
    
    # LPU 2 Data
    lpu2=data[0]
    uu2=data[1][0]
    su2=data[1][1]
    ii2=data[1][2]
    int2=data[1][3]
    dpc2=data[1][4] 
    dictCPU["CPU USAGE"]["Logical Processor 2"]["User Utilization"]=str(uu2) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 2"]["System Utilization"]=str(su2) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 2"]["Idle"]=str(ii2) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 2"]["Interrupts"]=str(int2) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 2"]["DPC"]=str(dpc2) + " %"

    # LPU 3 Data
    lpu3=data[2]
    uu3=data[2][0]
    su3=data[2][1]
    ii3=data[2][2]
    int3=data[2][3]
    dpc3=data[2][4]
    dictCPU["CPU USAGE"]["Logical Processor 3"]["User Utilization"]=str(uu3) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 3"]["System Utilization"]=str(su3) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 3"]["Idle"]=str(ii3) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 3"]["Interrupts"]=str(int3) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 3"]["DPC"]=str(dpc3) + " %"
    
    # LPU 4 Data
    lpu4=data[3]
    uu4=data[3][0]
    su4=data[3][1]
    ii4=data[3][2]
    int4=data[3][3]
    dpc4=data[3][4]
    dictCPU["CPU USAGE"]["Logical Processor 4"]["User Utilization"]=str(uu4) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 4"]["System Utilization"]=str(su4) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 4"]["Idle"]=str(ii4) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 4"]["Interrupts"]=str(int4) + " %"
    dictCPU["CPU USAGE"]["Logical Processor 4"]["DPC"]=str(dpc4) + " %"


    dictCPU["CPU FREQUENCY"]["Current Frequency"]=str(f1)+ " MHz"
    dictCPU["CPU FREQUENCY"]["Min Frequency"]=str(f2)+ " MHz"
    dictCPU["CPU FREQUENCY"]["Max Frequency"]=str(f3)+ " MHz"
    json_out = json.dumps(dictCPU,indent=4)
    # print(json_out)
    # # Writing to data.json
    # f=open("lpu_data.json", "w")
    # f.write(json_out)
    return(json_out)
