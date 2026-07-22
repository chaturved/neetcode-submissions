class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        min_heap = list(freq.keys())
        heapq.heapify(min_heap)

        while min_heap:
            if freq[min_heap[0]] == 0:
                heapq.heappop(min_heap)
                continue
            
            start = heapq.heappop(min_heap)
            for num in range(start, start + groupSize):
                if freq[num] == 0:
                    return False
                freq[num] -= 1
            
            if freq[start] > 0:
                heapq.heappush(min_heap, start)
        
        return True
            
            


        