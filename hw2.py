import re
from typing import Callable

# TASK 2

def generator_numbers(text: str):
    number_pattern = re.compile(r'\b\d+\.\d+\b')
    
    for match in number_pattern.finditer(text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")
