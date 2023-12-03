import regex as re

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def partOne(input: list[str]) -> int:
    sum = 0
    for line in input:
        digits = re.sub('[^\d]', '', line)
        res = int(digits[0::len(digits) - 1]) if len(digits) > 1 else int(digits * 2)
        sum += res
    return sum

def partTwo(input: list[str]) -> int:
    sum = 0
    for line in input:
        nums = {}
        for i, char in enumerate(line):
            if char.isdigit():
                nums.setdefault(char, []).append(i)
              
        for key in digits.keys():
            if key in line:
                iters = re.finditer(key, line)
                indices = [i.start() for i in iters]
                nums.setdefault(digits[key], []).extend(indices)

        min_index, max_index = float('inf'), float('-inf')
        first_char, second_char = '', ''
        for key, val in nums.items():
            min_val, max_val = min(val), max(val)
            if min_val < min_index:
                min_index, first_char = min_val, key
            if max_val > max_index:
                max_index, second_char = max_val, key

        result = int(first_char + second_char)
        sum += result
    return sum
    
if __name__ == "__main__":
    file = open("data/day1.txt", "r")
    puzzle_input = file.readlines()
    
    sum = partOne(puzzle_input)
    print(sum)
    
    sum2 = partTwo(puzzle_input)
    print(sum2)