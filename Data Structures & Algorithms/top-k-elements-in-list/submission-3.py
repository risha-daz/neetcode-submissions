import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem = defaultdict(int)

        for i in nums:
            mem[i]+=1

        pq = []
        for key, val in mem.items():
            heapq.heappush(pq, (val,key))
            if len(pq)>k:
                heapq.heappop(pq)
        
        return [_[1] for _ in pq][-k:]