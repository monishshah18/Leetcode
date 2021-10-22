def manhattan_distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        pq = [(0,0,'0'*len(bikes))]
        optimal_cost = collections.defaultdict(lambda: float('inf'))
        
        while pq:
            cost,i,bike_status = heapq.heappop(pq)
            if i == len(workers):
                return cost
            for j,k in enumerate(bikes):
                if bike_status[j] != '1':
                    new_cost = cost + manhattan_distance(workers[i],k)
                    new_bike_status = bike_status[:j] + '1' + bike_status[j+1:]
                    
                    if new_cost < optimal_cost[(i+1,new_bike_status)]:
                        optimal_cost[(i+1, new_bike_status)] = new_cost
                        heapq.heappush(pq,(new_cost,i+1,new_bike_status))
        return -1
            