calibration_values = []
total_calibration = 0

VALID_DIGITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

part = 2

def get_nums(text: str) -> list:
    nums = []

    if part == 1:
        for c in text:
            try:
                nums.append(int(c))
            except ValueError:
                print("Not a number.")
    else:
        word = ""

        for c in text:
            try:
                nums.append(int(c))
                word = ""
            except ValueError:
                word += c
                for digit in VALID_DIGITS:
                    if digit in word:
                        nums.append(VALID_DIGITS[digit])
                        word = "" + c

    return nums

with open("input.txt") as f:
    for line in f:
        nums = get_nums(line.strip())

        calibration_value = str(nums[0]) + str(nums[-1])
        calibration_values.append(int(calibration_value))
        print(line.strip() + f" -> {nums} = {calibration_value}")

total_calibration = sum(calibration_values)
print("\nTotal calibration values: " + str(total_calibration))
