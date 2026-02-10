# Introduction aux bases du langage de programmation Python - **Day One**

## Exercice 00 : Premier script Python

Cet exercice a pour objectif de comprendre les **différences et applications** des principales structures de données en Python :
- les listes
- les tuples
- les ensembles (set)
- les dictionnaires (dict)

---

## Définition des structures de données Python

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

### Remarque

- Une **liste est mutable**, c’est-à-dire que l’on peut y apporter n’importe quelle modification après sa création.

---
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

