import re 


def validate_size_str(size: str) -> bool:
    """Validate size(memory, storage) string."""
    valid_units = ["KB", "MB", "GB", "TB"]

    # Regular expression to match the format: digits followed by valid units
    pattern = re.compile(r"^\d+([KMG]B|TB)$", re.IGNORECASE)
    
    if not pattern.match(size):
        return False
    
    # Extract the unit from the string
    unit = size[-2:].upper()
    
    return unit in valid_units