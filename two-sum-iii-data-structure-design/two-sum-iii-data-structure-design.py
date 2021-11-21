class TwoSum:

    def __init__(self):
        self.nums = defaultdict(int)

    def add(self, number: int) -> None:
        self.nums[number] += 1

    def find(self, value: int) -> bool:
        for i in self.nums:
            complement = value - i
            if complement in self.nums:
                if (complement != i) or (complement==i and self.nums[i] >= 2):
                        return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)