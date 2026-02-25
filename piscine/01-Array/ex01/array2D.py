import numpy as np

def slice_me(family: list, start: int, end: int) -> list:

	assert len(family) > 0, "family cannot be empty"
	assert isinstance(family, list), "family must be a list"
	assert isinstance(start, int), "start must be an int"
	assert isinstance(end, int), "end must be an int"
	assert all(isinstance(row, list) for row in family), "family must be 2D"
	assert all(len(row) == len(family[0]) for row in family), "rows must have same length"

	tab = np.array(family)
	print("My shape is :", tab.shape)
	new_tab = tab[start:end]
	print("My new shape is :", new_tab.shape)
	return new_tab.tolist()
