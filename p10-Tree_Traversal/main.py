__author__ = "Ky Kartchner"

from bst import BST


def main() -> None:
    """Create a binary tree with hard-coded input and then print its
    pre-order, in-order, and post-order traversals.
    """

    input = [50, 75, 25, 15, 60, 35, 90, 42, 20, 27, 5, 55, 95, 80, 70]
    binary_tree = BST(input)

    print("\nWelcome to Tree Traversal!")
    print("Below is the input order of a hard-coded tree and its calculated",
          "traversals:")
    print_list("BST input order", input)
    print()
    print_list("pre-order", num_list(binary_tree.pre_order))
    print_list("in-order", num_list(binary_tree.in_order))
    print_list("post-order", num_list(binary_tree.post_order))
    print()


def print_list(label: str, num_list: [int]) -> None:
    """Print the provided list of numbers comma seperated.

    Args:
        label (str): The text that precedes the number list.
        num_list ([int]): The list of number to print.
    """

    print(f"{label}: {', '.join(str(e) for e in num_list)}")


def num_list(traversal) -> [int]:
    """Get a list of the numbers returned from the provided traversal function

    Args:
        traversal (function(call_back)): Traversal function to use
    
    Returns:
        [int]: The values returned from the traversal function.
    """

    values = []
    traversal(lambda node: values.append(node.value))

    return values


if __name__ == "__main__":
    main()