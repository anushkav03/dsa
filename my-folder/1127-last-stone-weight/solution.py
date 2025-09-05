class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)
            if y > x:
                new_y = y - x
                heapq.heappush(stones, -1*new_y)

        if len(stones) == 1:
            return -1 * heapq.heappop(stones)
        else:
            return 0

            
