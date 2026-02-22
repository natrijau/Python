import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	sqr_height = np.multiply(height, height)
	return np.divide(weight, sqr_height)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	return [bool(x > limit) for x in bmi]
# IMC = masse(kg) / Taille(m) ^ 2
# < 18.5 sous-poids | <24.9 noraml | < 29 surpoid | 34.9 obesité |>35 severe 


#tester.py
#from give_bmi import give_bmi, apply_limit
#height = [2.71, 1.15]
#weight = [165.3, 38.4]
#bmi = give_bmi(height, weight)
#print(bmi, type(bmi))
#print(apply_limit(bmi, 26))

# np.multiplie(height) --> nouveau tableau avec talle^2
# np.divide(masse/element[1] nu nouveau tableau precedent)

#arr = np.multiply(height, height)
#imc = divide(weight, arr)

#Votre fonction `give_bmi` prend en entrée deux listes d'entiers ou de nombres à virgule flottante et renvoie une liste
#de valeurs d'IMC.

#Votre fonction `apply_limit` accepte en paramètres une liste d'entiers ou de nombres à virgule flottante et un entier représentant
#une limite. Elle renvoie une liste de booléens (Vrai si la valeur est supérieure à la limite).

#Vous devez gérer les erreurs si les listes n'ont pas la même taille, ne sont pas de type `int` ou `float`, etc.


#Expected output:
#$> python tester.py
#[22.507863455018317, 29.0359168241966] <class 'list'>
#[False, True]