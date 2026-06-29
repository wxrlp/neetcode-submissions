class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        for a in s:
            if a not in map_s:
                map_s[a] = 0
            else:
                map_s[a] = map_s[a] + 1
        for b in t:
            if b not in map_t:
                map_t[b] = 0
            else:
                map_t[b] = map_t[b] + 1
        return map_s == map_t