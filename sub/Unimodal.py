# 34877

def maxUnimodal(A):
    B = []
    l = len(A)
    for i in range(l-2): 
        if A[i] <= A[i+1] and A[i+1] > A[i+2]:
            B.append(i+1)
    if A[0] > A[1]: 
        B.append(0)
    if A[l-1] >= A[l -2]:
        B.append(l-1)
    if len(B) >= 2: 
        return None
    return B[0] 

A = [2,2,1,1]
print(A)
iA = maxUnimodal(A)
if iA == None:
    print("is not unimodal.")
else:
    print("is unimodal. Maximum is at index", iA)

B = [0,2,5,8,8]
print(B, maxUnimodal(B))

C = [2,2,1,1]
print(C, maxUnimodal(C))

Z = [4,5,2,3]
print(Z, maxUnimodal(Z))
