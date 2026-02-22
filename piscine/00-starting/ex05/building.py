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
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    print(f"The text contains {len(obj)} characters:")
    print(sum(c.isupper() for c in obj), "upper letters")
    print(sum(c.islower() for c in obj), "lower letters")
    print(sum(c in punctuation_chars for c in obj), "punctuation marks")
    print(sum(c.isspace() for c in obj), "spaces")
    print(sum(c.isdigit() for c in obj), "digits")


def test_arg(obj: list[str]):
    """
        testing number of arguments:
            - 0 : input for adding arg
            - > 1 : AssertError
    """
    if len(obj) == 2:
        return obj[1]
    if len(obj) == 1:
        print("What is the text to count?")
        tmp = sys.stdin.readline()
        return tmp
    assert len(obj) == 2, "AssertionError: more than one argument is provided"


def main():
    try:
        string = test_arg(sys.argv)
        count_string_infos(string)
    except KeyboardInterrupt:
        sys.exit()
    except EOFError:
        sys.exit()
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
