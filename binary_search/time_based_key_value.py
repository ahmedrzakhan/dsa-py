# https://leetcode.com/problems/time-based-key-value-store/

# TC: set: O(1), get: O(log N) where N is the number of timestamps for that key
# SC: O(N) where N is the total number of key-timestamp-value pairs

class TimeMap:
    def __init__(self):
        # Initialize a dictionary to store key -> list of [timestamp, value] pairs
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If key doesn't exist, create an empty list
        if key not in self.store:
            self.store[key] = []
        # Append the [timestamp, value] pair
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # If key doesn't exist, return empty string
        if key not in self.store:
            return ""

        # Binary search to find the largest timestamp <= given timestamp
        values = self.store[key]
        print("values", values)
        L, R = 0, len(values) - 1

        # If timestamp is smaller than the first entry, return empty string
        if values[0][0] > timestamp:
            return ""

        # If timestamp is larger than or equal to the last entry, return last value
        if values[-1][0] <= timestamp:
            return values[-1][1]

        # Binary search
        while L <= R:
            mid = (L + R) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                L = mid + 1
            else:
                R = mid - 1

        # Return the value at right (largest timestamp <= given timestamp)
        return values[R][1]


timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))  # Should return "bar"
print(timeMap.get("foo", 3))  # Should return "bar"
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))  # Should return "bar2"
print(timeMap.get("foo", 5))  # Should return "bar2"