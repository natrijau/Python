#Tout les objets de type "Null"

#	1 . None
#		Type : NoneType   --> comme NULL
#		C'est l'absence de valeur ou un objet vide

#	2 . NaN (Not a Number)
#		Type : float
#		NaN n’est égal à rien, pas même à lui-même

#	3 . 0 (zéro entier) 
#		Type : int

#	4 . "" (chaîne vide)
#		Type : str

#	5 . False (booléen faux)
#		Type : bool
def NULL_not_found(object: any) -> int:
	if object is None:
		print("Nothing:", object, type(object))
		return 0
	elif type(object) is float and object != object:
		print("Cheese:", object, type(object))
		return 0
	elif type(object) is int and object == 0:
		print("Zero:", object, type(object))
		return 0		
	elif object == "":
		print("Empty:", object, type(object))
		return 0
	elif object is False:
		print("Fake:", object, type(object))
		return 0
	print("Type not found")
	return 1