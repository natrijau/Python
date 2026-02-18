#import os
from os import get_terminal_size


def ft_tqdm(lst: range):
	"""
	Docstring pour ft_tqdm
	
	:param lst: Description
	:type lst: range
	"""

	size = len(lst)
	width = get_terminal_size().columns
	purcentage = 0
	egual = "="
	for i in size:
		print(f"{purcentage}% | {egual} | {i}/{size} ")
	#os.write(1, b"_")