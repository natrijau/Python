# Introduction aux bases du langage de programmation Python

## Day one

## Exercice 00 : premier script python

Différences et applications des listes, tuple, set et dict en Python

## Comparaison des structures de données Python

| Caractéristique      | Liste             | Tuple             | Ensemble (Set)     | Dictionnaire         |
|----------------------|-------------------|-------------------|--------------------|----------------------|
| Type                 | Non homogène      | Non homogène      | Non homogène       | Non homogène         |
| Contenu              | Éléments          | Éléments          | Éléments           | Paires clé-valeur    |
| Syntaxe              | `[ ]`             | `( )`             | `{ }`              | `{ clé: valeur }`    |
| Doublons autorisés   | ✅ Oui            | ✅ Oui            | ❌ Non             | ❌ Non (clés)        |
| Imbrication          | ✅ Oui            | ✅ Oui            | ✅ Oui             | ✅ Oui               |
| Exemple              | `[1, 2, 3, 4, 5]` | `(1, 2, 3, 4, 5)` | `{1, 2, 3, 4, 5}`  | `{1: "a", 2: "b"}`   |
| Fonction de création | `list()`          | `tuple()`         | `set()`            | `dict()`             |
| Mutabilité           | ✅ Mutable        | ❌ Immuable       | ✅ Mutable         | ✅ Mutable           |
| Ordonnée             | ✅ Oui            | ✅ Oui            | ❌ Non             | ✅ Oui (Python ≥ 3.7)|
| Structure vide       | `l = []`          | `t = ()`          | `s=set(); b=set(a)`| `d = {}`             |

* Une liste est mutable, c'est-à-dire que l'on peut y apporter n'importe quelle modification.