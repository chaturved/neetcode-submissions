class CountSquares:

    def __init__(self):
        self.freq = defaultdict(int)
        self.max_xy = 0

    def add(self, point: List[int]) -> None:
        x, y = point
        self.max_xy = max(self.max_xy, x, y)
        self.freq[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        print(self.max_xy)
        x, y = point
        total_count = 0

        for d in range(1, self.max_xy + 1):
            for sx in (1, -1):
                for sy in (1, -1):
                    p1 = (x + sx * d, y)
                    p2 = (x, y + sy * d)
                    p3 = (x + sx * d, y + sy * d)
                    if p1 in self.freq and p2 in self.freq and p3 in self.freq:
                        total_count += self.freq[p1] * self.freq[p2] * self.freq[p3]

        return total_count