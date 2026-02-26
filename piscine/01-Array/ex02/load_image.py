from PIL import Image
import numpy as np


def ft_load(path: str):
    """
    Docstring ft_load

    :param path: Charge une image, affiche son format \
                    et son contenu en pixels (format RGB).
    :type path: str
    :return instruction -> "you can return to the desired format"
    :return type: Array
    :raises AssertionError: Si le chemin est invalide ou si le format n'est pas JPEG/JPG.
    :raises FileNotFoundError: Si l'image n'existe pas.
    :raises ValueError: Si l'image ne peut pas être chargée.
    """

    assert path is not None and path != "", "Need a good path"
    assert isinstance(path, str), "Need a string param to path file"

    img = Image.open(path)
    with Image.open(path) as img:
        assert img.format in ["JPEG", "JPG"], "Need format JPEG or JPG"
        img = img.convert("RGB")
    data = np.array(img)
    print("Thes shape of image is:", data.shape)
    return data
