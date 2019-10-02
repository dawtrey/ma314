l = [1,1,1,1,1,2,3,2,1]

def peak(x):
    for i in range(len(x)):
        if l[i] > l[i + 1]:
            return i

print(peak(l))

