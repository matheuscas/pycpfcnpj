def check_special_characters(func):
    def wrapper(document):
        not_digit = list(filter(lambda x: not x.isdigit(), clear_punctuation(document)))
        return False if not_digit else func(document)

    return wrapper


def clear_punctuation(document):
    """Remove from document all pontuation signals."""
    return document.translate(str.maketrans({".": None, "-": None, "/": None}))
