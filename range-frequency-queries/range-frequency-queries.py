class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.nums = defaultdict(list)
        for i,j in enumerate(arr):
            self.nums[j].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        i = bisect.bisect(self.nums[value], left - 1)
        j = bisect.bisect(self.nums[value], right)
        return j - i

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)