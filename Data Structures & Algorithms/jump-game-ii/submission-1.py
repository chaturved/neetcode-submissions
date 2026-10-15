class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        queue = deque([0])
        dist = {0: 0}
        next_unvisited = 1

        while queue:
            curr = queue.popleft()

            if curr == n - 1:
                return dist[curr]

            reach = min(curr + 1 + nums[curr], n)

            for nxt in range(next_unvisited, reach):
                dist[nxt] = dist[curr] + 1
                queue.append(nxt)

            next_unvisited = max(next_unvisited, reach)

        return -1