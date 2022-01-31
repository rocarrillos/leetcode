# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def makeAListNodeFromAList(iterable):
    if len(iterable) == 1:
        return ListNode(iterable[0], None)
    else:
        return ListNode(iterable[0], makeAListNodeFromAList(iterable[1:]))
    
def makeAListFromAListNode(listnode):
    if listnode.next is None:
        return [listnode.val]
    else:
        return [listnode.val] + makeAListFromAListNode(listnode.next)
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = makeAListFromAListNode(l1)
        b = makeAListFromAListNode(l2)
        a.reverse()
        b.reverse()
        for i in range(len(a)):
            a[i] = str(a[i])
        for i in range(len(b)):
            b[i] = str(b[i])
        anum = "".join(a)
        bnum = "".join(b)
        sol = str(int(anum) + int(bnum))[::-1]        
        return makeAListNodeFromAList(sol)
