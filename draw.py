"""Draw the tree of the infix expression"""
from structures.tree import Node
from structures.stack import Stack

import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout


def construct_tree(postfix_expression: str) -> Stack:
    """Construct the expression tree from the postfix expression"""
    stack = Stack()
    for i in postfix_expression:
        if i.isalpha():
            stack.push(Node(i, None, None))
        else:
            right = stack.pop()
            left = stack.pop()
            stack.push(Node(i, left, right))
    return stack


def visualize_expression(postfix: str) -> nx.Graph:
    """Visualize the binarytree of the postfix tree"""
    stack = construct_tree(postfix)
    root = stack.pop()
    G = nx.Graph()
    G.add_node(root.value)
    nodes = [root]
    while nodes:
        node = nodes.pop()
        if node.left:
            G.add_node(node.left.value)
            G.add_edge(node.value, node.left.value)
            nodes.append(node.left)
        if node.right:
            G.add_node(node.right.value)
            G.add_edge(node.value, node.right.value)
            nodes.append(node.right)
    return G


def show_tree(expression: str) -> None:
    """Show the tree"""
    G = visualize_expression(expression)
    pos = graphviz_layout(G, prog="dot")
    plt.axis("off")
    nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=15)
    plt.show()


# if __name__ == "__main__":
#     expression = "ab+de/^"
#     visualize_expression(expression)
