# -*- coding: utf-8 -*-
import random;

class salsaDao:
    def __init__(self):
        self.roma = 0;
        
        
    def devolverPalabra(self,string):
        i = random.randrange(0,len(string))
        h = i
        juan =string[i:i+1]
        if(juan.isalpha()):
            while(string[h:h+1].isalpha() and h >=0):
                h= h-1
                
                while(string[i:i+1].isalpha()and i<len(string)):
                    i= i+1
                    
                
                return string[h+1:i]
            
        else:
            while(string[i:i+1].isalpha()==False and i <len(string)):
                i= i+1
                
            if(i!=len(string)):
                h = i+1;
                while(string[h:h+1].isalpha()and h <len(string)):
                    h=h+1
            return string[i:h]
                
                
                  
                        
    
                
                
            