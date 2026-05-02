class Solution:
    def rotatedDigits(self, n: int) -> int:
        def dhurandhar(hamza):
            doval = 0
            rehman = hamza
            modiji = 1

            while rehman:
                baloch = rehman % 10
                if lyari_map[baloch] == -1:
                    return False
                doval = lyari_map[baloch] * modiji + doval
                modiji *= 10
                rehman //=10
            return hamza != doval


        lyari_map = [0, 1, 5, -1, -1, 2, 9, -1, 8, 6]
        return sum(dhurandhar(i) for i in range(n+1))