#Daily Coding Problem
#Parker Eischen
#April 1st 2019
'''
#PROBLEM:
#There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
#
#For example, if N is 4, then there are 5 unique ways:
#
#1, 1, 1, 1
#2, 1, 1
#1, 2, 1
#1, 1, 2
#2, 2
#What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, 
if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

'''

def stairCount(n,X): #recursive function with timeComplexity O(2^n) Only works for [1,2] needs to be Genralized
	if n <= min(X):
		return 1
	else:
		return stairCount(n-1,X) + stairCount(n-2,X)





def stairCountGeneralized(n,X): #recursive function with timeComplexity O(|X|^n) works for all ranges
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		sum = 0
		for x in X:
			sum += stairCountGeneralized(n-x,X)
		return sum

def stairCountGeneralizedFaster(n,X,mem): #recursive function with timeComplexity O(n * |X|) works for all ranges
	mem[0] = 1
	if n<0:
		return 0
	if mem[n] > 0:
		return mem[n]
	else:
		for x in X:
			mem[n] += stairCountGeneralizedFaster(n-x,X,mem)
		return mem[n]
		 




def helper(n,X):
	mem = [0 for x in range(n+1)]
	# print(stairCount(n,X))	
	# print(stairCountGeneralized(n,X))
	print(stairCountGeneralizedFaster(n,X,mem))

helper(100,{1,3,10})









