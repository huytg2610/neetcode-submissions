class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(int)
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        return [item[0] for item in sorted(result.items(), key=lambda x: x[1], reverse=True)][:k]
        
