class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ones_left = 1 if boxes[0] == '1' else 0
        ones_right = 0
        total = 0
        for i in range(1, n):
            if boxes[i] == '1':
                ones_right += 1
                total += i
        
        answer = [0] * n
        answer[0] = total
        for i in range(1, n):
            total += ones_left - ones_right
            if boxes[i] == '1':
                ones_right -= 1
                ones_left += 1
            answer[i] = total
        return answer