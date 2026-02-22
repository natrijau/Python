from sys import argv, exit 
from ft_filter import ft_filter 

def special_char(obj: str) -> bool:
	"""
	Docstring pour special_char
	
	:param words: Description
	:type words: str
	:return: Description
	:rtype: bool
	"""

	if all(char.isalpha() is False and char.isspace() is False for char in obj):
		return False

	if len(obj.split()) < 2:
		return False

	return True

def validate_args(av: list[str])  -> bool:
	"""
	Docstring pour validate_args
	
	:param av: Description
	:type av: list[str]
	:return: Description
	:rtype: bool
	"""
	assert len(av) == 3 and av[2].isdigit() and special_char(av[1]), "AssertionError: the arguments are bad"
	return True

def main():
	
	try:
		if validate_args(argv) is True:
			print(ft_filter(lambda word: len(word) > int(argv[2]), argv[1].split()))
	except KeyboardInterrupt:
		exit()
	except EOFError:
		exit()
	except AssertionError as error:
		print(error)


if __name__ == "__main__":
	main()