class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        stopBoard = {}
        for bus,stops in enumerate(routes):
            for stop in stops:
                if stop not in stopBoard:
                    stopBoard[stop] = [bus]
                else:
                    stopBoard[stop].append(bus)
        queue = deque([source])
        visited = set()
        res = 0
        while queue:
            res += 1
            pre_stop = len(queue)
            for _ in range(pre_stop):
                curr_stop = queue.popleft()
                for bus in stopBoard[curr_stop]:
                    if bus in visited: continue
                    visited.add(bus)
                    
                    for stop in routes[bus]:
                        if stop==target:
                            return res
                        queue.append(stop)
        return -1