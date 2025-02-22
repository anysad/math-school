import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero

# Koordināti
points = {
    "A": (-19.6, 2.39),
    "B": (-16.38, 4.43),
    "C": (-12.56, 6.59),
    "D": (-8.32, 7.86),
    "E": (-4.16, 8.71),
    "F": (0, 9.13),
    "G": (4.29, 8.63),
    "H": (8.33, 7.85),
    "I": (12.29, 6.3),
    "J": (16, 4),
    "K": (18.87, 2.58),
}

# Paņemt x un y koordinātus
x = np.array([coord[0] for coord in points.values()])
y = np.array([coord[1] for coord in points.values()])

# Ievietot 2. pakāpes polinomu punktiem
coeffs = np.polyfit(x, y, deg=2)
polynomial = np.poly1d(coeffs)

# Ģenerē jaunas x vērtības un aprēķina polinomam atbilstošās y vērtības
x_new = np.linspace(min(x), max(x), 500)
y_new = polynomial(x_new)

# Uzzīmēt punktus un kvadrātfunkciju
fig = plt.figure(figsize=(10, 6))
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)

plt.scatter(x, y, color="red", label="Datu punkti")
plt.plot(x_new, y_new, color="blue", label=f"Polynomial: {polynomial}")
plt.title("Kvadrātfunciju iegūšana")
plt.xlabel("X")
plt.ylabel("Y")
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
plt.axvline(0, color='black', linewidth=0.5, linestyle="--")
plt.legend()
plt.grid(True)
plt.show()

# Polinomas koeficienti
print("Polynomial Coefficients:", coeffs)
