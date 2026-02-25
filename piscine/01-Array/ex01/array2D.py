import numpy as np

# Expected output:
#	$> python test_array2D.py
#	My shape is : (4, 2)
#	My new shape is : (2, 2)
#	[[1.8, 78.4], [2.15, 102.7]]
#	My shape is : (4, 2)
#	My new shape is : (1, 2)
#	[[2.15, 102.7]]
#	$>

def slice_me(family: list, start: int, end: int) -> list:
	assert isinstance(family, list), "Need list arg"
	assert isinstance(start, int), "Need int arg"
	assert end is not None, "need good end arg"
	assert start is not None , "need good start arg"
	print("My shape is :", np.array(family).shape)
	x = slice(start, end)
	tmp = family[x]
	print("My new shape is :", np.array(tmp).shape)
	return [family[x]]


#slice(start, end, step)
#	Parameter Values

#Parameter	Description
#start		Optional. An integer number specifying at which position to start the slicing. Default is 0
#end		An integer number specifying at which position to end the slicing
#step		Optional. An integer number specifying the step of the slicing. Default is 1


#arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#print(arr.shape) -----> (2, 4)


#	Write a function that takes as parameters a 2D array, prints its shape, and returns a
#		truncated version of the array based on the provided start and end arguments.
#		You must use the slicing method.
#		You have to handle error cases if the lists are not the same size, are not a list ...
#	
# The prototype of function is:
#	def slice_me(family: list, start: int, end: int) -> list:

#Your tester.py:
#	from array2D import slice_me
#	family = [[1.80, 78.4],
#	[2.15, 102.7],
#	[2.10, 98.5],
#	[1.88, 75.2]]
#	print(slice_me(family, 0, 2))
#	print(slice_me(family, 1, -2))
#
# 
