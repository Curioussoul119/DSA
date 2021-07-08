# Merging
'''
def merge(A,B): # Merge A[0:m], B[0:n]
	(C, m, n) = ([],len(A),len(B))
	(i,j) = (0,0) # Current positions in A, B.
	
	while i+j < m+n: # i+j is number of elements merged so far
		if i == m: # Case 1: A is empty.
			C.append(B[j])
			j = j+1
		elif j == n: # CAse 2: B is empty
			C.append(A[i])
			i = i+1
		elif A[i] <= B[j]: # CAse 3: Head of A is smaller.
			C.append(A[i])
			i = i+1
		elif A[i] > B[j]: # CASE 4: Head of B is smaller
			C.append(B[j])
			j = j+1
	return(C)
	'''
	
#Check with input
'''a=list(range(0,500,2))
a enter
b=list(range(1,75,2))
b enter
merge(a,b)
len(merge(a,b))
'''

# Merging, Wrong

def mergewrong(A,B): # Merge A[0:m], B[0:n]
	(C,m,n) = ([], len(A), len(B))
	(i,j) = (0,0) # current positions in A, B
	
	while i+j < m+n:
	# i+j is number of elements merged so far
		#combine CASE 1, CASE 4
		if i == m or A[i] > B[j]:
		 C.append(B[j])
		 j = j+1
		 
		 # combine CASE 2, CASE 3
		elif j == n or A[i] <= B[j]:
			C.append(A[i])
			i=i+1
	return(C)
'''
a=[2,4,6]
b=[1,3,5]
merge(a,b)
error = List index out of range.
Just below while loop: print(m,n,i,j)
to know what is happening'''


## MERGE SORT
'''
To sort A[0:n] into B[0:n]
if n is 1, nothing to be done
otherwise
Sort A[0:n//2] into L (left)
Sort A[n//2:n] into R (right)
Merge L and R into B.

'''

'''def mergesort(A,left,right):
	# Sort the slice A[left:right]
	
	if right - left <= 1: # Base CAse
		return(A[left:right])
		
	if right - left > 1: # Recursive call
		
		mid = (left+right)//2
		
		L=mergesort(A, left,mid)
		
		R= mergesort(A, mid, right)
		
		return(merge(L, R))'''
		
'''
a = list (range(1,100,2)) + list(range(0,100,2))
a enter
mergesort(a,0,len(a))
you will get sorted list.
What if take larger list 10000, I will get result fraction of seconds
Not like insertion sort, recursion sort where O(n^2) but here o(n*log(n)).
Here we don't run into recursion limit problem.
'''

'''
# Variations on Merge.

#Union of two sorted lists (discard duplicates)
	while A[i] == B[j], increment j
	append A[i] to C and increment i

# Intersection of two sorted lists

if A[i] < B[j], increment i.
if B[j] < A[i], increment j.
if A[i] == B[j]
	while A[i] == B[j], increment j
	append A[i] to C and increment i
	
Exercise : List difference elements in A but not in B.

#merge sort: shorcomings.

# Merging A and B creates a new array C.
	No obvious way to efficiently merge in place.
# Extra storage can be costly.
#inherently recursive.
	#recursive call and return are expensive.
	
'''








































'''
	