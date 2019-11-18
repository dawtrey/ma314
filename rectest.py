import time

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

print(iter(500))

start1 = time.time()
print(rec(100))
end1 = time.time()

elapsed1 = end1 - start1
print(elapsed1)

start2 = time.time()
print(iter(10000))
end2 = time.time()

elapsed2 = end2 - start2
print(elapsed2)

print(elapsed2/elapsed1)
