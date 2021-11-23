class Fancy:

    def __init__(self):
        self.mul, self.add, self.mod = 1, 0, 10**9+7
        self.nums = []

    def append(self, val: int) -> None:
        self.nums.append([val, self.mul, self.add])

    def addAll(self, inc: int) -> None:
        self.add += inc

    def multAll(self, m: int) -> None:
        self.mul = self.mul * m % self.mod
        self.add = self.add * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.nums):
            return -1
        i, i_mul, i_add = self.nums[idx]
        inverse = pow(i_mul, self.mod-2, self.mod)
        ratio = self.mul * inverse
        return (i * ratio + self.add - i_add * ratio) % self.mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)