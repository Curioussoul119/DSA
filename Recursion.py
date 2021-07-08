# Recursive functions are typically Inductive definitions.
# Many arithmetic functions are naturally defined inductively.
# Examples.
'''
 # Factorial
  0! = 1
  n! = n * (n-1)!
  # Multiplication- Repeated Addition.
  m*1 = m
  m*(n+1) = m + (m*n)
  m*n = m + m(n-1)
  
  # Define one or more BASE cases
  # Inductive step defines f(n) in terms of smaller arguments.
  Example: Fibonacci series Fib(1)= Fib(2)=1
  Fib(n)=Fib(n-1)+Fib(n-2)
  #Inductive definitins naturally give rise to recursive programs.

  
 # Ex-1: Factorial:
 def factorial(n):
	if n == 0:
		return(1)
	else: 
		return(n*factorial(n-1))
  # Ex-2: Multiply.
 def mulitiply(m,n):
	if n == 1:
		return(m)
	else:
		return(m+multiply(m,n-1))
		
  # Ex-3: length of a list
 def length(l):
	if l == []:
		return(0)
	else:
		return(l[0]+sumlist[1:])'''
		
# Recursive insertion sort.
def InsertionSort(seq):
	isort(seq,len(seq))
def isort(seq,k): # sort slice seq[0:k]
	if k>1 :
		isort(seq,k-1)
		insert(seq,k-1)
def insert(seq,K): #Insert seq[k] into sorted sq[0:k-1]
	pos= k
	while pos > 0 and seq[pos] < seq[pos-1]:
		(seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
		pos = pos - 1
 # Recursion fails at it's limit: around 998. You can work around it.
 #by setting recursion limit. 1. import sys, sys.setrecursionlimit(10000).