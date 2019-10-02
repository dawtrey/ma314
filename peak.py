l1 = [1,1,1,1,1,2,3,2,1]
l2 = [3, 2, 1]
l3 = [1,2,3,4,5]

def peak(x):
    short = len(x) -1 
    for i in range(short):
        if x[i] > x[i + 1]:
            return i
        else: return short 

print("The peak is at index: " + str(peak(l1)))
print("The peak is at index: " + str(peak(l2)))
print("The peak is at index: " + str(peak(l3)))
