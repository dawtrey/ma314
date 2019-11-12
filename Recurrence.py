def rec(i):
  if i == 1: return 1
  return rec(i-1) + rec(i // 2) 

print(rec(100))


def iter(n): 
    A = [0.5]
    if(n == 1):
        return 1
    else:
        for i in range(n):            
            A.append(A[i]+A[(i+1)//2])
        return int(A[n])

print(iter(100))
