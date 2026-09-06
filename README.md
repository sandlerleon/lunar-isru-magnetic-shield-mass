# Mass-Minimized Lunar Radiation Protection Using In-Situ Regolith and Distributed Magnetic Shielding

Leon Sandler, Independent Researcher, Northbrook, IL, USA — sandler.leon@gmail.com — ORCID: [0009-0007-4584-808X](https://orcid.org/0009-0007-4584-808X)

Manuscript resubmitted to *Space Weather* (AGU), MS# 2026SW005387, as "Mass-Minimized
Lunar Radiation Protection Using In-Situ Regolith and Distributed Magnetic Shielding:
Physics, Engineering Feasibility, and a Specification for Dose Validation," following
editorial review. The revision fully incorporates the previously-unpublished Boris-pusher
physics (Sections 3–6), adds an engineering-feasibility section (launch, cryogenics,
power, reliability), and adds a radiation-dose-context section connecting the paper's
energy-fluence metric to NASA dose limits and published benchmarks — while stating
explicitly that dose reduction itself is not yet established and specifying the
HZETRN2020/Geant4 transport calculation required to do so.

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

- `manuscript/` — CC BY 4.0:
  - `Lunar_Shield_ISRU_Manuscript.docx` — the current manuscript.
  - `Cover_Letter.docx` — short resubmission cover letter.
  - `Response_to_Editor_Comments.docx` — point-by-point response to the editor's
    decision letter of September 4, 2026.
  - `Lunar_Shield_ISRU_Manuscript_TrackedChanges.docx` — word-level tracked-changes
    comparison against the original submission, per AGU's resubmission checklist.
- `figures/` — the three manuscript figures as separate files, regenerated from the
  model output by `code/generate_figures.py` (AGU requires separate figure files).
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
  - `generate_figures.py` — regenerates Figures 1–3 directly from
    `mass_isru_results.json`, so every plotted value traces to the archived
    calculation rather than to a hand-drawn graphic.

Run with `python scaffold_shield_mass_isru.py` (requires `numpy`,
`matplotlib`); reproduces the manuscript's Section 8-11 headline figures to
within Monte Carlo / interpolation noise (roughly one part in a thousand for
the closed-form results, low tenths of a percentage point for the
regolith-thickness sweep).

## License

Code: MIT (see `code/LICENSE` at repo root — the top-level `LICENSE` file
applies to `code/`). Manuscript: CC BY 4.0 (see `manuscript/LICENSE`).
