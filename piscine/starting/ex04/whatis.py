import sys

def is_integer(obj: any) -> bool:
	if not obj:
		return False
	if obj[0] in "+-":
		obj = obj[1:]
	return obj.isdigit()

def odd_or_even(argv: any):
	if len(argv) == 1:
		sys.exit()

	assert len(argv) == 2 , "AssertionError: more than one argument is provided"
	assert is_integer(argv[1]), "AssertionError: argument is not an integer"
	
	nb = int(argv[1])
	if nb % 2 == 0:
		return "I'm Even."
	return "I'm Odd."

try:
	print(odd_or_even(sys.argv))
except AssertionError as error:
	print(error)

