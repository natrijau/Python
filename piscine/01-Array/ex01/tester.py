from array2D import slice_me

family = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]
]

def test_assert(family, start, end, description):
    print(f"\n--- Test: {description} ---")
    try:
        result = slice_me(family, start, end)
        print("Result:", result)
    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Other Error:", e)
# sujet test
test_assert(family, 0, 2, "sujet test")
test_assert(family, 1, -2, "sujet test")
test_assert(family, 0, 4, "slice complet")
test_assert(family, 2, 10, "slice au-delà de la taille")
test_assert(family, -3, -1, "slice négatif")
test_assert(family, 0, 0, "slice vide")

# family vide
test_assert([], 0, 1, "family empty")

# family n'est pas une liste
test_assert("not a list", 0, 1, "family not a list")

# start n'est pas un int
test_assert([[1,2],[3,4]], "0", 1, "start not int")

# end n'est pas un int
test_assert([[1,2],[3,4]], 0, None, "end not int")

# family n'est pas 2D (élément non-liste)
test_assert([[1,2], 3], 0, 1, "family not 2D")

# rows pas de même longueur
test_assert([[1,2],[3,4,5]], 0, 2, "rows not same length")

# test valide pour comparaison
test_assert([[1,2],[3,4]], 0, 2, "valid slice")