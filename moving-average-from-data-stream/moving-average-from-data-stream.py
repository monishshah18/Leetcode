class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.deque(maxlen=size)

    def next(self, val: int) -> float:
        self.queue.append(val)
        return float(sum(self.queue)/len(self.queue))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)