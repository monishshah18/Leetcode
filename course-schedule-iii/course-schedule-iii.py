class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap_list = []
        curr_counter = 0
        for i,j in sorted(courses, key = lambda x:x[1]):
            curr_counter+=i
            heapq.heappush(heap_list, -i)
            if curr_counter > j:
                curr_counter += heapq.heappop(heap_list)
        return len(heap_list)
        