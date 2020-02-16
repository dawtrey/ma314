# 34877
def Recurrence(n): 
    A = [0.5]
    if n == 1:
        return 1
    else:
        for i in range(n):            
            A.append(A[i]+A[(i+1)//2])
        return int(A[n])

print(Recurrence(500))
