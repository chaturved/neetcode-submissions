class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        
        prefix = [0] * n
        count = 0
        for i in range(1, n):
            count += 1 if boxes[i - 1] == '1' else 0
            prefix[i] = prefix[i - 1] + count
        
        suffix = [0] * n
        count = 0
        for i in range(n - 2, -1, -1):
            count += 1 if boxes[i + 1] == '1' else 0
            suffix[i] = suffix[i + 1] + count
        
        return [p + s for p, s in zip(prefix, suffix)]