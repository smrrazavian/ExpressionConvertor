"""Main file for the project. """
from draw import show_tree
from expression_convertor import (
    detect_type,
    infix_to_postfix,
    infix_to_prefix,
    postfix_to_infix,
    prefix_to_infix,
)


def main():
    """Main function"""
    expression = input("Enter expression: ")
    expression = expression.replace(" ", "")
    expression_type = detect_type(expression)
    tree_expression = ""
    if expression_type == "infix":
        print("Expression type: Infix")
        print("Postfix: ", infix_to_postfix(expression))
        print("Prefix: ", infix_to_prefix(expression))
        tree_expression = infix_to_postfix(expression)
    elif expression_type == "prefix":
        print("Expression type: Prefix")
        print("Postfix: ", infix_to_postfix(prefix_to_infix(expression)))
        print("Infix: ", prefix_to_infix(expression))
        tree_expression = infix_to_postfix(prefix_to_infix(expression))
    elif expression_type == "postfix":
        print("Expression type: Postfix")
        print("Prefix: ", infix_to_prefix(postfix_to_infix(expression)))
        print("Infix: ", postfix_to_infix(expression))
        tree_expression = expression
    else:
        raise ValueError("Invalid expression")
    show_tree(tree_expression)


if __name__ == "__main__":
    main()
