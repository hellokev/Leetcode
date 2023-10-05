class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for j in t:
            if j in freq:
                freq[j] -= 1
            else:
                freq[j] = 1
        for k in freq:
            if freq.get(k) != 0:
                return False
        return True