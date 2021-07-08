
#Selection Sort
def SelectionSort(l):
	# Scan slices l[0:len(l)], l[1:len(l)],...
	for start in range(len(l)):
		#find minimum value in slice
		minpos = start
		for i in range(start,len(l)):
			if l[i] < l[minpos]:
				minpos = i
		#...and move it to start of slice
		(l[start],l[minpos])=(l[minpos],l[start])
# Finding minimum in unsorted segment of length K requires one scan, K steps.
# In each iteration, segment to be scanned reduces by 1.
# T(n) = n+(n-1)+(n-2)+.......+1=n(n+1)/2=O(n^2)