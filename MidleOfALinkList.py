# PROBLEM
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        # By two pointers
        one_space_pointer = head  # this advance one by one
        two_space_pointer = head  # advance two by two, and help us to stop the loop

        # When we reach the last element or a null, stop it
        while two_space_pointer and two_space_pointer.next:
            one_space_pointer = one_space_pointer.next
            two_space_pointer = two_space_pointer.next.next

        return one_space_pointer.val  # This always point one by one, and it will arrive at the middle when the other arrives at the end


# Construir la lista enlazada 1 -> 2 -> 3 -> 4 -> 5 -> 6
nodes = [ListNode(i) for i in [1, 2, 3, 4, 5, 6]]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

head = nodes[0]

print(Solution().middleNode(head))
