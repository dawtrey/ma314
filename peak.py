l1 = [1,1,1,1,1,2,3,2,1]
l2 = [3, 2, 1]
l3 = [1,2,3,4,5]

def peak(x):
    short = len(x) -1
    shorter = len(x) - 2
    if x[0] > x[1]:
        return 0
    else:
        for i in range(shorter):
        
            if x[i+1] >= x[i + 2] and x[i] <= x[i + 1]
                return i
            else: return short
   
        
print("The peak is at index: " + str(peak(l1)))
print("The peak is at index: " + str(peak(l2)))
print("The peak is at index: " + str(peak(l3)))
