import pathlib


def calc_sum_of_largest_joltage(battery_lines: list[str], selected_count: int):
    joltages = []
    for line in battery_lines:
        if not line:
            continue
        bank_joltages = [int(i) for i in line]

        joltage = 0
        for i in range(selected_count - 1, -1, -1):
            joltage_bit = max(bank_joltages[:-i] if i > 0 else bank_joltages)
            bank_joltages = bank_joltages[bank_joltages.index(joltage_bit) + 1 :]
            joltage += joltage_bit * 10**i
        joltages.append(joltage)

    return sum(joltages)


def test_calc_sum_of_largest_joltage():
    battery_lines = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    assert calc_sum_of_largest_joltage(battery_lines, 2) == 357


def main():
    with open(pathlib.Path(__file__).parent / "input.txt", "r") as f:
        battery_lines = [i.strip() for i in f.readlines() if i.strip()]
    print(calc_sum_of_largest_joltage(battery_lines, 2))
    print(calc_sum_of_largest_joltage(battery_lines, 12))


if __name__ == "__main__":
    main()
