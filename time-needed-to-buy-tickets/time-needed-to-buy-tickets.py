class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(tickets[k] - (i > k), num) for i,num in enumerate(tickets))