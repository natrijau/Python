from os import get_terminal_size

def ft_tqdm(lst: range) -> None:
	"""
	Loading bar
	"""
	size = len(lst)
	column = get_terminal_size().columns
	it = 0
    
	for it in lst:
		purcent = round((it * 100) / size)
		purcentage = f"{purcent:3d}%|"

		len_it = len("| ") + 1 + len(str(it)) + len(str(size))

		bar_space = column - len_it - len(purcentage) - 1

		white_space = int((purcent * bar_space)/100)
		len_space = bar_space - white_space

		if len_space < 0:
			len_space = 0
		

		loading_string = f"\r{purcentage}{"█" * white_space}{" " * len_space}| {it}/{size} "
		print(loading_string, end="" )
		yield
	print(f"\r{purcentage}{"█" * white_space}{" " * len_space}| {size}/{size} ")