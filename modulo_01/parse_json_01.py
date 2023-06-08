import sys
import string
import json

with open('/home/dudu/Desktop/Recon/modulo_01/json/json_basico.json') as json_file: #with open() mais performático, não precisa dar close().
    jsondata = json.load(json_file) #json.load Deserializa um arquivo no formato JSON para um arquivo.
    #print(jsondata['Key1']) acessar key1
    for i in jsondata:
        print(i,jsondata[i]) #muito usado para printar json complexos.
        