import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Узлы: 0 — левая, 1 — верхняя, 2 — правая, 3 — нижняя
edges = [
    (0, 1), (1, 2),   # левая → верх → правая
    (2, 3), (3, 0),   # правая → низ → левая
    (1, 3),           # верх ↔ низ
]
G.add_edges_from(edges)

# Координаты: горизонтально вытянутый ромб
pos = {
    0: (-2.0,  0.0),   # левая
    1: ( 0.0,  1.0),   # верхняя
    2: ( 2.0,  0.0),   # правая
    3: ( 0.0, -1.0),   # нижняя
}

nx.draw(G, pos, with_labels=True, node_size=700,
        node_color='lightblue', font_size=14,
        edge_color='gray', width=1.5)
plt.title("Горизонтально вытянутый ромб")
plt.axis('equal')
plt.show()