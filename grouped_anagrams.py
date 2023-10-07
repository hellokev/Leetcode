class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in grp:
                grp[key] = [word]
            else:
                grp[key].append(word)
        return grp.values()