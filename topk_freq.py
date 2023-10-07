class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        most_freq = counter.most_common(k)
        result = [num for num, _ in most_freq]
        return result
