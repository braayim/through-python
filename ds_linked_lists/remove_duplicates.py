import unittest


def remove_duplicates(head):
    """
    Removes duplicates from a linked list
    :param head:
    :return:
    """
    node = head

    if node:
        values = {node.val: True}
        while node.next:
            if node.next.val in values:
                node.next = node.next.next
            else:
                values[node.next.val] = True
                node = node.next
    return head


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Test(unittest.TestCase):
    def test_remove_duplicates(self):
        head = Node(1, Node(3, Node(3, Node(1, Node(5, None)))))
        remove_duplicates(head)
        data = [
            (head.val, 1),
            (head.next.val, 3),
            (head.next.next.val, 5),
            (head.next.next.next, None)
        ]

        for [node_val, expected] in data:
            self.assertEqual(node_val, expected)


if __name__ == "__main__":
    unittest.main()