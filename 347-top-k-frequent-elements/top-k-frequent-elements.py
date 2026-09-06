class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = dict()
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)
        
        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in hash_map.items():
            bucket[freq].append(num)
        
        result = []
        for freq in range(len(bucket)-1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result