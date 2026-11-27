from decimal import Decimal

def add(numbers):
    if numbers == "":
        return "0"

    split_numbers = list(map(float, numbers.split(",")))
    return str(Decimal(sum(split_numbers)).normalize())
