# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:41:40 2022

@author: Guillen
"""


def secuencia(arr:list):
    
    
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

def conditions(a:list,sec:list):
    
    sec =  '?'+sec
    #print(sec)
    for i in range(1,len(sec)):
        
        dicCantidadChar[sec[i]] = int(a.count(sec[i]))//sec.index(sec[i])
        
        #print(sec.index(sec[i])+1)


    print(dicCantidadChar)
    
    
def desencript(a:list,sec:list)->list:
    n=0
    sec =  "?"+sec
    for i in range(1,len(sec)):
        
        n += int(a.count(sec[i]))/sec.index(sec[i])
    
    print(n)
    
    
    return a[0:int(n)]
    

    
    

if __name__ == '__main__':
    
    
    #a = ['r','s','r','t','r','s','r','r','r','t','r','r','t']
    #ori = ['r','s','r','t','r','s','r']
    
    #a = "rsrtrsrrrtrrt"
    a = "mfqmtptmqpitmqmtptmqpitmqmtptmqptqtptqptqttqtttt"
    #a = "ama"
    #a = "qweqeewew"
    #a = "ppuxbdvdmmzbsbmrzjkdxkzxkbhpzpmmupbmz"
    #print(a.count("t"))
    
    #print(13-3-8)
    
    #print(len(a))
    #print(len(ori))
    
    #a.remove()
    
    #print(a)
    
    print(secuencia(a))
    
    sec = secuencia(a)
    
    conditions(a, sec)
    print(desencript(a, sec)+" " + sec)
    
    
    #print("hello")

    