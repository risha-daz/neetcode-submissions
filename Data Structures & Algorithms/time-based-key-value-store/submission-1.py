class TimeMap:

    def __init__(self):
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps.keys():
            self.timestamps[key] = [(timestamp, value)]
        else:
            self.timestamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps: return ""

        timestamps = self.timestamps[key]
        left = 0
        right = len(timestamps) - 1
        res = ""

        while left<=right:
            
            mid = (left + right) //2
            if timestamps[mid][0] == timestamp: 
                res = timestamps[mid][1]
                break
            if timestamps[mid][0] < timestamp:
                res = timestamps[mid][1]
                left = mid + 1
            else: right = mid - 1
        return res

        
        
