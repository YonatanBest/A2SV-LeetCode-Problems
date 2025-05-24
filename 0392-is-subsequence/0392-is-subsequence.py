from collections import deque
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = deque(s)
        for j in t:
            if not queue:
                return True
            if j == queue[0]:
                queue.popleft()
        return not queue