# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:41:40 2022

@author: Guillen
"""

import random
import time
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
    
def crearCadena(decrypted:str)->str: #Encripta Una cadena en orden de caracteres arbitrarios como hace el enunciado.
    a = decrypted
    i = 0
    while i != len(decrypted) and len(decrypted) > 0:
         n = random.randint(0,len(decrypted)-1)
         c = decrypted[n]
         b = decrypted.replace(c,"")
         a +=b
         decrypted = b
         i +=1
    return a
    
    

if __name__ == '__main__':
    
    start = time.time()

    #a = input()
    #a = "rsrtrsrrrtrrt"
    #a = "mfqmtptmqpitmqmtptmqpitmqmtptmqptqtptqptqttqtttt"
    #a = "ama"
    #a = "qweqeewew"
    #a = "ppuxbdvdmmzbsbmrzjkdxkzxkbhpzpmmupbmz"
    #a = "armaramam"
    #a = "pneumonoultramicroscopicsilicovolcanoconiosispnemonoltramicroscopicsilicovolcanoconiosispnemonoltramicrocopicilicovolcanoconioipnemnltramicrcpicilicvlcancniinemnltramicrcicilicvlcancniinemnltramcrcclcvlcancnnemnltrmcrcclcvlcncnnemnltmccclcvlcncnnemnltmlvlnnemltmlvleltlvleltllete"
    
    #a = crearCadena(input())
    
    with open('encriptado135kchars.txt', 'r+') as f: # Para testear la palabra encriptada correcta
        a = f.read()
    
    # with open('encriptado135kcharsNOEXISTE.txt', 'r+') as f: #Para testear la palabra encriptada incorrecta. Se le agregó solo un caracter, deberia dár incorrecto (NO EXISTE).
    #     a = f.read()
    
        f.close()
    
    
    
    #print(secuencia(a))
    #for i in range(1000):
        
    sec = secuencia(a)
    
    conditions(a, sec)
    
    
    original = decrypt(a, sec)
    with open('original10kchars.txt', 'w') as f:
        f.write(original+" "+ sec)
        f.close()
        checkEncrypt = comprobar(original, sec)
    
    if checkEncrypt != a:
        
        print("NO EXISTE")
    else:
        print(original+" " + sec)
    
    end = time.time()
    
    final = str(end-start)
    print(str("TIME: "+final))
    #print(crearCadena("pneumonoultramicroscopicsilicovolcanoconiosis"))
    #b = "ewbyagjnbfcypkcytgnkqwmcfztrnocfexpepxpdemnzwguzwgmmqauolduemzeuncdrpviinaelzidqpnkasvwbpisldepamfvjzzknqvjyrvbyytmlvsohktturbdabofnmmwndqmrcwrnnmdhywatvscxpelflujckcpjziotqtpgzamdczmyvzexajejrqymiuemrwbtywiuukpkihchrmsjwmozojxymsaygjrsdohioijjhtvjrrjpvefwnxdwrmowxsqamcyhykjdexeqqgchhvadtnzvljrfmgbplydvgpmioibvpsmsdukoorixmcynnxikudhngqmjyviarmyntelgtybmpvvnlbnbuslrdfjlotqqgrhkjayunywkkpqhtckaxlovlhytidzlxllsxsdvlmjkcydmvivkcnoyvsmavsbhkunfibmcnkxjvqlfmnlvdhlvhgkoxndqesemvfccfvhzyasbkvmcchwjgtlz"
    
    
    
    
    

    