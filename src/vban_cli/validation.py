import re


def is_valid_time_string(type_, value: str) -> str:
    """Validate if the given string is a valid time format (HH:MM:SS)."""
    pattern = r'^(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)$'
    if not re.match(pattern, value):
        raise ValueError('Invalid time format. Expected HH:MM:SS.')
    return value
