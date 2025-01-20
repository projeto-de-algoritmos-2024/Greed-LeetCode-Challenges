from typing import List
import sys

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        trabalhadores = [0]
        self.ans = sys.maxsize
        
        jobs.sort(reverse=True)
        
        def dfs(atual):

            if atual == len(jobs):
                self.ans = min(self.ans, max(trabalhadores))
                return
            

            repetidos = set()
            for i in range(k):
    
                if trabalhadores[i] in repetidos or trabalhadores[i] + jobs[atual] >= self.ans:
                    continue
                repetidos.add(trabalhadores[i])
                
                trabalhadores[i] += jobs[atual]
                dfs(atual + 1)
                trabalhadores[i] -= jobs[atual]
        
        dfs(0)
        return self.ans