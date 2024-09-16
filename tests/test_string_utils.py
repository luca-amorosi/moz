from moz import string_utils as str_ut

SEPARATORS = "_.-/| "


def test_prefix():
    # Supposed to find a prefix.
    prefix = "prefix"
    for sep in SEPARATORS:
        string = f"name{sep}other"
        assert "prefix" == str_ut.prefix(f"{prefix}{sep}{string}", sep)
