# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 01:55:13 2021

@author: vignesh jaishankar
"""

def printFizzBuzz():
    for num in range(1, 101):

        if num == 1:
            print(num)
            continue    
        
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

      
        if is_prime:
            print("prime ==> ", num)

        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ==> ",num)
        else:
        
            if num % 3 == 0:
                print("Fizz ==>",num)

          
            elif num % 5 == 0:
                print("Buzz ==> ",num)

       
            elif is_prime == False:
                print(num)
            
        
printFizzBuzz()