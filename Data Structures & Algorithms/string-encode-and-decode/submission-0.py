class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_s = ""

        for word in strs:
            enc_s += str(len(word)) + '#' + word

        return enc_s

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            w_length = int(s[i:j])

            i = j + 1
            j = i + w_length

            ans.append(s[i:j])
            i = j

        return ans