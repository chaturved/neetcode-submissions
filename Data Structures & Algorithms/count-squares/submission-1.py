class CountSquares:

    def __init__(self):
        self.freq = defaultdict(int)
        self.col = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.freq[(x, y)] += 1
        self.col[x].add(y)

    def count(self, point: List[int]) -> int:
        x, y = point
        all_possible_y = self.col[x]
        total_count = 0
        for y_dash in all_possible_y:
            if y_dash == y:
                continue
            d = abs(y - y_dash)
            for i in (-1, 1):
                p2 = (x + i * d, y)
                p3 = (x + i * d, y_dash)
                if p2 in self.freq and p3 in self.freq:
                    total_count += self.freq[(x, y_dash)] * self.freq[p2] * self.freq[p3]

        return total_count