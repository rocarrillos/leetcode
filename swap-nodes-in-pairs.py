# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # thoughts:
        # new first is second
        # new second is first
        # new third is fourth
        # new fourth is third etc
        # as you go through, create switched pairs. then stitch the pairs together in order
        node = head
        list_of_nodes = []
        while node is not None:
            next_node = node.next
            if next_node is not None:
                # create a new pair
                new_node = ListNode(next_node.val, ListNode(node.val))
                list_of_nodes.append(new_node)
                node = next_node.next
            else:
                list_of_nodes.append(node)
                node = None
            
        print(list_of_nodes)
        while(len(list_of_nodes) > 1):
            tail_node = list_of_nodes.pop(-1)
            list_of_nodes[-1].next.next = tail_node
        return list_of_nodes[0] if len(list_of_nodes) else None
        
