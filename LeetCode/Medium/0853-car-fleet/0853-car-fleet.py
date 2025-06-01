class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        cars = sorted(range(len(position)), key=lambda idx: position[idx])
        print(cars)
        fleet, ctime = 0, 0
        for car in cars[::-1]:
            timetoreach = (target - position[car]) / speed[car]

            if timetoreach > ctime:
                fleet +=1
                ctime = timetoreach
        return fleet

