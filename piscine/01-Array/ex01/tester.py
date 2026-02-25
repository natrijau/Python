from array2D import slice_me
import numpy as np
family = [
		[1.80, 78.4]
		,[2.15, 102.7]
		,[2.10, 98.5]
		,[1.88, 75.2]
	]

#rien = {}
rien = []
x = slice(3, 1)
print(x)
print("real slice", family[x])
print("real slice new shape is :", np.array(family).shape)
print(slice_me(family, 0,  1))
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
print(slice_me(rien, 0, 8))
print(slice_me(family))