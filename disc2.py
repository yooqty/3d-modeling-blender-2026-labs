import networkx as nx
import matplotlib.pyplot as plt

# ================= ЛЕВЫЙ ГРАФ =================
G1 = nx.Graph()

edges1 = [
    (0, 4), (0, 1), (0, 7),
    (4, 6), (4, 9), (4, 3), (4, 8),
    (6, 1), (6, 9), (6, 8),
    (1, 9), (1, 2), (1, 7), (1, 5),
    (9, 2), (9, 8),
    (5, 2), (5, 7),
    (3, 8), (3, 2),
    (8, 2),
    (2, 7)
]
G1.add_edges_from(edges1)

pos1 = {
    0: (2.0, 10.0),
    4: (0.5, 7.0),
    6: (1.5, 8.0),
    1: (3.0, 8.0),
    5: (4.0, 6.5),
    9: (2.3, 5.5),
    8: (1.5, 3.5),
    3: (0.5, 1.5),
    2: (2.5, 0.5),
    7: (4.0, 1.5),
}

# ================= ПРАВЫЙ ГРАФ =================
G2 = nx.Graph()

edges2 = [
    (4, 9), (4, 0), (4, 3),
    (3, 9), (3, 8), (3, 2),
    (9, 8), (9, 5), (9, 2),
    (8, 5), (8, 7), (8, 2),
    (5, 6), (5, 7), (5, 1),
    (6, 7), (6, 1),
    (7, 2), (7, 1),
    (2, 1),
    (0, 1)
]
G2.add_edges_from(edges2)

pos2 = {
    4: (2.0, 10.0),
    0: (0.0, 6.0),
    3: (4.0, 8.5),
    9: (2.8, 7.5),
    8: (3.5, 6.2),
    5: (1.8, 3.8),
    6: (2.7, 3.8),
    7: (3.3, 4.8),
    2: (4.0, 2.5),
    1: (2.3, 1.0),
}

# ================= ОТРИСОВКА =================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 8))

nx.draw(G1, pos1, ax=ax1, with_labels=True,
        node_size=500, node_color='#1f77b4',
        font_color='white', font_weight='bold',
        edge_color='black', width=1.2)

nx.draw(G2, pos2, ax=ax2, with_labels=True,
        node_size=500, node_color='#1f77b4',
        font_color='white', font_weight='bold',
        edge_color='black', width=1.2)

ax1.set_title("Граф 1")
ax2.set_title("Граф 2")
plt.tight_layout()
plt.show()