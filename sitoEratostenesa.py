from math import sqrt, floor

def sito(n):
    A = [True]
    for i in range (2,n+1):
        A.append(True)
    
    
    for i in range (2, int(floor(sqrt(n))+1)):
        if (A[i] == True):
            j = i**2
            while (j<n):
                A[j] = False
                j += i
            
    B = []
    for k in range (2,len(A)):
        if A[k] == True:
            B.append(k) 
    return B
    
C = sito(30)
print (C)