class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = list(zip(position, speed))
        position_speed.sort(reverse=True)
        stack = []
        for pos, spd in position_speed:
            time = (target - pos) / spd
            if not stack:
                stack.append(time)
            elif stack[-1] < time:
                stack.append(time)
        

        return len(stack)