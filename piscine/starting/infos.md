# Introduction aux bases du langage de programmation Python - **Day One**

Ce module introduit les fondamentaux du langage Python à travers 9 exercices progressifs.
Chaque exercice met en pratique des concepts essentiels : structures de données, gestion du temps, types, assertions, manipulation de chaînes, fonctions anonymes, générateurs et plus encore.


---

# Table des matières

- [Exercice 00 – Structures de données](#exercice-00--Premier-script-Python)
- [Exercice 01 – Gestion du temps](#exercice-01--gestion-du-temps)
- [Exercice 02 – Typage dynamique](#exercice-02--typage-dynamique)
- [Exercice 03 – Null-like values](#exercice-03--null-like-values)
- [Exercice 04 – Arguments & Assertions](#exercice-04--arguments--assertions)
- [Exercice 05 – Analyse de texte](#exercice-05--analyse-de-texte)
- [Exercice 06 – Filter & Lambda](#exercice-06--filter--lambda)
- [Exercice 07 – Morse Translator](#exercice-07--morse-translator)
- [Exercice 08 – Barre de progression](#exercice-08--barre-de-progression)

---


# Exercice 00 - Premier script Python

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

# Exercice 01 – Gestion du temps

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