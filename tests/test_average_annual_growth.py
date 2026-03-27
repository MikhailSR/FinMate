import unittest
from src import average_annual_growth


class TestAverageAnnualGrowth(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(
            average_annual_growth.calculation_average_annual_growth(0.15, 7.85, 7), 93.4)


if __name__ == '__main__':
    unittest.main()
