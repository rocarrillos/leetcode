class SnapshotArray:

    def __init__(self, length: int):
        d = dict()
        d[0] = 0
        self.data = [dict(d) for i in range(length)]
        self.counter = 0

    def set(self, index: int, val: int) -> None:
        self.data[index][self.counter] = val

    def snap(self) -> int:
        self.counter += 1
        return self.counter - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.data[index].keys():
            return self.data[index][snap_id]
        else:
            key_to_get = max(list(filter(lambda x: x < snap_id, self.data[index].keys())))
            return self.data[index][key_to_get]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# version with lists
# this one got Time Limit Exceeded
class SnapshotArray:

    def __init__(self, length: int):
        self.data = [[0] for i in range(length)]
        self.counter = 0

    def set(self, index: int, val: int) -> None:
        self.data[index][self.counter] = val

    def snap(self) -> int:
        self.counter += 1
        for item in self.data:
            item.append(item[-1])
        return self.counter - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.data[index][snap_id]
    

# version with dicts
# this one got Memory Limit Exceeded
class SnapshotArray:

    def __init__(self, length: int):
        self.data = dict()
        self.snapshots = dict()
        self.counter = 0

    def set(self, index: int, val: int) -> None:
        self.data[index] = val

    def snap(self) -> int:
        self.snapshots[self.counter] = dict(self.data)
        self.counter += 1
        return self.counter - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snapshots[snap_id].keys():
            return self.snapshots[snap_id][index]
        else:
            return 0