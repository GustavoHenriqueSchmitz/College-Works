from collections import deque


class Node:
    """Nó da árvore, que representa uma Pessoa."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.left = None
        self.right = None

    def __str__(self):
        return f"Nome: {self.name:<10} - Idade: {self.age}"


class BinarySearchTree:
    """Árvore Binária de Busca de pessoas.

    Ordena pela idade e, em caso de empate, pelo nome.
    Os menores vão para a esquerda e os maiores ou iguais vão para a direita.
    """

    def __init__(self):
        self.root = None

    def insert(self, name, age):
        new_node = Node(name, age)

        def insert_at(current):
            if current is None:
                return new_node
            if (new_node.age, new_node.name) < (current.age, current.name):
                current.left = insert_at(current.left)
            else:
                current.right = insert_at(current.right)
            return current

        self.root = insert_at(self.root)

    def print_in_order(self, node):
        if node is not None:
            self.print_in_order(node.left)
            print(node)
            self.print_in_order(node.right)

    def print_pre_order(self, node):
        if node is not None:
            print(node)
            self.print_pre_order(node.left)
            self.print_pre_order(node.right)

    def print_post_order(self, node):
        if node is not None:
            self.print_post_order(node.left)
            self.print_post_order(node.right)
            print(node)

    def print_dec_order(self, node):
        if node is not None:
            self.print_dec_order(node.right)
            print(node)
            self.print_dec_order(node.left)

    def print_breadth_first(self):
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node is not None:
                print(node)
                queue.append(node.left)
                queue.append(node.right)


if __name__ == "__main__":
    tree = BinarySearchTree()

    people = [
        ("Gustavo", 20),
        ("Marcelo", 47),
        ("Claudenice", 48),
        ("Adriano", 20),
        ("Kauã", 20),
        ("Harry", 19),
        ("Ivone", 68),
        ("Pedro", 74),
        ("Isabelly", 9),
        ("Yasmin", 9),
        ("Isabela", 21),
    ]

    for name, age in people:
        tree.insert(name, age)

    print("Em Ordem:")
    tree.print_in_order(tree.root)

    print("\nPré Ordem:")
    tree.print_pre_order(tree.root)

    print("\nPós Ordem:")
    tree.print_post_order(tree.root)

    print("\nEm Ordem Invertido (Dec Order):")
    tree.print_dec_order(tree.root)

    print("\nLargura:")
    tree.print_breadth_first()
