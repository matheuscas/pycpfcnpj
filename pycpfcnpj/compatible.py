def clear_punctuation(document: str) -> str:
    """Remove from document all pontuation signals."""
    return document.translate(str.maketrans({".": None, "-": None, "/": None}))
