def recursive_range(n):
    if n == 0:
        return []
    return recursive_range(n-1) + [n-1]


def maxUnimodal(A):
  #create list that should have one element if unimodal and more than two if not
  B = []
  l = len(A)
  for i in recursive_range(l-1):
    if A[i-1] <= A[i] and A[i] >= A[i+1]:
      B.append(i)
  if A[0] >= A[1]:
    B.append(0)
  elif A[l-1] >= A[l -2]:
    B.append[l-1]
  elif len(B) >= 2:
    return None
  return B[0]

C = (1,2,3,2)
  
print(maxUnimodal(C))
