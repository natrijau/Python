#def ft_load(path: str) -> array: (you can return to the desired format)
from PIL import Image
import numpy as np

def ft_load(path: str):

	assert path == "animal.jpeg", "bad image"
	img = Image.open(path)
	assert img.format in ("JPEG", "JPG", "jpeg", "jpg"), f"Error: Unsupported format: {img.format}"
	#Format RGB
	img = img.convert("L")

	#Format tableau numpy
	data = np.array(img)
	print("The shape of image is:", data.shape)

	return data