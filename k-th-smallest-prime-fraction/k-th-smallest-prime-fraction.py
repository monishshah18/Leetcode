class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        #keeping heap of k items
        heap = [(arr[i]/arr[-1],i,len(arr)-1)for i in range(min(len(arr)-1, k))]
        for _ in range(k-1):
            _,i,j = heap[0]
            heapreplace(heap,(arr[i]/arr[j-1],i,j-1))
        return [arr[heap[0][1]], arr[heap[0][2]]]