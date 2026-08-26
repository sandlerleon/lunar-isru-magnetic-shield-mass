# Mass-Minimized Lunar Radiation Protection Using In-Situ Regolith and Distributed Magnetic Shielding

Leon Sandler, Independent Researcher, Northbrook, IL, USA — sandler.leon@gmail.com

Manuscript prepared for submission to *Space Weather* (AGU), MS# 2026SW005387.

## Summary

Evaluates a distributed superconducting magnetic "fence" for lunar surface
protection against solar energetic particle (SEP) events under an explicit
Earth-launched-mass constraint. Tests and rules out permanent magnets as a
substitute moment source, propagates previously uncosted engineering margins
into a Monte Carlo mass budget, and develops an in-situ-resource-utilization
(ISRU) architecture that substitutes regolith-derived structure for
Earth-launched structural mass. Separately models direct regolith cladding
for fixed equipment via a first-order CSDA slab-attenuation calculation.
Concludes that the optimal lunar SEP-mitigation strategy is asset-dependent:
regolith cladding for fixed equipment, an ISRU-structural magnetic fence for
mobile/EVA assets that regolith cannot reach.

The retained relativistic Boris-pusher SEP-attenuation physics (Sections 2-7:
fence-vs-monolith baseline, moment-budget scaling law, chiral-winding effect)
is unchanged from the prior physics-focused analysis, archived separately at
[github.com/sandlerleon/magdome](https://github.com/sandlerleon/magdome) /
[10.5281/zenodo.21179710](https://doi.org/10.5281/zenodo.21179710).

## Contents

- `manuscript/` — full manuscript (Word), CC BY 4.0.
- `code/` — Python/NumPy simulation and calculation code, MIT license:
  - `scaffold_shield_sim.py` — the validated relativistic Boris-pusher core
    (geometry builders, field solver, particle push), reused unchanged from
    the prior physics paper.
  - `scaffold_shield_mass_isru.py` — this paper's new contributions
    (Sections 8-11): permanent-magnet moment-per-mass feasibility check
    (with an independent Boris-pusher re-run at the NdFeB-equivalent moment
    budget), the engineering mass-budget Monte Carlo (N=300,000), the ISRU
    structural-mass allocation and regolith-multiplier sweep, and the CSDA
    regolith slab-attenuation thickness sweep. Each result prints next to
    the manuscript's stated figure for direct comparison.
  - `mass_isru_results.json` — machine-readable output of the above run.

Run with `python scaffold_shield_mass_isru.py` (requires `numpy`,
`matplotlib`); reproduces the manuscript's Section 8-11 headline figures to
within Monte Carlo / interpolation noise (roughly one part in a thousand for
the closed-form results, low tenths of a percentage point for the
regolith-thickness sweep).

## License

Code: MIT (see `code/LICENSE` at repo root — the top-level `LICENSE` file
applies to `code/`). Manuscript: CC BY 4.0 (see `manuscript/LICENSE`).
