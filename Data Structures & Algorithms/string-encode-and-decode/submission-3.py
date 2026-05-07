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
            length = ""

            while i < len(s):
                c = s[i]
                i += 1
                if c == "#": break
                length += c
            
            length = int(length)
            ans.append(s[i: i + length ])

            i += length

        return ans