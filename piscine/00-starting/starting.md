# Introduction aux bases du langage de programmation Python

Ce module introduit les fondamentaux du langage Python à travers 9 exercices progressifs.
Chaque exercice met en pratique des concepts essentiels : structures de données, gestion du temps, types, assertions, manipulation de chaînes, fonctions anonymes, générateurs et plus encore.

---

# Table des matières

- [Exercice 00 – First python script](#exercice-00--first-python-script)  
- [Exercice 01 – First use of package](#exercice-01--first-use-of-package)  
- [Exercice 02 – Gestion du temps](#exercice-02--gestion-du-temps)  
- [Exercice 03 – Null-like values](#exercice-03--null-like-values)  
- [Exercice 04 – Arguments & Assertions](#exercice-04--arguments--assertions)  
- [Exercice 05 – Analyse de texte](#exercice-05--analyse-de-texte)  
- [Exercice 06 – Filter & Lambda](#exercice-06--filter--lambda)  
- [Exercice 07 – Morse Translator](#exercice-07--morse-translator)  
- [Exercice 08 – Barre de progression](#exercice-08--barre-de-progression)

---
# Exercice 00 – First python script

## Objectif

Comprendre les différences entre :

- `list`
- `tuple`
- `set`
- `dict`


En Python, les structures de données permettent de **stocker, organiser et manipuler** des informations de différentes manières.  
Les plus couramment utilisées sont **les listes, les tuples, les ensembles (set) et les dictionnaires**.

- **Liste (`list`)**  
  Structure de données **mutable** et **ordonnée** permettant de stocker une collection d’éléments.  
  Elle accepte les **doublons** et peut être modifiée après sa création.

- **Tuple (`tuple`)**  
  Structure de données **immuable** et **ordonnée**, utilisée lorsque les données ne doivent pas être modifiées.  
  Les doublons sont autorisés.

- **Ensemble (`set`)**  
  Structure de données **mutable** mais **non ordonnée**, contenant uniquement des éléments **uniques**.  
  Elle est souvent utilisée pour supprimer les doublons ou effectuer des opérations mathématiques (union, intersection).

- **Dictionnaire (`dict`)**  
  Structure de données **mutable** stockant des données sous forme de **paires clé-valeur**.  
  Les clés sont uniques et permettent un accès rapide aux valeurs associées.

---

## Comparaison des structures de données Python

| Caractéristique      | Liste             | Tuple             | Ensemble (Set)     | Dictionnaire          |
|----------------------|-------------------|-------------------|--------------------|-----------------------|
| Type                 | Non homogène      | Non homogène      | Non homogène       | Non homogène          |
| Contenu              | Éléments          | Éléments          | Éléments           | Paires clé-valeur     |
| Syntaxe              | `[ ]`             | `( )`             | `{ }`              | `{ clé: valeur }`     |
| Doublons autorisés   | ✅ Oui            | ✅ Oui            | ❌ Non             | ❌ Non (clés)         |
| Imbrication          | ✅ Oui            | ✅ Oui            | ✅ Oui             | ✅ Oui                |
| Exemple              | `[1, 2, 3, 4, 5]` | `(1, 2, 3, 4, 5)` | `{1, 2, 3, 4, 5}`  | `{1: "a", 2: "b"}`    |
| Fonction de création | `list()`          | `tuple()`         | `set()`            | `dict()`              |
| Mutabilité           | ✅ Mutable        | ❌ Immuable       | ✅ Mutable         | ✅ Mutable            |
| Ordonnée             | ✅ Oui            | ✅ Oui            | ❌ Non             | ✅ Oui (Python ≥ 3.7) |
| Structure vide       | `l = []`          | `t = ()`          | `s = set()`        | `d = {}`              |

---

## Récapitulatif des méthodes courantes en Python (Débutant)

### Listes (`list`)

Les listes sont **mutables** et très utilisées.

| Méthode | Description |
|-------|------------|
| `append(x)` | Ajoute un élément à la fin de la liste |
| `remove(x)` | Supprime la première occurrence de `x` |
| `pop()` | Supprime et retourne le dernier élément |
| `insert(i, x)` | Insère `x` à l’index `i` |
| `clear()` | Vide la liste |
| `len(l)` | Retourne la taille de la liste |
| `sort()` | Trie la liste |
| `reverse()` | Inverse l’ordre des éléments |

---

### Tuples (`tuple`)

Les tuples sont **immuables** (pas de modification possible).

| Méthode | Description |
|-------|------------|
| `count(x)` | Compte le nombre d’occurrences de `x` |
| `index(x)` | Retourne l’index de `x` |
| `len(t)` | Retourne la taille du tuple |

---

### Ensembles (`set`)

Les ensembles contiennent des **éléments uniques**.

| Méthode | Description |
|-------|------------|
| `add(x)` | Ajoute un élément |
| `remove(x)` | Supprime un élément (erreur si absent) |
| `discard(x)` | Supprime un élément (sans erreur) |
| `clear()` | Vide l’ensemble |
| `union(s)` | Union de deux ensembles |
| `intersection(s)` | Intersection de deux ensembles |
| `len(s)` | Taille de l’ensemble |

---

### Dictionnaires (`dict`)

Les dictionnaires stockent des **paires clé-valeur**.

| Méthode | Description |
|-------|------------|
| `get(key)` | Retourne la valeur associée à la clé |
| `keys()` | Retourne toutes les clés |
| `values()` | Retourne toutes les valeurs |
| `items()` | Retourne les paires clé-valeur |
| `pop(key)` | Supprime une clé et sa valeur |
| `update(d)` | Met à jour le dictionnaire |
| `len(d)` | Taille du dictionnaire |

---

### Fonctions utiles pour toutes les structures

| Fonction | Description |
|--------|------------|
| `len()` | Nombre d’éléments |
| `type()` | Type de la variable |
| `print()` | Affichage |


---

# Exercice 01 – First use of package

## Objectif

Créer une première fonction Python permettant de manipuler les types d’objets.

Cet exercice permet de se familiariser avec :

- Les types natifs Python (list, tuple, set, dict, str, int)
- La fonction intégrée type()
- L’affichage formaté
- La création d’une fonction avec annotation de type
- Le comportement d’un fichier exécuté seul

---

## Prototype demandé


```python
def all_thing_is_obj(object: any) -> int:
    # your code here
```

- La fonction doit afficher le type de l’objet passé en paramètre.
- Elle doit retourner 42.
- Aucune fonction spécifique n’est imposée (Allowed functions: None).

##  Formatage de date lisible

Types à reconnaître

La fonction doit détecter et afficher correctement :
- list
- tuple
- set
- dict
- str

Pour les chaînes de caractères (str) :

Le message doit être :
```python
<contenu> is in the kitchen : <class 'str'>
```

Pour un type non reconnu :
```python
Type not found
```


## type() vs isinstance()

Pour : 
```python
class MyList(list):
    pass

obj = MyList()
```

### 1 - type()

La fonction type(obj) retourne le type exact de l’objet.
```python
print(type(obj) == list) # -> <class '__main__.MyList'>
```
Car type(obj) est exactement MyList, pas list
Cette comparaison fonctionne uniquement si le type est exactement list.
Elle ne prend pas en compte l’héritage.

### 2 - isinstance()

isinstance(obj, type) vérifie si un objet est :
- du type donné
- ou d’un type qui hérite de ce type

```python
x = [1, 2, 3]
if isinstance(x, list): -# --> True
    print("C'est une liste")
```
Car MyList hérite de list.



- Avec type() :


- Avec isinstance() :
```python
x = [1, 2, 3]
print(isinstance(obj, list)) # True
```
Car MyList hérite de list.

---

### Tableau récapitulatif

| Fonction             | Vérifie type exact      | Gère l’héritage   | Recommandée ?     
|----------------------|-------------------------|-------------------|--------------------|
| type(obj) == list    | ✅ Oui                  | ❌ Non            | ❌ Non             |
| isinstance(obj, list)| ❌ Non                  | ✅ Oui            | ✅ Oui             |

---

# Exercice 02 – Gestion du temps

## Objectif

Manipuler les dates et comprendre le **timestamp Unix (Epoch)**, qui représente le nombre de secondes écoulées depuis le **1er janvier 1970, 00:00:00 UTC**.

Cet exercice permet de se familiariser avec :

- Le module `datetime` pour créer et manipuler des dates et heures
- Les fuseaux horaires (`timezone`)
- La différence entre deux dates (`timedelta`)
- Le formatage des dates et l’affichage en notation scientifique

---

## Création de dates

```python
from datetime import datetime, timezone

# Date de référence Unix Epoch
post_date = datetime(1970, 1, 1, tzinfo=timezone.utc)

# Date actuelle UTC
now = datetime.now(timezone.utc)
```

- datetime(1970, 1, 1, tzinfo=timezone.utc) crée un objet datetime pour l’Epoch avec le fuseau horaire UTC.
- datetime.now(timezone.utc) récupère la date et l’heure actuelle en UTC.

##  Calcul de la différence entre deux dates

```python
delta = now - post_date
seconds = delta.total_seconds()
```

- delta est un objet timedelta représentant l’intervalle de temps entre now et post_date.
- total_seconds() retourne la durée totale en secondes.

##  Formatage de date lisible

```python
date_str = now.strftime("%b %d %Y")
print(date_str)  # Exemple: Feb 20 2026
```

- %b : nom abrégé du mois (Jan, Feb…)
- %d : jour du mois (01 à 31)
- %Y : année sur 4 chiffres

##  Affichage du timestamp en notation scientifique

```python
print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
```

- :,.4f : format avec virgule comme séparateur de milliers et 4 décimales
- :.2e : format scientifique (exponentielle) avec 2 décimales

***Exemple de sortie :***
```python
Seconds since January 1, 1970: 1,793,407,200.1234 or 1.79e+09 in scientific notation
```

---

# Exercice 03 – Null-like values

## Objectif

Identifier les **valeurs null-like** en Python et comprendre comment elles sont traitées.  
Ces valeurs peuvent représenter une **absence de données**, des **valeurs vides** ou des **booléens faux**.

---

## Types de valeurs null-like

1. `None`  
   - Type : `NoneType`  
   - Représente l'absence de valeur ou un objet vide

2. `NaN` (Not a Number)  
   - Type : `float`  
   - N’est égal à rien, pas même à lui-même (`float("NaN")`)

3. `0` (zéro entier)  
   - Type : `int`

4. `""` (chaîne vide)  
   - Type : `str`

5. `False` (booléen faux)  
   - Type : `bool`

---

## Fonction de test `NULL_not_found`

```APKpython
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
```

---

## Bonnes pratiques

- None est le seul objet du type NoneType.
- Pour détecter NaN, utiliser object != object ou math.isnan().
- Les tests if not object: détectent implicitement 0, "", False et None.
- Utiliser is pour comparer à None et False pour éviter les erreurs.

---

# Exercice 04 – Arguments & Assertions

## Objectif

Créer un script Python qui :

- prend un seul argument depuis la ligne de commande,
- vérifie s’il s’agit d’un entier,
- affiche si ce nombre est pair ou impair,
- ou déclenche une AssertionError si :
	- il n’y a aucun argument,
	- il y a plus d’un argument,
	- l’argument n’est pas un entier.

---

## Référence : Python AssertionError Exception

1. Qu’est‑ce qu’un AssertionError ?

Un AssertionError est une exception intégrée en Python qui est levée quand une instruction assert échoue.
L’instruction assert permet de vérifier qu’une condition est vraie — si elle est fausse, Python génère une AssertionError et arrête le programme.

2. Définition

- Utilisé surtout pour le debugging (vérifier des hypothèses dans le code).
- Peut être intercepté dans un bloc try … except.

---

Exemple simple:
```python
x = "hello"
assert x == "hello"  # rien ne se passe
assert x == "goodbye"  # AssertionError
```
Si la condition est fausse, une AssertionError est levée.

---

## Bonnes pratiques

- Utiliser assert pour vérifier des hypothèses dans le code.
- Fournir un message explicite dans l’assertion pour faciliter le debug :
```python
assert condition, "Message d'erreur clair"
```
- Ne pas utiliser assert pour gérer des erreurs normales (préférer if + raise).
- Pour afficher proprement le message d’une AssertionError, on peut capturer l’exception :
```python
try:
    assert condition, "Message d'erreur clair"
except AssertionError as error:
    print(error)
```
Cela permet de fournir un retour lisible à l’utilisateur sans planter le programme brutalement.

---------

***A partir de l'exercice 05 , toutes les fonctions doivent avoir une documentation (___doc___)***

---

# Documentation de `__doc__` en Python

`__doc__` est un attribut spécial disponible sur **tous les modules, classes, fonctions et méthodes** en Python.  
Il contient la **docstring** associée, c’est-à-dire la chaîne de documentation décrivant l’objet.

---

## 1 - Définition

- Type : `str` ou `None`
- Valeur : La chaîne de documentation définie par des **guillemets triples** `"""..."""` au début du module, de la classe ou de la fonction.
- Si aucun docstring n’est présent, `__doc__` vaut `None`.

---

## 2 - Obtenir la documentation

### Pour un module
```python
import math
print(math.__doc__)
```

## 3 - Bonnes pratiques pour __doc__

1) Toujours mettre une docstring descriptive pour :

- les modules
- les classes
- les fonctions/méthodes

2) Commencer par une phrase courte résumant l’objet.

3) Ajouter, si nécessaire :
- Arguments (Args) et types
- Valeur de retour (Returns) et type
- Exceptions possibles (Raises)

4) Utiliser les guillemets triples """ au début de l’objet.

## 4 - Notes
- Toutes les fonctions doivent avoir une **docstring claire** expliquant :
  - l’objectif de la fonction,
  - les paramètres et leurs types,
  - le type et la signification du retour,
  - les exceptions levées (le cas échéant).
- Aucune exécution de code en **scope global** : tout doit passer par la fonction `main()`.
- Les exceptions doivent être **capturées et affichées proprement**, sans planter le programme.

## 5 Exemple complet
```python
"""
building.py

Programme autonome qui analyse une chaîne de caractères fournie
en argument et affiche le nombre de majuscules, minuscules, chiffres,
espaces et ponctuations.

Usage :
    python building.py "Ma chaîne à analyser"

Arguments :
    text (str) : chaîne à analyser

Retour :
    None (affiche les résultats à l'écran)

Exceptions :
    AssertionError : si aucun argument ou trop d'arguments sont fournis
"""
```

- building.__doc__ retournera exactement ce texte.
- help(building) affichera la docstring de manière lisible.

---

# Exercice 05 – First standalone program Python

## Objectif

Créer un **programme autonome** en Python qui :

- prend **une seule chaîne de caractères** depuis la ligne de commande,
- affiche le **nombre de majuscules, minuscules, chiffres, espaces et caractères de ponctuation** dans cette chaîne,
- ou déclenche une **AssertionError** si :
  - aucun argument n’est fourni,
  - plus d’un argument est fourni.

Si aucun argument n’est fourni, le programme doit **demander à l’utilisateur de saisir une chaîne**.

---

## Fonctionnalités

1. **Programme autonome**  
   - Doit contenir une fonction `main()` et ne pas être un simple script global.
2. **Arguments**  
	- Accepte **un seul argument de type chaîne**.
	- Si l’argument est absent ou invalide, une exception est levée ou l’utilisateur est invité à entrer une chaîne.
3. **Analyse du texte et compter**  
	- Les **lettres majuscules**
	- Les **lettres minuscules**
	- Les **chiffres**
	- Les **espaces**
	- Les **caractères de ponctuation**
4. **Gestion des erreurs**  
	- `AssertionError` est utilisé pour signaler un nombre d’arguments incorrect.

---

## Exemple de sortie attendue

```bash
$> python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
7 punctuation marks
26 spaces
15 digits
$>
```

### Bonnes pratiques

Toujours utiliser une fonction main() pour centraliser le code exécuté :

```python
def main():
    # tests et gestion des erreurs

if __name__ == "__main__":
    main()
```
- Ajouter une docstring (__doc__) pour le programme et pour chaque fonction.
- Ne jamais exécuter de code directement dans le scope global (hors main).

--- 

# Exercice 06 – Filter & Lambda

## Objectif

Apprendre à recréer une fonction intégrée de Python (filter) et à manipuler des chaînes avec des expressions lambda et des compréhensions de liste.

Cet exercice est divisé en deux parties :

1 - Recréer le comportement de la fonction intégrée filter avec list comprehension.
2 - Écrire un programme qui filtre les mots d’une chaîne selon leur longueur, en utilisant lambda et list comprehension.

Cet exercice explore des concepts avancés de Python fonctionnel et itératif, en combinant :
 - Les list comprehensions pour générer des listes de manière concise et expressive.
 - La recréation de la fonction intégrée filter.
 - L’utilisation des fonctions lambda pour définir des fonctions anonymes.
 - La validation et la manipulation des arguments passés au script.

L’objectif est de comprendre comment manipuler des séquences de données et appliquer des filtres de manière pythonique.

---

## Notions clés

### 1. List Comprehension

Une list comprehension est une syntaxe compacte pour créer des listes en Python, souvent utilisée pour filtrer ou transformer des éléments d’une séquence.

#### Syntaxe :

```python
[expression for item in iterable if condition]
```
- expression : ce que vous voulez mettre dans la nouvelle liste.
- item : chaque élément de l’itérable.
- condition (optionnelle) : filtre pour inclure seulement certains éléments.

#### Exemples :

```python
# Filtrer les nombres pairs dans une liste
numbers = [1, 2, 3, 4, 5]
evens = [n for n in numbers if n % 2 == 0]  # [2, 4]

# Transformer une liste de mots en majuscules
words = ["hello", "world"]
upper_words = [w.upper() for w in words]  # ['HELLO', 'WORLD']
```
Les list comprehensions sont utilisées dans ft_filter pour recréer le comportement de filter.

### 2. Fonction filter

La fonction intégrée filter(function, iterable) retourne un itérateur contenant uniquement les éléments pour lesquels la fonction renvoie True.

#### Syntaxe :

```python
filter(fonction, iterable)
```
- fonction : Une fonction qui prend un élément de l'itérable en entrée et retourne True ou False. Si la fonction retourne True, l'élément est inclus dans le résultat.
- itérable : L'itérable à filtrer (liste, tuple, etc.).

#### Exemples :

```python
# Définir une fonction de test
def is_pair(n):
    return n % 2 == 0

# Liste d'entrée
nombres = [1, 2, 3, 4, 5, 6]

# Appliquer filter()
resultat = filter(is_pair, nombres)

# Convertir le résultat en liste pour l'afficher
print(list(resultat))  # Sortie : [2, 4, 6]

```
Si function est None, filter retourne tous les éléments évalués comme vrais.
ft_filter recrée ce comportement sans utiliser la fonction filter, avec une list comprehension.

### 3. Lambda

Une lambda est une fonction anonyme définie en une seule ligne, pratique pour le filtrage ou le tri rapide.

#### Syntaxe :

```python
lambda arguments: expression
```
- arguments : Les paramètres d'entrée de la fonction (comme pour une fonction classique).
- expression : Une expression qui est évaluée et retournée. Pas besoin d'utiliser return.

#### Exemples :

1. Lambda pour une condition simple
```python
# Lambda qui vérifie si un nombre est pair
est_pair = lambda n: n % 2 == 0

# Liste d'entrée
nombres = [1, 2, 3, 4, 5, 6]

# Utilisation de la lambda avec filter()
resultat = list(filter(est_pair, nombres))
print(resultat)  # Sortie : [2, 4, 6]
```

2. Lambda pour trier une liste
```python
# Liste de tuples (nom, âge)
personnes = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# Trier par âge avec une lambda
personnes_triees = sorted(personnes, key=lambda x: x[1])
print(personnes_triees)
# Sortie : [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

```

3. Lambda pour une opération mathématique
```python
# Lambda qui calcule le carré d'un nombre
carre = lambda x: x ** 2

# Appliquer la lambda à une liste
nombres = [1, 2, 3, 4]
resultat = list(map(carre, nombres))
print(resultat)  # Sortie : [1, 4, 9, 16]

```

4. Lambda avec plusieurs arguments
```python
# Lambda qui additionne deux nombres
addition = lambda a, b: a + b
print(addition(3, 5))  # Sortie : 8
```
- Les lambdas sont souvent utilisées avec des fonctions comme filter(), map(), ou sorted() pour des opérations concises.
- Elles ne sont pas adaptées pour des fonctions complexes (plusieurs lignes, boucles, etc.).


--- 

## Résumé des notions abordées

| Notion                   | Description |
|--------------------------|-------------|
| **List comprehension**   | Permet de créer une liste de manière concise en filtrant ou transformant les éléments d’un iterable. |
| **Filter**               | Fonction intégrée qui retourne les éléments d’un iterable pour lesquels une condition est vraie. |
| **Lambda**               | Fonction anonyme définie en une seule ligne, idéale pour les expressions simples et le filtrage. |

---

# Exercice 07 – Objectif

## Objectif

Implémenter un programme utilisant un dictionnaire (dict) comme structure centrale afin de traduire une chaîne alphanumérique en code Morse.

Cet exercice met l’accent sur :

- L’utilisation d’un dictionnaire comme table de correspondance
- L’accès direct aux valeurs via leurs clés
- La séparation claire entre données (table Morse) et logique (traduction)

---

## Notions clés

### 1. Dictionnaire comme table de correspondance

Un dictionnaire permet d’associer une clé unique à une valeur.

Dans cet exercice :
- Clé → caractère alphanumérique (A-Z, 0-9, espace)
- Valeur → représentation en Morse (.-, --.., etc.)

#### Exemples :

```python
morse = {
    "A": ".-",
    "B": "-...",
    " ": "/"
}
#Accès direct :
morse["A"]  # ".-"
```

Autre exemple:

```python
" ".join(morse[c.upper()] for c in string)
```

Étapes :
- Parcours de chaque caractère
- Normalisation (majuscule)
- Accès direct à la valeur correspondante
- Assemblage de la chaîne finale

--- 

# Exercice 08 – ft_tqdm

## Objectif

Reproduire le comportement simplifié de la fonction tqdm en implémentant une fonction personnalisée :

```python
def ft_tqdm(lst: range) -> None:
```

Cet exercice met l’accent sur :

- L’utilisation du mot-clé yield
- La création d’un générateur
- L’affichage dynamique dans le terminal
- L’adaptation à la taille du terminal (os.get_terminal_size)

---

## Notions clés

### 1. Le générateur (yield)

Un générateur est une fonction qui produit des valeurs progressivement, sans stocker l’ensemble en mémoire.

Contrairement à return, yield :
- Suspend l’exécution de la fonction
- Conserve son état interne
- Reprend à l’instruction suivante lors de l’itération

#### Exemples :

```python
def generator(n):
    for i in range(n):
        yield i
```
#### Utilisation :
```python
for value in generator(3):
    print(value)
```
#### Pourquoi yield ?

ft_tqdm doit :

- Parcourir une séquence (range)
- Afficher dynamiquement la progression
- Continuer à fournir les éléments à la boucle appelante

***Le générateur permet donc :***
-D’afficher la barre de progression
-De ne pas casser la boucle for
-De reproduire le comportement natif de tqdm

### 2. Adaptation au terminal

L’utilisation de :
```python
os.get_terminal_size()
```
permet d’adapter dynamiquement la largeur de la barre de progression à la taille du terminal, rendant l’affichage plus robuste et professionnel.

--- 

## Logique globale

Pour chaque élément:


```python
for i in lst:
    # calcul progression
    # affichage
    yield i
```