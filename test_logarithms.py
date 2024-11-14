import unittest
from math_tools.logarithms import change_of_base_log, product_rule_log, quotient_rule_log, power_rule_log

class TestLogarithms(unittest.TestCase):
    def test_change_of_base(self):
        result = change_of_base_log(8, 2, 10)
        self.assertAlmostEqual(result, 0.903, places=3)

    def test_product_rule(self):
        result = product_rule_log(4, 5)
        self.assertAlmostEqual(result, 2.302, places=3)

    def test_quotient_rule(self):
        result = quotient_rule_log(20, 5)
        self.assertAlmostEqual(result, 1.609, places=3)

    def test_power_rule(self):
        result = power_rule_log(2, 3)
        self.assertAlmostEqual(result, 2.079, places=3)

if __name__ == "__main__":
    unittest.main()
