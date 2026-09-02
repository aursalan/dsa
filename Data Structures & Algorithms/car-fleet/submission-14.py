class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)
        fleet = 1
        stack = []
        stack.append((target-cars[0][0])/cars[0][1])

        for i in range(1, len(cars)):
            current_time = (target-cars[i][0])/cars[i][1]
            if current_time <= stack[-1]:
                continue
            else:
                fleet+=1
                stack.append(current_time)
        
        return fleet


            
