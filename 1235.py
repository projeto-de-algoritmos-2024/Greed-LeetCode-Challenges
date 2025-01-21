class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[0])
        hp = []
        total = 0

        for s,e,p in jobs:
            while hp and hp[0][0] <= s:
                popd = heappop(hp)
                total = max(total, popd[1])

            heappush(hp, (e, p + total))

        while hp:
            popd = heappop(hp)
            total = max(total, popd[1])

        return total