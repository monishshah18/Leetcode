class StockPrice:

    def __init__(self):
        self.timestamp = {}
        self.maxTimeStamp = 0
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp: int, price: int) -> None:
        self.timestamp[timestamp] = price
        self.maxTimeStamp = max(self.maxTimeStamp, timestamp)
        
        heappush(self.minHeap, (price, timestamp))
        heappush(self.maxHeap, (-price, timestamp))
        

    def current(self) -> int:
        return self.timestamp[self.maxTimeStamp]
        

    def maximum(self) -> int:
        currPrice, currTimestamp = heappop(self.maxHeap)
        while -currPrice != self.timestamp[currTimestamp]:
            currPrice, currTimestamp = heappop(self.maxHeap)
        heappush(self.maxHeap, (currPrice, currTimestamp))
        return -currPrice

    def minimum(self) -> int:
        currPrice, currTimestamp = heappop(self.minHeap)
        while currPrice != self.timestamp[currTimestamp]:
            currPrice, currTimestamp = heappop(self.minHeap)
        heappush(self.minHeap, (currPrice, currTimestamp))
        return currPrice


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()