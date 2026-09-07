class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for w in strs:
            counter = [0] * 26
            for c in w:
                counter[ord(c) - ord("a")] += 1
                
            groups[tuple(counter)].append(w)
        
        return list(groups.values())