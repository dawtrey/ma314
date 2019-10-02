l = [1,1,1,1,1,2,3,2,1]

def peak(x):
    a = x[0] - 1
    z = x[-1] - 1
    m = [a] + x + [z]  
    for i in range(len(m)):
        if m[i] > m[i + 1]:
            return i
    

print(peak(l))

