from rig.libs import string_utils as str_ut

SEPARATORS = "_.-/| "


def test_prefix():
    # Supposed to find a prefix.
    prefix = "prefix"
    for sep in SEPARATORS:
        string = f"name{sep}other"
        assert "prefix" == str_ut.prefix(f"{prefix}{sep}{string}", sep)

    # No prefix found.
    assert None == str_ut.suffix("prefix_name_other", ".")


def test_suffix():
    # Supposed to find a suffix.
    suffix = "suffix"
    for sep in SEPARATORS:
        string = f"name{sep}other"
        assert "suffix" == str_ut.suffix(f"{string}{sep}{suffix}", sep)

    # No suffix found.
    assert None == str_ut.suffix("name_other_suffix", ".")
