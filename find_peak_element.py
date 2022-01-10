

'''Given an array of integers. Find a peak element in it. 
An array element is a peak if it is NOT smaller than 
its neighbours. For corner elements, we need to consider
only one neighbour. 
Input: array[]= {5, 10, 20, 15}
Output: 20
The element 20 has neighbours 10 and 15,
both of them are less than 20.

Input: array[] = {10, 20, 15, 2, 23, 90, 67}
Output: 20 or 90
The element 20 has neighbours 10 and 15, 
both of them are less than 20, similarly 90 has neighbours 23 and 67.
Following corner cases give better idea about the problem. 

If input array is sorted in strictly increasing order, 
the last element is always a peak element. 
For example, 50 is peak element in {10, 20, 30, 40, 50}.
If the input array is sorted in strictly decreasing order, 
the first element is always a peak element. 
100 is the peak element in {100, 80, 60, 50, 20}.
If all elements of input array are same, every element is a peak element.

It is clear from the above examples that there is always a peak element
 in the input array.

Naive Approach: The array can be traversed and the element whose neighbours
 are less than that element can be returned.

Algorithm: 
If in the array, the first element is greater than the second or the last element is greater than the second last, print the respective element
and terminate the program.Else traverse the array from the second index to the second last index
If for an element array[i], it is greater than both its neighbours,i.e., array[i] > array[i-1] and array[i] > array[i+1], 
 then print that element and terminate.'''
 
''' 
# Simple program O(n)
 
def findpeak(arr,n):
#first or last element is peak element
	# if (n == 1):
		# return 0
	# if (arr[0] >= arr[1]):
		# return 0
	# if (arr[n-1] >= arr[n-2]):
		# return n-1
	# Check for every other element
	for i in range(1,n - 1):
		#check if the neighbours are smaller
		if (arr[i] >= arr[i-1] and arr[i] >= arr[i+1]):
			return i
'''

'''
# Driver code.
arr = [ 1, 3, 20, 4, 1, 0 ]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))
'''
 

'''
output:
Index of a peak point is 2
Complexity Analysis: 

Time complexity: O(n). 
One traversal is needed so the time complexity is O(n)
Space Complexity: O(1). 
No extra space is needed, so space complexity is constant
Efficient Approach: Divide and Conquer can be used to find a peak in O(Logn) time. The idea is based on the technique of Binary Search to check if the middle element is the peak element or not. If the middle element is not the peak element, then check if the element on the right side is greater than the middle element then there is always a peak element on the right side. If the element on the left side is greater than the middle element then there is always a peak element on the left side. Form a recursion and the peak element can be found in log n time. 

Algorithm: 

Create two variables, l and r, initialize l = 0 and r = n-1
Iterate the steps below till l <= r, lowerbound is less than the upperbound
Check if the mid value or index mid = (l+r)/2, is the peak element or not, if yes then print the element and terminate.
Else if the element on the left side of the middle element is greater then check for peak element on the left side, i.e. update r = mid – 1
Else if the element on the right side of the middle element is greater then check for peak element on the right side, i.e. update l = mid + 1
 '''
 
# A Python3 program to find a peak
# Element using divide and conquer

# A binary search based function
# that returns index of a peak element.

def findPeakUtil(arr, low, high,n):
	
	#find index of a middle element
	# (low + high)/2
	mid = low + (high - low)/2
	mid = int(mid)
	
	#compare middle element with its
	#neighbours (if neighbours exist)
	if ((mid == 0 or arr[mid -1] <= arr[mid]) and 
	(mid == n - 1 or arr[mid+1] <= arr[mid])):
		return mid
	
	#if middle element is not peak and
	# its left neighbour is greater than it, then left
	#half must have a peak element.
	elif (mid > 0 and arr[mid-1] > arr[mid]):
		return findPeakUtil(arr,low,(mid-1),n)
	
	#if the middle element is not peak and its right
	#neighbour is greater than it, then right half must
	#have a peak element.
	else:
		return findPeakUtil(arr,(mid + 1), high, n)
		
# A wrapper over recursive
# Function findPeakUtil()
def findPeak(arr, n):
	
	return findPeakUtil(arr, 0, n-1, n)

'''
#driver code
arr = [1,3,20,4,1,0]
n = len(arr)
print('Index of a peak point is', findPeak(arr,n))


Complexity Analysis: 

Time Complexity: O(Logn). 
Where n is the number of elements in the input array. In each step our search becomes half. So it can be compared to Binary search, So the time complexity is O(log n)
Space complexity: O(1). 
No extra space is required, so the space complexity is constant.
'''
 
 
 
 
 
 
 
 
 
 
 
 
 
 