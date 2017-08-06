import six
import string


def clear_punctuation(document):
    """Remove from document all pontuation signals."""
    if six.PY2:
        return document.translate(None, string.punctuation)
    else:
        return document.translate(str.maketrans("", "", string.punctuation))
