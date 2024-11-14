import math

def change_of_base_log(value, base, new_base):
    """Calculate the logarithm of a value with a new base."""
    return math.log(value, new_base) / math.log(base, new_base)

def product_rule_log(x, y):
    """Apply the product rule for logarithms."""
    return math.log(x) + math.log(y)

def quotient_rule_log(x, y):
    """Apply the quotient rule for logarithms."""
    return math.log(x) - math.log(y)

def power_rule_log(base, power):
    """Apply the power rule for logarithms."""
    return power * math.log(base)
