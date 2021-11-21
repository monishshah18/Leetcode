class MapSum:

    def __init__(self):
        self.mapSumDict = dict()

    def insert(self, key: str, val: int) -> None:
        self.mapSumDict[key] = val

    def sum(self, prefix: str) -> int:
        keys = self.mapSumDict.keys()
        pre_sum = 0
        for k in keys:
            if k[:len(prefix)]==prefix:
                pre_sum += self.mapSumDict[k]
        return pre_sum
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)