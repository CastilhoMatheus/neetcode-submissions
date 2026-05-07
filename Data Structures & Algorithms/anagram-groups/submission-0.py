class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        groups = defaultdict(list)

        for w in strs:
            cp = w
            cp = [c for c in cp]
            cp.sort()
            key = "".join(cp)

            groups[key].append(w)

        for g in groups.values():
            ans.append(g)

        return ans