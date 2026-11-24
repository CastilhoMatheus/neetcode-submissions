class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def searchMin(self, word, smallest):
        cur = self.root
        for i in range(min(len(word), smallest)):
            if word[i] not in cur.children:
                return i
            cur = cur.children[word[i]]
        
        return min(len(word), smallest)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]


        smallest_idx = 0
        for i, w in enumerate(strs):
            if len(strs[smallest_idx]) > len(w):
                smallest_idx = i

        s_word = strs[smallest_idx]

        trie = PrefixTrie()
        trie.insert(s_word)
        i = len(s_word)

        for word in strs:
            i = trie.searchMin(word, i)
        
        return strs[0][:i]

