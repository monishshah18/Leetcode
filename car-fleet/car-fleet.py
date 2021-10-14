class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos,sp in sorted(zip(position,speed))[::-1]:
            dist = target - pos
            if not stack:
                stack.append(dist/sp)
            elif dist/sp > stack[-1]:
                stack.append(dist/sp)
        return len(stack)
                