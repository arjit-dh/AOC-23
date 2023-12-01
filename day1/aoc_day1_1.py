import re

def read_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().split('\n')
        return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

def part1():
    data = read_data('aoc_day1_1.txt')
    total = 0
    for line in data:
        digits = [char for char in line if char.isnumeric()]
        if len(digits) == 1:
            digits.append(digits[0])
        calibration = digits[0] + digits[-1]
        total += int(calibration)
    return total

def part2():
    data = read_data('aoc_day1_1.txt')
    total = 0

    digit_words = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
        'eno': '1', 'owt': '2', 'eerht': '3', 'ruof': '4', 'evif': '5', 'xis': '6', 'neves': '7', 'thgie': '8', 'enin': '9'
    }
    digit_words.update({str(i): str(i) for i in range(10)})

    numbers = re.compile("|".join(digit_words))

    for line in data:
        digits = numbers.findall(line)
        first_digit = digit_words[digits[0]] if digits else '0'
        digits_reverse = numbers.findall(''.join(list(reversed(line))))
        second_digit = digit_words[digits_reverse[0]] if digits_reverse else '0'
        calibration = first_digit + second_digit
        total += int(calibration)

    return total

if __name__ == '__main__':
    print(part1())
    print(part2())