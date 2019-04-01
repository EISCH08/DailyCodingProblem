#Daily Coding Problem
#Parker Eischen
#April 1st 2019
'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def firstThought(A,k): #O(N * (N-1))
	for i in range(0,len(A)):
		val = k - A[i]
		for j in range(i+1,len(A)):
			if A[j] == val: return True
	return False






def helper(A,k):
	print(firstThought(A,k))





helper([1,10,15,3],26)