# Euclid Algorithm

'''
#Suppose d divides both m and n, and m>n
#then m = a*d, n = b*d.
#So m-n = ad-bd = (a-b)d
# d divides m-n as well.
# so gcd(m,n) = gcd(n,m-n)

consider gcd(m,n) with m>n
If n divides m, return n.
otherwise, compute gcd(n,m-n) and return that value.
'''

'''def gcd(m,n):
	#assume m>=n
	if m<n:
		(m,n)=(n,m)
	if (m%n) == 0:
		return(n)
	else:
		diff = m-n
		#diff > n? Possible!
		return(gcd(max(n,diff),min(n,diff)))'''
		
# Euclid algorithm-using while loop.

'''def gcd(m,n):
	if m<n: # assume m>=n
		(m,n) = (n,m)
	
	while (m%n) != 0:
		diff = m-n
		#diff > n? possible!
		(m,n) = (max(n,diff),min(n,diff))
	return(n)'''
	
# Even better
'''
# suppose n does not divide m
# then m=qn+r, where q is quotient, r is the 
remainder when we divide m by n.
# Assume d divides both m and n.
# Then m=ad, n=bd.
# so ad=q(bd) + r.
# it follows that r = cd, so d divides r as well.
'''
# This is the actual version of gcd 
#proposed by Euclid.
# 1. Consider gcd(m,n) with m>n.
# 2. If n divides m, return n.
# 3. otherwise, let r = m%n.
# 4. return gcd(n,r)

'''def gcd(m,n):
	if m<n: # assume m>=n.
		(m,n) =  (n,m)
	if (m%n) == 0:
		return(n)
	else:
		return(gcd(n,m%n)) # m%n < n, always!.'''

# using while loop.
def gcd(m,n):
	if m<n: # assume m>=n
		(m,n) = (n,m)
	while (m%n) != 0:
		(m,n) = (n, m%n) #m%n < n, always!
	return(n)
	
 ''' # Efficiency
 # Can show that the second version of Euclid'second
 algorithm takes time proportional to the number
 of digits in m.
 # if m is 1 billion (10^9), the naive algorithm
 takes billion of steps, but this algorithm takes
 tens of steps.'''
	



	
