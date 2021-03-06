def swapRows(A, i, j):
    """
    interchange two rows of A
    operates on A in place
    """
    tmp = A[i].copy()
    A[i] = A[j]
    A[j] = tmp

def relError(a, b):
    """
    compute the relative error of a and b
    """
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        try:
            return np.abs(a-b)/np.max(np.abs(np.array([a, b])))
        except:
            return 0.0

def rowReduce(A, i, j, pivot):
    """
    reduce row j using row i with pivot pivot, in matrix A
    operates on A in place
    """
    factor = A[j][pivot] / A[i][pivot]
    for k in range(len(A[j])):
        # we allow an accumulation of error 100 times larger 
        # than a single computation
        # this is crude but works for computations without a large 
        # dynamic range
        if relError(A[j][k], factor * A[i][k]) < 100 * np.finfo('float').resolution:
            A[j][k] = 0.0
        else:
            A[j][k] = A[j][k] - factor * A[i][k]

# stage 1 (forward elimination)
def forwardElimination(B):
    """
    Return the row echelon form of B
    """
    A = B.copy()
    m, n = np.shape(A)
    for i in range(m-1):
        # Let lefmostNonZeroCol be the position of the leftmost nonzero value 
        # in row i or any row below it 
        leftmostNonZeroRow = m
        leftmostNonZeroCol = n
        ## for each row below row i (including row i)
        for h in range(i,m):
            ## search, starting from the left, for the first nonzero
            for k in range(i,n):
                if (A[h][k] != 0.0) and (k < leftmostNonZeroCol):
                    leftmostNonZeroRow = h
                    leftmostNonZeroCol = k
                    break
        # if there is no such position, stop
        if leftmostNonZeroRow == m:
            break
        # If the leftmostNonZeroCol in row i is zero, swap this row 
        # with a row below it
        # to make that position nonzero. This creates a pivot in that position.
        if (leftmostNonZeroRow > i):
            swapRows(A, leftmostNonZeroRow, i)
        # Use row reduction operations to create zeros in all positions 
        # below the pivot.
        for h in range(i+1,m):
            rowReduce(A, i, h, leftmostNonZeroCol)
    return A

#################### 

# If any operation creates a row that is all zeros except the last element,
# the system is inconsistent; stop.
def inconsistentSystem(A):
    """
    B is assumed to be in echelon form; return True if it represents
    an inconsistent system, and False otherwise
    """
    m, n = np.shape(A)
    for i in range(m):
        for j in range(n):
            if(A[i][j] != 0):
                if(j == n-1):
                    return True
                else:
                    break
    return False
        
    


def backsubstitution(B):
    """
    return the reduced row echelon form matrix of B
    """
    A = B.copy()
    m, n = np.shape(A)
    A = A.astype(float)
    for i in range(m-1, -1, -1):#bottom right
        pivot = 0.0 # creat variable pivot which help define the pivot of each row
        for j in range(n): #column
            if pivot == 0.0:
                if A[i][j] != 0:
                    pivot = A[i][j] #give pivot a value
            if pivot != 0.0: #pivot can not be 0
                A[i][j] = A[i][j] / pivot
    
    for i in range(m-1,0,-1):
        for j in range(0, n-1):
            if A[i][j] == 1:
                for k in range(i-1, -1, -1):
                    rowReduce(A, i, k, j)
    return A
            






#####################
import numpy as np
import warnings
import scipy.linalg

A = np.array([[0,13,8,4],[4,9,8,4],[8,6,12,8],[0,5,0,-4]])

eigVals = np.linalg.eigvals(A)

B = np.subtract(A, (1*np.eye(4,4)))
zeros = np.zeros((4,1))
afterappend = np.append(B, zeros,axis=1)

C = forwardElimination(afterappend)
D = backsubstitution(C)



    
    