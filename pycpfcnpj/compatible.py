import sys
import string


def clear_punctuation(document):
    """Remove from document all pontuation signals."""
    document = str(document)
    if sys.version_info[0] < 3:
        return document.translate(None, string.punctuation)
    else:
        return document.translate(str.maketrans("", "", string.punctuation))
