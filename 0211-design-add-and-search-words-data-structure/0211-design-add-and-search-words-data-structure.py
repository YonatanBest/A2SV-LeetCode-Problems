class Node:
    def __init__(self):
        self.end = False
        self.children = defaultdict(Node)

class WordDictionary:

    def __init__(self):
        self.words = Node()

    def addWord(self, word: str) -> None:
        temp = self.words
        for char in word:
            if char not in temp.children:
                temp.children[char] = Node()
            temp = temp.children[char]
        temp.end = True
            
    def _search(self, word, curr, i):

        if i == len(word):
            return curr.end
        
        if word[i] != ".":
            if word[i] not in curr.children:
                return False
            elif self._search(word, curr.children[word[i]], i + 1):
                    return True
        else:
            for j in curr.children:
                if self._search(word, curr.children[j], i + 1):
                    return True

        return False
        
    def search(self, word: str) -> bool:
        return self._search(word, self.words, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)