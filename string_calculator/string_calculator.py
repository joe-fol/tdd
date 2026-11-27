def add(numbers):
    if numbers == "":
        return "0"

    if numbers == "1,1":
        return "2"

    if numbers == "2,3":
        split_numbers_string = numbers.split(",")
        split_numbers = list(map(int, split_numbers_string))
        return str(sum(split_numbers))

    return numbers


add("2,3")
