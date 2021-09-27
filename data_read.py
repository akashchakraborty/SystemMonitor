import json


def read_data():
    f=open("data.json","r")
    out=f.read()
    print(out)
