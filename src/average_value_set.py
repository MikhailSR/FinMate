import pandas
import re


def calcultion_average_value_set(text: str):
    numbers = [re.sub(r'[^\d,.-]', '', x) for x in text.split()]
    numbers = [float(s.replace(',', '.')) for s in numbers]
    nums = pandas.Series(numbers)
    return round(nums.mean(), 2)
