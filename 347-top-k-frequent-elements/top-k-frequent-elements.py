class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)
        
        hash_map = {k:v for k, v in sorted(hash_map.items(), key = lambda x:x[1], reverse = True)}
        print(hash_map)
        result = []
        count = 0
        for num, cnt in hash_map.items():
            count += 1
            if count > k:
                break
            result.append(num)
        return result
