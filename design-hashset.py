class MyHashSet:

    def __init__(self):
        self.keys = [0] * (10**6 + 1)
        
    def add(self, key: int) -> None:
        self.keys[key] = 1

    def remove(self, key: int) -> None:
        self.keys[key] = 0

    def contains(self, key: int) -> bool:
        return self.keys[key] == 1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# this is a stupid but clever solution. absolutely would get hired at facebook
