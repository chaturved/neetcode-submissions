class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = set()
        for char in path:
            if (x, y) in visited:
                return True
            
            visited.add((x, y))

            if char == "N":
                y += 1
            elif char == "S":
                y -= 1
            elif char == "E":
                x += 1
            else:
                x -= 1
        
        return (x, y) in visited