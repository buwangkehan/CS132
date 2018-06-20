#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:23:58 2018

@author: wangkehan
"""
import numpy as np
import random

def p35():
    a = np.zeros((5,6))
    b = np.ones((3,5))
    c = np.identity(6)
    d = np.diagflat([3,5,7,2,4])
    print("The answer of a: \n" + str(a))
    print()
    print("The answer of b: \n" + str(b))
    print()
    print("The answer of c: \n" + str(c))
    print()
    print("The answer of d: \n" + str(d))
    print()

def p36():
    matrix1 = np.random.rand(6, 4)
    matrix2 = np.random.randint(-9, 9, size = (3,4))
    print("6x4 matrix with random entries in range [0,1): \n" + str(matrix1))
    print()
    print("3x4 matrix with interger entries between -9 and 9: \n" + str(matrix2))
    print()

def p37():
    for i in range(3):
    
        A = np.random.randint(-9, 9, size = (4,4))
        B = np.random.randint(-9, 9, size = (4,4))
        I = np.identity(4)
        result1 = np.subtract(np.dot(np.add(A,I),np.subtract(A,I)), np.subtract(np.dot(A,A),I))
        result2 = np.subtract(np.dot(np.add(A,B),np.subtract(A,B)),np.subtract(np.dot(A,A),np.dot(B,B)))
        all_zeros = result1.any()
        all_zeros2 = result2.any()
        if not all_zeros:
            print("In Example " + str(i+1) + " random matrix A and Identity matrix I verified the formula (A+B)(A-B) - (A**2 - I) and make the zero matrix")
            print(result1)
        else:
            print("In Example " + str(i+1) + " random matrix A and Identity matrix I fail to verified the formula(A+B)(A-B) - (A**2 - I) and does not make the zero matrix")
            print(result1)
        if not all_zeros2:
            print("In Example " + str(i+1) + " two matrics A and B verified the formula (A+B)(A-B) - (A**2 - B**2) and  make the zero matrix")
            print(result2)      
        else:
            print("In Example " + str(i+1) + " two matrics A and B fail to verified the formula (A+B)(A-B) - (A**2 - B**2) and does not make the zero matrix")
            print(result2)      

        
    
def test():
    print('Problem35: \n')
    p35()
    print('Problem36: \n')
    p36()
    print('Problem37: \n')
    p37()
    


test()