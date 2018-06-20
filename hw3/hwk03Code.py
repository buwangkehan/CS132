import numpy as np

def innerProduct(a,b):
    """
    Takes two vectors a and b, of equal length, and returns their inner product
    """
    inner = 0 #initial varaiable return at end
    for i in range(len(a)):# run through each entry in the vector
        inner += a[i] * b[i] # multiply one entry from a to another b
    return inner # return the final result

def AxIP(A,x):
    """
    Takes a matrix A and a vector x and returns their product
    """
    result = np.zeros(len(A)) # creating a new array(same size with A)
    for i in range(len(A)): # run through each row of the martix A
        result[i] = innerProduct(A[i,:], x) #using innerProduct method get the inner product of ith row and vector, and put it to ith position of array 
    return result # return the final result
    

def AxVS(A,x):
    """
    Takes a matrix A and a vector x and returns their product
    """
    result = np.zeros(len(A)) # creating a new array(same size with A)
    for i in range(len(x)):# run through each column
        result += x[i] * A[:,i] # multiply column, put it into array
    return result # return the final result



