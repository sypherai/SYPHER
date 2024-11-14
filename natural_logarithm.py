import math

def natural_log(value):
    """Calculate the natural logarithm (base e) of a value."""
    if value <= 0:
        raise ValueError("Value must be greater than 0.")
    return math.log(value)

def exponential_from_ln(log_value):
    """Calculate the original number from a natural logarithm."""
    return math.exp(log_value)
