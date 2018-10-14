import re


def clear_punctuation(document):
    """Remove from document all pontuation signals."""
    return re.sub('\D', '', str(document))
