class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)
        fleet = 1
        fleet_time = (target-cars[0][0])/cars[0][1]

        for i in range(1, len(cars)):
            current_time = (target-cars[i][0])/cars[i][1]
            if current_time <= fleet_time:
                continue
            else:
                fleet+=1
                fleet_time = current_time
        
        return fleet


            
