# Introduction aux bases du langage de programmation Python

**Day One**

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
