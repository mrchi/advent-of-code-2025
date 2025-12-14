import pathlib


class PaperRolls:
    def __init__(self, lines: list[str]) -> None:
        self.coords = [list(line.strip()) for line in lines]
        self.height = len(self.coords)
        self.width = len(self.coords[0])

    def get_valid_neighbours(self, h: int, w: int) -> list[str]:
        return [
            self.coords[h1][w1]
            for h1, w1 in [
                (h - 1, w - 1),
                (h - 1, w),
                (h - 1, w + 1),
                (h, w - 1),
                (h, w + 1),
                (h + 1, w - 1),
                (h + 1, w),
                (h + 1, w + 1),
            ]
            if 0 <= h1 < self.height and 0 <= w1 < self.width
        ]

    def get_accessible_rolls(self) -> list[tuple[int, int]]:
        accessible_rolls = []
        for h in range(self.height):
            for w in range(self.width):
                if self.coords[h][w] != "@":
                    continue

                neighbours = self.get_valid_neighbours(h, w)
                if neighbours.count("@") < 4:
                    accessible_rolls.append((h, w))
        return accessible_rolls

    def repeat(self) -> int:
        total_count = 0
        while accessible_rolls := self.get_accessible_rolls():
            for h, w in accessible_rolls:
                self.coords[h][w] = "x"
            total_count += len(accessible_rolls)
        return total_count


def test_paper_rolls():
    lines = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]
    assert len(PaperRolls(lines).get_accessible_rolls()) == 13
    assert PaperRolls(lines).repeat() == 43


def main():
    with open(pathlib.Path(__file__).parent / "input.txt", "r") as f:
        lines = [i.strip() for i in f.readlines() if i.strip()]
    print(len(PaperRolls(lines).get_accessible_rolls()))
    print(PaperRolls(lines).repeat())


if __name__ == "__main__":
    main()
