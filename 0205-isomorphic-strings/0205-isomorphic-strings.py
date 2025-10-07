class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        e -> a
        g -> d
        g -> d


        f -> b
        o -> a
        o -> r

        p -> t
        a -> t
        p -> t
        e -> l
        r -> e
        """

        isomorphic_s = {}
        isomorphic_t = {}
        for j in range(len(s)):
            if (s[j] in isomorphic_s and isomorphic_s[s[j]] != t[j]) or (t[j] in isomorphic_t and isomorphic_t[t[j]] != s[j]):
                return False
            isomorphic_s[s[j]] = t[j]
            isomorphic_t[t[j]] = s[j]
        return True