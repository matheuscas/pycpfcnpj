import string
import six


def clear_punctuation(document):
    """Remove from document all pontuation signals."""
    document = str(document)

    if six.PY2:
        return document.translate(None, string.punctuation)
    else:
        return document.translate(str.maketrans("", "", string.punctuation))
