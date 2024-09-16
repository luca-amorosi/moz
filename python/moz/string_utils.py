def prefix(string: str, separator: str = "_") -> str | None:
    """Returns the prefix of any string. Prefix is considered as the first set
    of characters before the separator. If not any separator, return None.

    :param string: String.
    :param separator: Separator between character chains. Default is "_".

    :return: String prefix.
    """
    if separator not in string:
        return None

    return string[: len(string.split(separator)[0])]
