class Node:
    def __init__(self):
        self.flag = False
        self.children = {}

class MagicDictionary:

    def __init__(self):
        self.Trie = Node()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            temp = self.Trie
            for char in word:
                if char not in temp.children:
                    temp.children[char] = Node()
                temp = temp.children[char]
            temp.flag = True


    def search(self, searchWord: str) -> bool:
        return self._search(searchWord, False, 0, self.Trie)

    def _search(self, word, check, i, temp):
        if i == len(word):
            if temp.flag and check:
                return True
            return False
       
        for j in temp.children:
            
            if check and word[i] != j:
                continue

            if word[i] != j:
                if self._search(word, True, i + 1, temp.children[j]):
                    return True
            elif self._search(word, check, i + 1, temp.children[j]):
                return True
       
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)