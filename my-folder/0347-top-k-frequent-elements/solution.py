class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        #sortednums = [x[0] for x in sorted(dict.items(), key=lambda item: item[1])][:k]
        sortedtuples = sorted(dict.items(), key=lambda item: item[1], reverse=True)
        sortednums = [x[0] for x in sortedtuples][:k]
        return sortednums


        
