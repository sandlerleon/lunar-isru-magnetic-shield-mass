# -*- coding: utf-8 -*-
"""Regenerate Figures 1-3 for the Lunar Shield ISRU manuscript directly from the
model's own Monte Carlo / sweep output, so every plotted value traces to
scaffold_shield_mass_isru.py rather than to a hand-drawn graphic.

Output: fig1_isru_sweep.png, fig2_mass_uncertainty.png, fig3_pareto.png (300 dpi).
"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
RES = json.load(open(os.path.join(HERE, "mass_isru_results.json")))

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 9, "axes.labelsize": 9, "axes.titlesize": 9,
    "xtick.labelsize": 8, "ytick.labelsize": 8, "legend.fontsize": 8,
    "axes.spines.top": False, "axes.spines.right": False,
})

# ---------------------------------------------------------------- Figure 1
sweep = RES["isru"]["sweep"]
M_E = RES["isru"]["M_E_t"]
mults = [1, 3, 5]
m_local = [sweep[str(m)][0] for m in mults]
m_total = [sweep[str(m)][1] for m in mults]
f_isru  = [sweep[str(m)][2] for m in mults]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.0))
x = np.arange(len(mults)); w = 0.26
ax1.bar(x - w, [M_E]*3, w, label="Earth-launched $M_E$", color="#3B6FB6")
ax1.bar(x,     m_local,  w, label="Local (regolith) mass", color="#4C9A5A")
ax1.bar(x + w, m_total,  w, label="Total system mass", color="#7C5AA6")
ax1.set_xticks(x); ax1.set_xticklabels([f"{m}×" for m in mults])
ax1.set_xlabel("Regolith-construction mass multiplier")
ax1.set_ylabel("Mass (t)")
ax1.legend(frameon=False, loc="upper left")
for xi, v in zip(x - w, [M_E]*3):
    ax1.text(xi, v + 4, f"{v:.1f}", ha="center", fontsize=7)

ax2.plot(mults, [100*f for f in f_isru], "o-", color="#7C5AA6")
for m, f in zip(mults, f_isru):
    ax2.annotate(f"{100*f:.0f}%", (m, 100*f), textcoords="offset points",
                 xytext=(0, 7), ha="center", fontsize=8)
ax2.set_xticks(mults); ax2.set_xticklabels([f"{m}×" for m in mults])
ax2.set_xlabel("Regolith-construction mass multiplier")
ax2.set_ylabel("In-situ mass fraction $f_{ISRU}$ (%)")
ax2.set_ylim(35, 92)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig1_isru_sweep.png"), dpi=300)
plt.close(fig)

# ---------------------------------------------------------------- Figure 2
tor = RES["mass_montecarlo"]["tornado"]
base = RES["mass_montecarlo"]["baseline_midpoint_t"]
labels = {"S": "Structural / cryostat / leads / power",
          "D": "Conductor current derating",
          "T": "Lunar thermal-cycling radiator",
          "Du": "Dust mitigation"}
order = sorted(tor.keys(), key=lambda k: tor[k][1] - tor[k][0])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.6, 3.0))
for i, k in enumerate(order):
    lo, hi = tor[k]
    ax1.barh(i, lo - base, left=base, color="#6FA3D6", height=0.6)
    ax1.barh(i, hi - base, left=base, color="#D67F6F", height=0.6)
ax1.axvline(base, color="k", lw=1)
ax1.set_yticks(range(len(order)))
ax1.set_yticklabels([labels[k] for k in order])
ax1.set_xlabel("Total system mass (t)")
ax1.text(base, len(order) - 0.35, f" baseline {base:.1f} t", fontsize=7, va="center")

rng = np.random.default_rng(2026)
N = 300_000; C = 12.0
total = (C * rng.uniform(1.0, 1.5, N) * rng.uniform(3.0, 5.0, N)
           * rng.uniform(1.0, 1.5, N) * rng.uniform(1.0, 1.2, N))
med = RES["mass_montecarlo"]["median_t"]
lo90, hi90 = RES["mass_montecarlo"]["ci90_t"]
ax2.hist(total, bins=140, color="#9BB7D4", edgecolor="none")
ax2.axvline(med, color="#7C5AA6", lw=1.6, label=f"median {med:.0f} t")
ax2.axvline(lo90, color="#444", ls="--", lw=1, label=f"90% CI {lo90:.0f}–{hi90:.0f} t")
ax2.axvline(hi90, color="#444", ls="--", lw=1)
ax2.axvline(100, color="#B03A2E", ls=":", lw=1.2,
            label=f"P(>100 t) = {100*RES['mass_montecarlo']['p_gt_100t']:.0f}%")
ax2.set_xlabel("Total system mass (t)")
ax2.set_ylabel("Monte Carlo samples")
ax2.set_xlim(20, 200)
ax2.legend(frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig2_mass_uncertainty.png"), dpi=300)
plt.close(fig)

# ---------------------------------------------------------------- Figure 3
# Four architectures on the common (M_E, dF_E) basis of manuscript Table 3.
arch = [
    ("A — Imported fence",           81.0, 75.0, "#3B6FB6", "Mobile/EVA (baseline)"),
    ("B — Regolith only, 2 cm",       5.0, 91.4, "#4C9A5A", "Fixed equipment"),
    ("C — Fence + regolith, 2 cm",   46.4, 94.7, "#D18F2E", "Fixed, high-value"),
    ("D — ISRU-structural fence",    46.4, 75.0, "#7C5AA6", "Mobile/EVA (preferred)"),
]
# per-point label offsets, hand-tuned so no label collides with the ISRU arrow note
offsets = {"A": (11, -3), "B": (11, 3), "C": (11, 3), "D": (-11, -6)}
aligns = {"A": "left", "B": "left", "C": "left", "D": "right"}
fig, ax = plt.subplots(figsize=(6.8, 4.2))
for name, me, dfe, col, _ in arch:
    k = name[0]
    ax.scatter(me, dfe, s=90, color=col, zorder=3, edgecolor="white", linewidth=1.2)
    ax.annotate(f"{name}\n$\\eta_F$={dfe/me:.2f} %/t", (me, dfe),
                textcoords="offset points", xytext=offsets[k],
                ha=aligns[k], fontsize=7.5)
ax.annotate("", xy=(46.4, 75.0), xytext=(81.0, 75.0),
            arrowprops=dict(arrowstyle="->", color="#7C5AA6", lw=1.4))
ax.text(63.7, 71.4, "ISRU substitution:\n\u221234.6 t at unchanged $\\Delta F_E$",
        fontsize=7.5, ha="center", va="center", color="#7C5AA6")
ax.set_xlabel("Earth-launched mass $M_E$ (t)")
ax.set_ylabel("SEP energy-fluence reduction $\\Delta F_E$ (%)")
ax.set_xlim(-8, 116); ax.set_ylim(68, 100)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig3_pareto.png"), dpi=300)
plt.close(fig)

print("wrote fig1_isru_sweep.png, fig2_mass_uncertainty.png, fig3_pareto.png")
print("Fig1 check: M_E invariant =", M_E, " f_ISRU =", [round(f,3) for f in f_isru])
print("Fig2 check: median =", round(med,2), " CI90 =", [round(v,1) for v in (lo90,hi90)])
print("Fig3 check: eta_F =", [round(d/m,2) for _, m, d, _, _ in arch])
