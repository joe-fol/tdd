def add(numbers):
    if numbers == "":
        return "0"

    split_numbers = list(map(int, numbers.split(",")))
    return str(sum(split_numbers))
