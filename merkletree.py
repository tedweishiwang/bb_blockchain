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

    nodel = None
    noder = None

    while len(nodes) > 1:
        newnodelist = []
        for idx in range(0, len(nodes), 2):
            if idx != len(nodes) - 1:
                nodel, noder = nodes[idx], nodes[idx + 1]
            else:
                nodel = nodes[idx]
                noder = None
            if noder is None:
                merged = double_hash(nodel.data + nodel.data)
            else:
                merged = double_hash(nodel.data + noder.data)
            parent = Node(merged)
            parent.left = nodel
            parent.right = noder
            newnodelist.append(parent)
        nodes = newnodelist
        level += 1

    root = nodes[0]
    root.left = nodel
    root.right = noder
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
