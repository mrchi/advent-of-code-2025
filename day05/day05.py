import pathlib


class InventoryManager:
    def __init__(self, content: str) -> None:
        self.ranges, self.ids = self.parse_content(content)

    @staticmethod
    def parse_content(content: str) -> tuple[list[tuple[int, int]], list[int]]:
        range_lines, id_lines = content.strip().split("\n\n")
        ranges = [
            tuple(int(i) for i in line.split("-")) for line in range_lines.splitlines()
        ]
        ids = [int(line) for line in id_lines.splitlines()]
        return ranges, ids

    def is_fresh(self, item_id: int) -> bool:
        for start, end in self.ranges:
            if start <= item_id <= end:
                return True
        else:
            return False

    def evaluate_inventory(self) -> int:
        return len([item_id for item_id in self.ids if self.is_fresh(item_id)])

    def get_fresh_ids_count(self) -> int:
        self.ranges.sort()

        new_ranges = [self.ranges[0]]
        for start, end in self.ranges[1:]:
            last_start, last_end = new_ranges[-1]
            if start <= last_end:
                new_ranges[-1] = (last_start, max(last_end, end))
            else:
                new_ranges.append((start, end))
        total_count = 0
        for start, end in new_ranges:
            total_count += end - start + 1
        return total_count


def test_inventory_manager():
    content = """\
    3-5
    10-14
    16-20
    12-18

    1
    5
    8
    11
    17
    32
    """
    manager = InventoryManager(content)
    assert manager.evaluate_inventory() == 3
    assert manager.get_fresh_ids_count() == 14


def main():
    with open(pathlib.Path(__file__).parent / "input.txt", "r") as f:
        content = f.read()
    manager = InventoryManager(content)
    print(manager.evaluate_inventory())
    print(manager.get_fresh_ids_count())


if __name__ == "__main__":
    main()
