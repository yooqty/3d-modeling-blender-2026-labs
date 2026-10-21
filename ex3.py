import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import networkx as nx

# --- матрица РОВНО как введена ---
A = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 0, 1],
], dtype=float)

print("Матрица смежности A (как введена, с петлями, несимметричная):")
print(A)
print("Несимметрична:", not np.allclose(A, A.T))

# --- обозначение рёбер ---
edges = [(i+1, j+1) for i in range(3) for j in range(3) if A[i, j]]
loops = [(i+1, i+1) for i in range(3) if A[i, i]]
arcs  = [e for e in edges if e[0] != e[1]]
print("\nПетли:", loops)
print("Дуги:  ", arcs)

# --- 1. спектр графа (собственные значения A) ---
mu = np.linalg.eigvals(A)
print("\nСпектр графа Spec(A):")
for v in mu:
    print(f"  {v:.6f}")

# --- рисунок орграфа с петлями ---
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from(edges)
pos = {1: (0, 1), 2: (1, 1), 3: (0.5, 0)}

plt.figure(figsize=(5, 4))
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=900, font_size=14, width=1.5,
        arrows=True, arrowsize=18, connectionstyle='arc3,rad=0.15')
for i in range(3):
    if A[i, i] != 0:
        x, y = pos[i+1]
        plt.text(x + 0.12, y + 0.12, f"петля {i+1}", fontsize=9, color='green')
plt.title("Орграф с петлями (как введено)")
plt.axis('equal')
plt.show()

# --- 2. матрица Кирхгофа и уравнение ---
deg_out = A.sum(axis=1)
L = np.diag(deg_out) - A
print("\nИсходящие степени:", deg_out)
print("Матрица Кирхгофа L = D_out - A (несимметричная):")
print(L)

lam = sp.symbols('lambda')
char_poly = sp.expand(sp.Matrix(L).charpoly(lam).as_expr())
print("\nУравнение det(L - lambda*I) = 0:")
print(char_poly, "= 0")
print("Факторизация:", sp.factor(char_poly), "= 0")

# --- 3. собственные значения и «вектор Фидлера» ---
eigvals, eigvecs = np.linalg.eig(L)
order = np.argsort(np.abs(eigvals))
eigvals_sorted = eigvals[order]
eigvecs_sorted = eigvecs[:, order]

print("\nСобственные значения L (несимметричная, с петлями):")
for i, v in enumerate(eigvals_sorted):
    print(f"  lambda_{i} = {v:.6f}")

idx_fiedler = 1
fiedler = np.real(eigvecs_sorted[:, idx_fiedler])
if fiedler[0] < 0:
    fiedler = -fiedler
print(f"\n«Вектор Фидлера» для lambda = {eigvals_sorted[idx_fiedler]:.6f}:")
print(np.round(fiedler, 6))
print("ВНИМАНИЕ: для несимметричной L классический вектор Фидлера не определён;")
print("это собственный вектор для второго по модулю собственного значения.")

# --- рисунок с вектором ---
fiedler_dict = {i+1: fiedler[i] for i in range(3)}
plt.figure(figsize=(5, 4))
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=900, font_size=14, width=1.5,
        arrows=True, arrowsize=18, connectionstyle='arc3,rad=0.15')
for node, (x, y) in pos.items():
    plt.text(x, y - 0.15, f"{fiedler_dict[node]:.2f}",
             ha='center', fontsize=11, color='darkred')
colors = ['red' if fiedler_dict[n] > 0 else 'blue' for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=900, alpha=0.6)
plt.title("«Вектор Фидлера» для несимметричной L")
plt.axis('equal')
plt.show()