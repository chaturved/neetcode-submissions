class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        {1: 1, 2: 2, 3: 2, 4: 2, 5: 1}
        """
        freq = Counter(hand)
        heap = list(freq.keys())
        heapq.heapify(heap)
        while heap:
            start = heap[0]
            for num in range(start, start + groupSize):
                if freq[num] == 0:
                    return False
                
                freq[num] -= 1
                if freq[num] == 0:
                    heapq.heappop(heap)
        
        return True
                    
