class ProductOfNumbers:

    def __init__(self):
        self.arr = []
    def add(self, num: int) -> None:
        if num != 0:
            if self.arr:
                self.arr.append(self.arr[-1] * num)
            else:
                self.arr.append(num)
        else:
            self.arr = []
    def getProduct(self, k: int) -> int:
        if not self.arr or len(self.arr) < k:
            return 0
        else:
            if len(self.arr) - k != 0:
                return self.arr[-1] // self.arr[len(self.arr) - k - 1]
            else:
                return self.arr[-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)