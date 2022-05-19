# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:41:40 2022

@author: Guillen
"""


def secuencia(arr:list): # Extrae la secuencia de caracteres removidos en su orden de encriptación
    
    
    #sec = []
    sec = ""
    
    for i in range(len(arr)-1,-1,-1):
        
        #print(arr[i])
        if arr[i] not in sec:
            
            sec = arr[i] + sec
            #sec.insert(0, arr[i])

    return sec
    
    print(sec)
    
    
dicCantidadChar = {}

def conditions(a:list,sec:list): #Solo sirve para ver cuantas letras de cada una debe tener la cadena desencriptada
    
    sec =  '?'+sec
    #print(sec)
    for i in range(1,len(sec)):
        
        dicCantidadChar[sec[i]] = int(a.count(sec[i]))//sec.index(sec[i])
        
        #print(sec.index(sec[i])+1)


    print(dicCantidadChar)
    
    
def decrypt(a:list,sec:list)->list: #desencripta dadas la cadena encriptada y la secuencia de cadenas eliminadas
    n=0
    sec =  "?"+sec
    for i in range(1,len(sec)):
        
        n += int(a.count(sec[i]))/sec.index(sec[i])
    
    print(n)
    
    
    return a[0:int(n)]
    

def comprobar(decrypted:str,sec:str)->str: #Encripta otra vez para comprobar si la cadena encriptada que se leyó es la misma
    
    a = decrypted
    for i in sec:
        
        b = decrypted.replace(i,"")
        a +=b
        decrypted = b
        #print(decrypted)
        #print(a)
    return a
    
    
    
    

if __name__ == '__main__':
    
    
    #a = input()
    #a = "rsrtrsrrrtrrt"
    #a = "mfqmtptmqpitmqmtptmqpitmqmtptmqptqtptqptqttqtttt"
    #a = "ama"
    #a = "qweqeewew"
    #a = "ppuxbdvdmmzbsbmrzjkdxkzxkbhpzpmmupbmz"
    a = "armaramam"
    #print(a.count("t"))
    
    
    #print(secuencia(a))
    
    sec = secuencia(a)
    
    conditions(a, sec)
    
    
    original = decrypt(a, sec)

    checkEncrypt = comprobar(original, sec)
    
    if checkEncrypt != a:
        
        print("NO EXISTE")
    else:
        print(original+" " + sec)
        
    

    