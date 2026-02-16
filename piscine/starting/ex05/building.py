import sys
import string


def count_string_infos(obj: str):
    """
        count for string:
            - nb of characters
            - nb of characters that are considered uppercase
            - nb of characters that are considered lowercase
            - nb of characters that are considered punctuation
            - nb of characters that are considered whitespace
            - nb of characters that are considered digits
    """
    nb_char = sum(1 for c in obj if c in string.printable)
    print(f"The text contains {nb_char} characters:")
    print(sum(1 for c in obj if c.isupper()), "upper letters")
    print(sum(1 for c in obj if c.islower()), "lower letters")
    print(sum(1 for c in obj if c in string.punctuation), "punctuation marks")
    print(sum(1 for c in obj if c in string.whitespace), "spaces")
    print(sum(1 for c in obj if c in string.digits), "digits")


def test_arg(obj: list[str]):
    """
        testing number of arguments:
            - 0 : input for adding arg
            - > 1 : AssertError
    """
    if len(obj) == 2:
        return obj[1]
    if len(obj) == 1:
        print("Please enter a string :")
        tmp = input()
        while len(tmp) == 0:
            print("Please enter a string :")
            tmp = input()
        return tmp
    assert len(obj) == 2, "AssertionError: more than one argument is provided"


def main():
    try:
        string = test_arg(sys.argv)
        count_string_infos(string)
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
