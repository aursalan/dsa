class TimeMap:

    def __init__(self):
        self.time_Map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_Map:
            self.time_Map[key] = [[],[]]

        self.time_Map[key][0].append(timestamp)
        self.time_Map[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time_Map:
            return ""
        
        timestamps, values = self.time_Map[key]

        left = 0
        right = len(timestamps)-1
        result = ""

        while left<=right:

            mid = (left+right)//2

            if timestamps[mid] <= timestamp:
                result = values[mid]
                left = mid + 1
            else:
                right = mid - 1
        
        return result