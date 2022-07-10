def check_special_characters(func):
    def wrapper(document):
        not_digit = [i for i in clear_punctuation(document) if not i.isdigit()]
        return False if not_digit else func(document)

    return wrapper


def clear_punctuation(document):
    """Remove from document all pontuation signals."""
    return document.translate(str.maketrans({".": None, "-": None, "/": None}))
