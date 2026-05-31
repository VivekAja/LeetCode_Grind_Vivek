class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for i in range(len(asteroids)):
            if asteroids[i] <= mass:
                mass+= asteroids[i]
                asteroids[i] = 0
        return sum(asteroids) == 0
