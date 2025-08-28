import numpy as np
import matplotlib.pyplot as plt

def cos_sim(a, b):
    a = np.asarray(a); b = np.asarray(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

# Vettori di esempio
v_man    = np.array([0.0, 0.0])
v_woman  = np.array([1.0, 1.0])
v_king   = np.array([2.0, 0.0])
v_queen  = np.array([3.0, 1.05])
v_result = v_king - v_man + v_woman
sim = cos_sim(v_result, v_queen)

# Grafico con sfondo nero
fig, ax = plt.subplots(figsize=(6, 5), facecolor="black")
ax.set_facecolor("black")

# Stile assi
for spine in ax.spines.values():
    spine.set_color("white")
ax.tick_params(colors="white")
ax.grid(True, linestyle="--", linewidth=0.5, color="#444")
#ax.set_title("Parallelogramma dell'analogia: king - man + woman ≈ queen", color="white")
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("Dimensione 1", color="white")
ax.set_ylabel("Dimensione 2", color="white")

# Punti e testi
points = {
    "man": v_man,
    "woman": v_woman,
    "king": v_king,
    "queen": v_queen,
    "result": v_result
}
for name, (x, y) in points.items():
    ax.scatter([x], [y], c="white")
    ax.text(x + 0.05, y + 0.05, name, color="white")

# Funzione per frecce
def arrow(p, q, c="white", ls="-"):
    dx, dy = q - p
    ax.arrow(p[0], p[1], dx, dy,
             head_width=0.06, head_length=0.09,
             length_includes_head=True, color=c, linestyle=ls, lw=1.8)

# Lati principali e diagonali
arrow(v_man, v_woman, c="cyan")
arrow(v_man, v_king, c="cyan")
arrow(v_king, v_result, c="cyan", ls=":")
arrow(v_woman, v_result, c="cyan", ls=":")
arrow(v_result, v_queen, c="yellow")

plt.show()
print(f"Similarità coseno(result, queen) = {sim:.4f}")