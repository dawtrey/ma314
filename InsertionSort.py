# InsertionSort
def InsertionSort(A):
	for i in range(1,len(A)):
		current = A[i]
		j = i-1
		while j >= 0 and A[j] > current:
			A[j+1] = A[j]
			j -= 1        
		A[j+1] = current
		
A = [27, 47, 9, 10, 7, 30]			
InsertionSort(A)
print(A)
