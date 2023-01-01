"""Draw the tree of the infix expression"""
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

from structures.stack import Stack
from structures.tree import Node


def construct_tree(postfix_expression: str) -> Stack:
    """Construct the expression tree from the postfix expression"""
    stack = Stack()
    unique_id = 0
    for i in postfix_expression:
        unique_id  = unique_id + 1
        if i.isalpha():
            stack.push(Node(i, None, None, unique_id))
        else:
            right = stack.pop()
            left = stack.pop()
            stack.push(Node(i, left, right, unique_id))
    return stack


def visualize_expression(postfix: str) -> nx.Graph:
    """Visualize the binarytree of the postfix tree"""
    stack = construct_tree(postfix)
    root:Node = stack.pop()
    G = nx.Graph()
    G.add_node(root.id, value = root.value)
    nodes = [root]
    while nodes:
        node = nodes.pop()
        if node.left:
            G.add_node(node.left.id, value = node.left.value)
            G.add_edge(node.id, node.left.id)
            nodes.append(node.left)
        if node.right:
            G.add_node(node.right.id, value = node.right.value)
            G.add_edge(node.id, node.right.id)
            nodes.append(node.right)
    return G


def show_tree(expression: str) -> None:
    """Show the tree"""
    G = visualize_expression(expression)
    pos = graphviz_layout(G, prog="dot")
    plt.axis("off")
    labels = nx.get_node_attributes(G, 'value')
    nx.draw_networkx(G, pos, labels=labels, with_labels=True, node_color="skyblue")
    plt.show()
