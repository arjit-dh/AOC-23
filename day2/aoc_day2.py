import re

ORIGINAL_RED, ORIGINAL_GREEN, ORIGINAL_BLUE = 12, 13, 14


def read_data(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().split('\n')
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []


def validate(total_red, total_green, total_blue):
    return not (total_red > ORIGINAL_RED or total_green > ORIGINAL_GREEN or total_blue > ORIGINAL_BLUE)


def get_game_number(game_string):
    match = re.search(r"Game (\d+):", game_string)
    return int(match.group(1)) if match else None


def get_color_pairs(game_string):
    return re.findall(r"(\d+) (\w+)", game_string)


def solution_1(color_pairs):
    total_red, total_green, total_blue = 0, 0, 0
    for number, color in color_pairs:
        if color == 'red':
            total_red = int(number)
        elif color == 'green':
            total_green = int(number)
        elif color == 'blue':
            total_blue = int(number)
        if not validate(total_red, total_green, total_blue):
            return False
    return True


def part1(data):
    total = 0
    for game_string in data:
        game_number = get_game_number(game_string)
        if game_number is not None:
            color_pairs = get_color_pairs(game_string)
            if solution_1(color_pairs):
                total += game_number
    return total


def solution_2(color_pairs):
    max_red, max_green, max_blue = 0, 0, 0
    for number, color in color_pairs:
        if color == 'red':
            max_red = max(max_red, int(number))
        elif color == 'green':
            max_green = max(max_green, int(number))
        elif color == 'blue':
            max_blue = max(max_blue, int(number))
    return max_red * max_green * max_blue


def part2(data):
    total = 0
    for game_string in data:
        color_pairs = get_color_pairs(game_string)
        total += solution_2(color_pairs)
    return total


if __name__ == '__main__':
    game_data = read_data('input_day2.txt')
    print(part1(game_data))
    print(part2(game_data))
