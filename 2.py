class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None
    def insert_left(self, new_node):
        if self.right_child and isinstance(self.right_child, BinaryTree) and self.right_child.get_root_val() < new_node:
            print("error")
            return ""
        elif self.right_child and self.right_child < new_node:
            print("error")
            return ""
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj
    def insert_right(self, new_node):
        if self.left_child and isinstance(self.left_child, BinaryTree) and self.left_child.get_root_val() > new_node:
            print("error")
            return ""
        elif self.left_child and self.left_child > new_node:
            print("error")
            return ""
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())