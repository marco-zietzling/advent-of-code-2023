print("advent of code 2023 - day 1")


def read_input():
    """
    Reads the input from a file and returns a list of entries.

    Returns:
        list: A list of strings, where each string is a line from the file with leading and trailing whitespace removed.
    """
    entries = list()

    with open("day01/input.txt") as file:
        for line in file:
            entries.append(str(line).strip())
    return entries


def sum_all_entries(entries):
    """
    Calculate the sum of all entries.

    Args:
        entries (List[str]): A list of string entries.

    Returns:
        int: The sum of all numbers consisting of the first and last digit extracted from each entry.
    """
    total_sum = 0
    for entry in entries:
        digits = [int(i) for i in entry if i.isdigit()]
        number = str(digits[0]) + str(digits[-1])
        total_sum += int(number)
    return total_sum


entries = read_input()
sum = sum_all_entries(entries)

# result = 54968
print(f"part 1: result = {str(sum)}")

replaced_entries = list()
for entry in entries:
    entry = entry.replace("one", "o1e")
    entry = entry.replace("two", "t2o")
    entry = entry.replace("three", "t3e")
    entry = entry.replace("four", "f4r")
    entry = entry.replace("five", "f5e")
    entry = entry.replace("six", "s6x")
    entry = entry.replace("seven", "s7n")
    entry = entry.replace("eight", "e8t")
    entry = entry.replace("nine", "n9e")
    replaced_entries.append(entry)

sum = sum_all_entries(replaced_entries)

# result = 54094
print(f"part 2: result = {str(sum)}")
