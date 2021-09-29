from lpu_usage import get_lpu_usage
import psutil
import sys
import os
import json

count = 0
count = psutil.cpu_count()


def get_lpu_freq():
    global count
    print(count)
    # data=psutil.cpu_freq(percpu=True)
    # lpu1f=data[0][0]
    # lpu2f=data[0][1]
    # lpu3f=data[0][2]
    # return lpu1f,lpu2f,lpu3f
get_lpu_freq()