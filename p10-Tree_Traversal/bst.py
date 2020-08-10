__author__ = "Ky Kartchner"


class Node:
    def __init__(self, value: int):
        """Intialize node with provided value

        Args:
            value (int): The value to assign to node.
        """

        self.left_child = None
        self.right_child = None
        self.value = value


class BST:
    def __init__(self, values=[]):
        """Initialize binary tree with values list.

        Args:
            values ([int]): List of integers to seed the binary tree with.
        """

        self.root_node = None
        for val in values:
            self.insert(val)

    def __post_order(self, node: Node, call_back) -> None:
        """Preform a post order traversal starting with the specified node

        Args:
            node (Node): The node to traverse on.
            callback (function(node)): The call_back function to perform on 
                each node.
        """

        if node is not None:
            self.__post_order(node.left_child, call_back)
            self.__post_order(node.right_child, call_back)
            call_back(node)

    def __in_order(self, node: Node, call_back) -> None:
        """Preform an in order traversal starting with the specified node

        Args:
            node (Node): The node to traverse on.
            callback (function(node)): The call_back function to perform on 
                each node.
        """
        if node is not None:
            self.__in_order(node.left_child, call_back)
            call_back(node)
            self.__in_order(node.right_child, call_back)

    def __pre_order(self, node: Node, call_back) -> None:
        """Preform an in order traversal starting with the specified node

        Args:
            node (Node): The node to traverse on.
            callback (function(node)): The call_back function to perform on 
                each node.
        """
        if node is not None:
            call_back(node)
            self.__pre_order(node.left_child, call_back)
            self.__pre_order(node.right_child, call_back)

    def insert(self, value: int) -> bool:
        """Find the correct position for the specified value 
        and insert it into the binary tree.

        Args:
            value (int): The value to insert into the tree
        
        Return:
            bool: True if value was inserted; False if already exists.
        """
        new_node = Node(value)
        if (self.root_node == None):
            self.root_node = new_node
        else:
            cur_node = self.root_node
            while cur_node:
                prev_node = cur_node
                if value < cur_node.value:
                    cur_node = cur_node.left_child
                elif value > cur_node.value:
                    cur_node = cur_node.right_child
                else:
                    # value already exists in tree
                    return False

            if value < prev_node.value:
                prev_node.left_child = new_node
            else:
                prev_node.right_child = new_node

    def post_order(self, call_back):
        """Call __post_order on root"""
        self.__post_order(self.root_node, call_back)

    def in_order(self, call_back):
        """Call __in_order on root"""
        self.__in_order(self.root_node, call_back)

    def pre_order(self, call_back):
        """Call __pre_order on root"""
        self.__pre_order(self.root_node, call_back)