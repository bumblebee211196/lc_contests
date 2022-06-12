import string

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        trie = defaultdict(set)
        res = 0
        
        for idea in ideas:
            trie[idea[0]].add(idea[1:])
        
        for c1 in string.ascii_lowercase:
            for c2 in string.ascii_lowercase:
                if c1 == c2: continue
                v1 = len(trie[c1] - trie[c2])
                v2 = len(trie[c2] - trie[c1])
                res += v1 * v2
                
        return res
