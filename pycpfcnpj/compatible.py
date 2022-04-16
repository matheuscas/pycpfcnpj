def clear_punctuation(document):
    """Remove from document all pontuation signals."""
    return document.translate(str.maketrans({".": None, "-": None, "/": None}))
