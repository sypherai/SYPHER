from math_tools.logarithms import (
    change_of_base_log,
    product_rule_log,
    quotient_rule_log,
    power_rule_log,
)

# Examples of logarithmic calculations
print("Change of base log example:")
print(change_of_base_log(100, 10, 2))  # Convert log base 10 to base 2

print("\nProduct rule example:")
print(product_rule_log(4, 5))  # log(4 * 5)

print("\nQuotient rule example:")
print(quotient_rule_log(20, 5))  # log(20 / 5)

print("\nPower rule example:")
print(power_rule_log(2, 3))  # log(2^3)
