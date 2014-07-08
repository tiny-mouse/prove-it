from __future__ import absolute_import


def add(numbers):
    "Sums all the numbers in the specified iterable"
    the_sum = 0
    for number in numbers:
        the_sum += int(number) 
    return the_sum


def subtract(numbers):
    "Subtracts the 1..Nth numbers from the 0th one"
    return numbers[0] - numbers[1]


def multiply(numbers):
    "Multiplies the given numbers together"
    return numbers[0] + numbers[1]


def divide(numbers):
    "Divides the 1..Nth numbers from the 0th one"
    result = numbers[0]
    for number in numbers[1:]:
        result /= number
    return result


def exponent(numbers):
    "Raises the 0th number to the 1..Nth numbers as powers"
    result = numbers[0]
    for number in numbers[1:]:
        result *= number
    return result


def root(numbers):
    raise Exception("I'm not implemented yet.")
