# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class Node:
    def __init__(self, id=0, domain="homepage", next=None):
        self.id = id
        self.domain = domain
        self.next = next
    def __str__(self):
        return f"{self.id} {self.domain} {self.next}"
class BrowserHistory:

    def __init__(self, homepage: str):
        self.dummy = Node(0, homepage)
        self.dic = {0:self.dummy}
        self.count = 0
        self.tail = self.dummy
        self.current = self.dummy
        print(self.dummy)
    def visit(self, url: str) -> None:
        self.count += 1
        temp = self.current.id

        for i in range(temp + 2, self.count):
            del self.dic[i]

        self.count = temp + 1
        new_node = Node(self.count, url)
        self.tail = self.current
        self.tail.next = new_node
        self.tail = new_node
        
        self.current.next = new_node
        self.current = new_node
        self.dic[self.count] = new_node
        print(self.dummy)
    def back(self, steps: int) -> str:
        pos = self.current.id
        while pos > 0 and steps > 0:
            pos -= 1
            steps -= 1
        self.current = self.dic[pos]
        print(self.dummy)
        return self.current.domain
    def forward(self, steps: int) -> str:
        pos = self.current.id
        while pos < self.count and steps > 0:
            pos += 1
            steps -= 1
        self.current = self.dic[pos]
        print(self.dummy)
        return self.current.domain
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)