#filter(function or None, iterable) --> filter object

#Return an iterator yielding those items of iterable for which function(item)
#is true. If function is None, return the items that are true.

def	ft_filter(funct, iterable: list):
	"""
	filter(function or None, iterable) --> filter object

	Return an iterator yielding those items of iterable for which function(item)
	is true. If function is None, return the items that are true.
	"""
	if funct is None:
		return [x for x in iterable if x]

	new = list(None)
	for x in iterable:
		if funct(x):
			new.append(x)
	return [x for x in iterable if funct(x)]