class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        for num, count in freq.items():
            heap.append((-count, num))
        heapq.heapify(heap)
        most_frequent = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            most_frequent.append(num)

        return most_frequent
