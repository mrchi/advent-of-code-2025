import pathlib
from typing import Literal


class Dial:
    def __init__(self) -> None:
        self.pointing = 50
        self.pointed_zero_times = 0
        self.passed_zero_times = 0

    def dial(self, clicks: int, direction: Literal[-1, 1]):
        for _ in range(clicks):
            self.pointing += direction
            self.pointing %= 100

            if self.pointing == 0:
                self.passed_zero_times += 1
        if self.pointing == 0:
            self.pointed_zero_times += 1

    def handle(self, commands: list[str]):
        for command in commands:
            clicks = int(command[1:])
            direction = -1 if command[0] == "L" else 1
            self.dial(clicks, direction)
        return self.pointed_zero_times, self.passed_zero_times


def test_dial():
    commands = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    pointed_zero_times, pass_zero_times = Dial().handle(commands)
    assert pointed_zero_times == 3
    assert pass_zero_times == 6


def main():
    with open(pathlib.Path(__file__).parent / "input.txt", "r") as f:
        commands = [line.strip() for line in f.readlines() if line.strip()]
    print(Dial().handle(commands))


if __name__ == "__main__":
    main()
