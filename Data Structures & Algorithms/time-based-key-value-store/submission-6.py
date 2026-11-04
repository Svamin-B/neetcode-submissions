class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key, None) == None:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        high = len(self.store[key]) - 1
        low = 0
        value = ""

        while low <= high:
            mid = (low + high) // 2

            if self.store[key][mid][1] > timestamp:
                high = mid - 1
            else:
                value = self.store[key][mid][0]
                low = mid + 1

        return value