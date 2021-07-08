# INSERTION SORT
''' 
# Strategy 2
First paper: Put in a new stack
Second paper:
	Lower marks than first? place below first paper.
	higher marks than first? Place above first paper.
Third paper:
	Insert into the correct position wrt first two papers.
Do this for each subsequent paper
Insert into correct position in new sorted stack.'''

def InsertionSort(seq):
	for sliceEnd in range(len(seq)):
		# Build longer and longer sorted slices
		# In each iteration seq[0:sliceEnd] already sorted.
		
		# Move the first element after sorted slice left
		# till it is in the correct place.
		pos = sliceEnd
		while pos > 0 and seq[pos] < seq[pos-1]:
			(seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
			pos = pos-1
# Ananlysis of Insertion Sort
	''' 
	# Inserting a new value in sorted segment of length k
	requires upto k steps in the worst case.
	# In each iteration, sorted segment in which to insert
	increased by 1
	# T(n)= 1+2+3.......+n-1 = n(n-1)/2= O(n^2)
# Efficiency
https://www.youtube.com/watch?v=QnjToZfpi0E
INsertinSort works better than SelectionSort
for comments look in the above link: last one minute.