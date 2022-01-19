from collections import Counter
from binarytree import Node

# создаём дерево
def haffman_tree(string):
    periodicity = Counter(string)
    tree = {}
    for period in periodicity.most_common():
        root = Node(period[1])
        root.left = Node(ord(period[0]))
        if root.value in tree:
            tree[root.value].append(root)
        else:
            tree[root.value] = [root]

    m = min(tree.keys())
    while len(tree) != 1 or m is not None:
        nodes = [0, 0]
        for i in range(len(nodes)):
            nodes[i] = tree[m].pop()
            if not tree[m]:
                tree.pop(m)
                try:
                    m = min(tree.keys())
                except ValueError:
                    m = None

        root = Node(nodes[0].value + nodes[1].value)
        root.left = nodes[0]
        root.right = nodes[1]

        if root.value in tree:
            tree[root.value].append(root)
        else:
            tree[root.value] = [root]
    return tree[min(tree.keys())][0]

# создаём таблицу
def haffman_table(tree):
    haf_table = {}

    def traversal(current_node, string=""):
        if current_node.right is not None:
            traversal(current_node.left, string + "0")
            traversal(current_node.right, string + "1")
        else:
            haf_table[chr(current_node.left.value)] = string

    traversal(tree)
    return haf_table


def unification(string):
    haf_tree = haffman_tree(string)
    haf_table = haffman_table(haf_tree)

    print(haf_tree)

    result = []
    for char in string:
        result.append(haf_table[char])
    return result

print(unification("beep boop beer!"))


# Код написан при помощи сторонний библиотеки операясь на пример с урока