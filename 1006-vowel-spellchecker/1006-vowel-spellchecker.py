class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordlist_org = set(wordlist)
        wordlist_check = defaultdict(str)
        wordlist_vowel = defaultdict(str)

        def vowel_star(word):
            tmp = []
            vowels = "aeiou"
            for c in word.lower():
                if c in vowels:
                    tmp.append("*")
                else:
                    tmp.append(c)
            return "".join(tmp)
        
        for word in wordlist:
            if word.lower() not in wordlist_check:
                wordlist_check[word.lower()] = word

        for word in wordlist:
            if vowel_star(word) not in wordlist_vowel:
                wordlist_vowel[vowel_star(word)] = word

        result = []
        for que in queries:
            if que in wordlist_org:
                result.append(que)
            elif que.lower() in wordlist_check:
                result.append(wordlist_check[que.lower()])
            elif vowel_star(que) in wordlist_vowel:
                result.append(wordlist_vowel[vowel_star(que)])
            else:
                result.append("")


        return result