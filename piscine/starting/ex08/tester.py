from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
from os import get_terminal_size
from os import write


def it_per_sec(it, time):
	return it/time
#for elem in ft_tqdm(range(3)):
#	sleep(0.005)
#print()
size = len(range(3333))
column = get_terminal_size().columns
purcentage = 0
sign_purcen = "%"
pipe = "|"
white_space = ""
it_s = 

#| 3333/3333 [00:17<00:00, 194.58it/s]


while purcentage < 100:
	purcentage += 1
	add = ""
	if purcentage < 10:
		add = "  "
	elif purcentage < 100 and purcentage > 10:
		add = " "
	else:
		add = ""
	first_word = add + str(purcentage) + sign_purcen + pipe
	white_space = "█" * purcentage
	print(f"\r{first_word}{white_space}", end="") 
	sleep(0.05)
print()
#width = get_terminal_size().columns
#purcentage = 0
#egual = "="
#print(size)
#for i in enumerate(range(3333)):
	#str = f"{purcentage}% | {egual} | {i}/{size}"
	#write(1, b"\r" + str.encode())



for elem in tqdm(range(3333)):
	sleep(0.005)
print()