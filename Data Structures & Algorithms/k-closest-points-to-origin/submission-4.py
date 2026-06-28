class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0] ** 2 + point[1] ** 2
        
        def partition(l, r):
            pivot_dist = distance(points[r])
            store = l
            for i in range(l, r):
                if distance(points[i]) <= pivot_dist:
                    points[i], points[store] = points[store], points[i]
                    store += 1
            points[store], points[r] = points[r], points[store]
            return store
        
        l, r = 0, len(points) - 1
        pivot = -1
        while pivot != k - 1:
            pivot = partition(l, r)
            if pivot < k - 1:
                l = pivot + 1
            else:
                r = pivot - 1
        
        return points[:k]