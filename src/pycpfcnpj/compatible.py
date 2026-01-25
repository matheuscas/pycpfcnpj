def check_special_characters(func):
    def wrapper(document):
        cleared_doc = clear_punctuation(document)
        invalid_chars = [i for i in cleared_doc if not (i.isdigit() or i.isalpha())]
        return False if invalid_chars else func(document)

    return wrapper


def clear_punctuation(document):
    """Remove from document all pontuation signals."""
    return document.translate(str.maketrans({".": None, "-": None, "/": None}))
