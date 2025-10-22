class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        def checker(path):
            count = Counter(path)
            freq = count[path[0]]
            for i in count:
                if freq != count[i]:
                    return False
            return True

        for i in range(len(word)):
            if checker(word[:i] + word[i + 1:]):
                return True
        
        return False
