class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        minHeap = []
        for x in nums:
            heappush(minHeap, int(x))
            if len(minHeap) > k:
                heappop(minHeap)
        return str(minHeap[0])