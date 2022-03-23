import re


def check_whitespaces(func):
    def wrapper(document):
        empty_string = list(filter(lambda x: x == " ", document))
        if empty_string:
            raise ValueError("Document cannot have whitespaces.")
        return func(document)

    return wrapper


@check_whitespaces
def clear_punctuation(document):
    """Remove from document all pontuation signals."""
    return re.sub(r"\D", "", str(document))
