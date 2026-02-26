from load_image import ft_load

i = 1

def tester(path: str):
    global i
    print("\n----- Test", i,"-----\n")
    i += 1
    print(ft_load(path))
try:
    tester("landscape.jpg")
    tester("")
    tester(1)
except AssertionError as error:
    print(error)
