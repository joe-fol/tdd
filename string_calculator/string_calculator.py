from decimal import Decimal

def add(numbers):
    if numbers == "":
        return "0"

    split_numbers = [Decimal(number) for number in numbers.split(",")]
    return str(sum(split_numbers))
