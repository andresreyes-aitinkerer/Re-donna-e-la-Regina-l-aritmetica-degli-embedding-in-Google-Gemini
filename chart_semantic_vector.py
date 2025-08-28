import matplotlib.pyplot as plt
import numpy as np

# Create a simple diagram showing a semantic vector in 2D
fig, ax = plt.subplots(figsize=(6, 6), facecolor="black")
ax.set_facecolor("black")

# Axis settings
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
ax.set_xlabel("Dimensione 1", color="white")
ax.set_ylabel("Dimensione 2", color="white")
ax.set_title("Esempio di semantic vector", color="white", pad=15)

# Draw the vector
origin = np.array([0, 0])
vector = np.array([2, 1.5])
ax.arrow(origin[0], origin[1], vector[0], vector[1],
         head_width=0.1, head_length=0.15, fc="white", ec="white", linewidth=2)

# Add labels
ax.text(vector[0] + 0.05, vector[1], "parola: 'regina'", color="white", fontsize=10)
ax.text(0.1, -0.2, "origine\n(spazio vettoriale)", color="white", fontsize=9)

# Show direction label
ax.text(1.0, 0.7, "direzione del\nsemantic vector", color="white", fontsize=9,
        bbox=dict(facecolor="black", edgecolor="white", boxstyle="round,pad=0.2"))

plt.show()
