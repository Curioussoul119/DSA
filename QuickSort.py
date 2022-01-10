
# Alternative Approach
'''
Extra space is required to merge
merging happens because elements in left half must move right and viceversa.
can we divide so that everything to the left is smaller than everything to the right?
No need to merge.'''

''' 
Divide and Conquer without merging
# suppose the median value in A is m.
# More all values <=m to left half of A.
	Right half has values >m.
	This shifting can be done in place, in time O(n)
# Recursively sort left and right halves
# A is now sorted! No need to merge

T(n) = 2 T(n/2) + n = O(n log n)
'''
'''
How do we find the median?
	Sort and pick up middle element.
	But our aim is to Sort!
Instead, pick up some value in A - Pivot.
	Split A with respect to this pivot element.
	
Invented by Tonyy Hoare.
'''
'''
# Quick Sort.
1. Choose a pivot element
	Typically the first value in the array
2. Partition A into lower and upper parts with respect to pivot.
3. Move pivot between lower and upper partition.
4. Recursively sort two partitions.
'''


# Quicksort in Python.
def Quicksort(A,l,r): #Sort A[l:r]
	if r - l <= l: # Base case
	return()
	
	# Partition with respect to pivot, a[l]
	yellow = l+1
	
	for green in range(l+1,r):
		if A[green] <= A[l]:
			(A[yellow], A[green]) = (A[green], A[yellow])
			yellow = yellow + 1
	
	
	# Move pivot into place
	
	(A[l], A[yellow-1]) = (A[yellow-1],A[l])
	
	Quicksort(A, l, yellow-1) # Recursive calls
	Quicksort(A, yellow, r)
	
	
'''
l= list (range(500, 0,-1))
l enter
 Quicksort(l,0,len(l))
 
 WE HAVE THE SAME PROBLEM THAT WE HAD WITH INSERTION SORT
 let's say if l= list(range(1000,0,-1))
 you will get recursion depth exceeded error.
 
 import sys
 sys.setrecurrsionlimit(10000)
 
 
 '''






































