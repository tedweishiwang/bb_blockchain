import hashlib
import binascii


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def double_hash(input):
    return hashlib.sha256(hashlib.sha256(input).digest()).digest()


def unhex(input):
    return binascii.unhexlify(input)


def hex(input):
    return binascii.hexlify(input)


def reverse(input):
    return input[::-1]


def build_merkle_tree(txs):
    nodelist = txs

    nodes = []

    for node in nodelist:
        nodes.append(Node(node))

    level = 1

    node_l = None
    node_r = None

    while len(nodes) > 1:
        new_node_list = []
        for idx in range(0, len(nodes), 2):
            if idx != len(nodes) - 1:
                node_l, node_r = nodes[idx], nodes[idx + 1]
            else:
                node_l = nodes[idx]
                node_r = None
            if node_r is None:
                merged = double_hash(node_l.data + node_l.data)
            else:
                merged = double_hash(node_l.data + node_r.data)
            parent = Node(merged)
            parent.left = node_l
            parent.right = node_r
            new_node_list.append(parent)
        nodes = new_node_list
        level += 1

    root = nodes[0]
    root.left = node_l
    root.right = node_r
    return root


def inorderTraversal(root):
    res = []
    helper(root, res)
    return res


def helper(root, res):
    if root:
        helper(root.left, res)
        res.append(hex(reverse(root.data)))
        helper(root.right, res)


def hasPath(root, path, x):
    if not root:
        return False

    path.append(root)

    if hex(reverse(root.data)) == x:
        return True

    if (hasPath(root.left, path, x) or
            hasPath(root.right, path, x)):
        return True

    path.pop(-1)
    return False


def getPath(root, x):
    path = []
    hasPath(root, path, x)
    return path
