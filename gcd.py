#Computing gcd(14,63)
#Idea
''' 1. Factors of 14: 1,2,7,14
	2. Factors of 63: 1,3,7,9,21,63
	3. Construct list of common factors
	4. For each factor of 14, check if it is a factor of 63
							1,7
	5. Return largest factor in this list'''
# Algorithm steps
''' 1. Use fm, fn for list of factors of m,n respectively
	2. For each i from 1 to m, add i to fm if i divides m
	3. For each j from 1 to n, add j to fn if j divides n
	4. Use cf for list of common factors
	5. For each f in fm, add f to cf if f also appears in fn
	6. Return largest (rightmost) value in cf.'''
	
def gcd(m,n):
	fm=[]
	#py:excludes last value in the range =>m+1
	for i in range(1,m+1):
		if m%i ==0:
			fm.append(i)
	fn=[]
	for j in range(1,n+1):
		if n%j == 0:
			fn.append(j)
	cf=[]
	for f in fm:
		if f in fn:
			cf.append(f)
	return(cf[-1])
	
