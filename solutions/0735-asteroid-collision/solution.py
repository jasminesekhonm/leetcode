class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        n = len(asteroids)

        stack = []

        for a in asteroids:
            alive = True
            while alive and stack and a < 0 and stack[-1] > 0:
                if stack[-1] < -a:
                    stack.pop()
                elif stack[-1] == -a:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(a)
        return stack
            






