import heapq
from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        heap = []

        for inicio, fim in intervals:
            if heap and heap[0] < inicio:
                heapq.heappop(heap)
                
            heapq.heappush(heap, fim)

        return len(heap)