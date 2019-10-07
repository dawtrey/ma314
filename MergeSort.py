def Merge(left, right):
    leftIndex, rightIndex = 0, 0
    result = []
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

    result += left[leftIndex:]
    result += right[rightIndex:]
    return result


def MergeSort(A):
	# base case, list of length 1 is sorted
    if len(A) <= 1:  
        return A

    # divide list in half and sort recursively
    m = len(A) // 2
    left = MergeSort(A[:m])
    right = MergeSort(A[m:])

    return Merge(left, right)
    

A = [6,4,3,8,1,5,2,7]
print(MergeSort(A))
