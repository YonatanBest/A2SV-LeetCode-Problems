class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)

        def checker(count, freq):
            for i in count:
                if freq != count[i]:
                    return False
            return True

        for i in range(len(word)):
            counter[word[i]] -= 1

            if counter[word[i]] == 0:
                del counter[word[i]]

            if checker(counter, counter[next(iter(counter))]):
                return True
            
            counter[word[i]] += 1
        
        return False
