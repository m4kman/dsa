# Given a linked list of 2n nodes, where each node contains a name, describe an O(n)
# time algorithm to reverse the order of the second half of the list. The algorithm
# should modify the list in place without creating new nodes or using non-constant-sized data structures.
# Write a Python function reorder_nodes(L) that implements this algorithm.


def reorder_nodes(L):
    n = len(L)

    a = L.head

    for _ in range(n - 1):
        a = a.next

    nthNode = a.next
    prevNode, currNode = a, nthNode

    for _ in range(n):
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode, currNode = currNode, nextNode

    reversedFirstNode = prevNode
    a.next = reversedFirstNode  # since the nodes have been reversed, the last node of the first half should point to the first node of the reversed second half
    nthNode.next = (
        None  # the nodes have been reversed, so the last node should point to None
    )

    return
