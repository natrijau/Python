from sys import argv, exit 

def special_char(obj: str) -> bool:
	"""
	Docstring pour special_char
	
	:param words: Description
	:type words: str
	:return: Description
	:rtype: bool
	"""

	return all(char.isalnum() or char.isspace() for char in obj)

def validate_args(av: list[str])  -> bool:
	"""
	Docstring pour validate_args
	
	:param av: Description
	:type av: list[str]
	:return: Description
	:rtype: bool
	"""
	assert len(av) == 2 and special_char(av[1]), "AssertionError: the arguments are bad"
	return True


def	morse_translate(word: str)  -> str:
	"""
	"""
	morse = {' ': '/ ',
			'0': '-----',
			'1': '.----',
			'2': '..---',
			'3': '...--',
			'4': '....-',
			'5': '.....',
			'6': '-....',
			'7': '--...',
			'8': '---..',
			'9': '----.',
			'A': '.-',
			'B': '-...',
			'C': '-.-.',
			'D': '-..',
			'E': '.',
			'F': '..-.',
			'G': '--.',
			'H': '....',
			'I': '..',
			'J': '.---',
			'K': '-.-',
			'L': '.-..',
			'M': '--',
			'N': '-.',
			'O': '---',
			'P': '.--.',
			'Q': '--.-',
			'R': '.-.',
			'S': '...',
			'T': '-',
			'U': '..-',
			'V': '...-',
			'W': '.--',
			'X': '-..-',
			'Y': '-.--',
			'Z': '--..'}
	
	translate = " ".join(morse[c.upper()] for c in word)
	return translate


def main():
	
	try:
		if validate_args(argv) is True:
			print(morse_translate(argv[1]))
	except KeyboardInterrupt:
		exit()
	except EOFError:
		exit()
	except AssertionError as error:
		print(error)


if __name__ == "__main__":
	main()