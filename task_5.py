import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import numpy as np
import time

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#000000"  # Початковий колір - чорний
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited=None, delay=1):
    if visited is None:
        visited = []

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)

    for node in visited:
        plt.text(pos[node][0], pos[node][1] - 0.1, s='Visited', horizontalalignment='center', fontsize=12, color='red')

    plt.show()
    time.sleep(delay)

def generate_colors(n):
    colors = []
    for i in range(n):
        color = plt.cm.viridis(i / n)
        colors.append(to_hex(color))
    return colors

def dfs(node, colors, visited):
    stack = [(node, 0)]
    index = 0
    while stack:
        current, depth = stack.pop()
        if current:
            current.color = colors[index]
            visited.append(current.id)
            draw_tree(root, visited)
            index += 1
            stack.append((current.right, depth + 1))
            stack.append((current.left, depth + 1))

def bfs(node, colors, visited):
    queue = [(node, 0)]
    index = 0
    while queue:
        current, depth = queue.pop(0)
        if current:
            current.color = colors[index]
            visited.append(current.id)
            draw_tree(root, visited)
            index += 1
            queue.append((current.left, depth + 1))
            queue.append((current.right, depth + 1))

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Генерація кольорів
num_nodes = 6  # Загальна кількість вузлів
colors = generate_colors(num_nodes)

# Візуалізація обходу в глибину (DFS)
print("Обхід в глибину (DFS):")
dfs(root, colors, [])

# Перевстановлення кольорів для обходу в ширину (BFS)
root.color = "#000000"
root.left.color = "#000000"
root.left.left.color = "#000000"
root.left.right.color = "#000000"
root.right.color = "#000000"
root.right.left.color = "#000000"

# Візуалізація обходу в ширину (BFS)
print("Обхід в ширину (BFS):")
bfs(root, colors, [])
