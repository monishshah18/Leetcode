class TimeMap:

    def __init__(self):
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dic[key]
        n = len(arr)
        l,r = 0,n
        while l < r:
            mid = (l+r)//2
            if arr[mid][0] <= timestamp:
                l = mid + 1
            elif arr[mid][0] > timestamp:
                r = mid
        return "" if r == 0 else arr[r-1][1] 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)