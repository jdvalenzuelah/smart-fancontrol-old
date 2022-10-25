
SPECIAL_CHARS = '`!@#$%^&*()-_+={}|[]\\;\':",.<>?/ '

def scape_str(str: str) -> str:
    return ''.join([c if c not in SPECIAL_CHARS else f'\{c}' for c in str])
