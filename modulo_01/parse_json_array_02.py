import sys
import string
import json

with open('/home/dudu/Desktop/Recon/modulo_01/json/json_strings.json') as json_file:
    jsondata = json.load(json_file) 
    for i in jsondata:
        print(i,jsondata[i].split(' ')[2]) #split para quebrar a strings e delimitar apenas por um resultado

with open('/home/dudu/Desktop/Recon/modulo_01/json/json_number.json') as json_number:
    jsondata = json.load(json_number)
    for i in jsondata:
        print(i,jsondata[i]) #conseguimos ler números normalmente.