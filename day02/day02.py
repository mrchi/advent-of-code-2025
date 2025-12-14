import pathlib
from typing import Callable


def sum_of_invalid_ids(line: str, is_invalid_id_func: Callable[[int], bool]):
    invalid_ids = []
    for range_str in line.strip().split(","):
        range_left, range_right = range_str.split("-")
        for num in range(int(range_left), int(range_right) + 1):
            if is_invalid_id_func(num):
                invalid_ids.append(num)
    return sum(invalid_ids)


def is_invalid_id1(num: int) -> bool:
    num_string = str(num)
    num_length = len(num_string)
    return (
        num_length % 2 == 0
        and num_string[: num_length // 2] == num_string[num_length // 2 :]
    )


def is_invalid_id2(num: int) -> bool:
    num_string = str(num)
    num_length = len(num_string)
    for part in [2, 3, 5, 7, 11]:
        if (
            num_length % part == 0
            and num_string[: num_length // part] * part == num_string
        ):
            return True
    else:
        return False


def test_sum_of_invalid_ids():
    line = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    assert sum_of_invalid_ids(line, is_invalid_id1) == 1227775554
    assert sum_of_invalid_ids(line, is_invalid_id2) == 4174379265


def main():
    with open(pathlib.Path(__file__).parent / "input.txt", "r") as f:
        line = f.readline()
    print(sum_of_invalid_ids(line, is_invalid_id1))
    print(sum_of_invalid_ids(line, is_invalid_id2))


if __name__ == "__main__":
    main()
