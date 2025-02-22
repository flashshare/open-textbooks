# Biogeochemical Processes

## Learning Objectives
After completing this chapter, you will be able to:
- Understand the key biogeochemical processes in estuarine systems
- Implement reaction kinetics for nutrient cycling, primary production, and organic matter degradation
- Analyze the interactions between different biogeochemical cycles
- Assess the impact of eutrophication on water quality

## Theoretical Background

### Primary Production
Primary production is the synthesis of organic matter from inorganic carbon and nutrients, driven by sunlight. The C-GEM model simulates primary production by phytoplankton, using a light- and nutrient-limited growth model.

### Nutrient Cycling (N, P, Si)
The C-GEM model simulates the cycling of nitrogen, phosphorus, and silica, which are essential nutrients for phytoplankton growth. The model includes processes such as:

*   Nitrification
*   Denitrification
*   Ammonification
*   Phosphate adsorption and desorption
*   Silica dissolution and precipitation

### Organic Matter Degradation
Organic matter degradation is the breakdown of organic matter into simpler compounds, releasing nutrients and carbon dioxide. The C-GEM model simulates organic matter degradation using a first-order decay model.

### Carbonate Chemistry
The C-GEM model simulates the carbonate chemistry system, which includes dissolved inorganic carbon (DIC), pH, and alkalinity. This system is important for regulating the pH of the water and for controlling the exchange of carbon dioxide between the water and the atmosphere.

### Gas Exchange
The C-GEM model simulates the exchange of oxygen and carbon dioxide between the water and the atmosphere. This process is driven by the difference in partial pressure between the water and the atmosphere.

## Mathematical Formulation

### Primary Production
The gross primary production (GPP) rate for each phytoplankton group is calculated as:

$
GPP[i][s] = P_b[s] \cdot \alpha[s] \cdot I[i] \cdot \text{NutrientLimitation}[i][s] \cdot \text{PhyBiomass}[i][s]
$

where:
*   $GPP[i][s]$ is the gross primary production rate for phytoplankton group $s$ at cell $i$ (e.g., mg C/L/s).
*   $P_b[s]$ is the maximum photosynthetic rate for phytoplankton group $s$ (e.g., /s).  This parameter is often temperature-dependent and can be modeled using a Q10 function (see references).
*   $\alpha[s]$ is the photosynthetic efficiency for phytoplankton group $s$ (e.g., mg C/L/s per unit light).
*   $I[i]$ is the light intensity at cell $i$ (e.g., \(\mu\)E/m²/s).
*   $\text{NutrientLimitation}[i][s]$ is the nutrient limitation factor for phytoplankton group $s$ at cell $i$ (dimensionless, 0 to 1).
*   $\text{PhyBiomass}[i][s]$ is the biomass of phytoplankton group $s$ at cell $i$ (e.g., mg C/L).

### Code Implementation

**8. DETAILED BIOGEOCHEMICAL PROCESSES**

This section provides comprehensive documentation of all biogeochemical processes in the C-GEM model, including academic background, mathematical formulations, and implementation details.


### Variables Overview


Below is an **in-depth walkthrough** of each **biogeochemical reaction** in your model, along with **fully expanded stoichiometric equations** and an explanation of how the code implements them. We then discuss **limitations** and **suitable applications** of these assumptions in your 1D estuarine or river model. Where references appear like \((\dots)\), these expansions reflect typical Redfield-like or extended stoichiometries commonly found in academic water-quality models. Note that actual numeric coefficients in your code might use slightly different or approximate stoichiometric ratios (like $15/106$ or 93.4/106 for partial reaction steps). We will strive here to give the **complete** forms as they appear in standard references, but keep in mind that your code lumps or approximates them for simpler calculation.

---

# 1. Reaction Equations for Each Process

We have four central processes:

1. **Primary Production** (Phytoplankton growth)
2. **Organic Matter Degradation** (Mineralization / Respiration)
3. **Nitrification**
4. **Denitrification**

Additionally, your model includes:

- **Sediment fluxes** (erosion, deposition of SPM)
- **CO₂ exchange** with the atmosphere
- **O₂ exchange** with the atmosphere
- **pH** and **carbon speciation** (DIC partitioning, alkalinity changes)

For completeness, we show not only the symbolic but also the **expanded stoichiometry** with typical Redfield or near-Redfield assumptions, plus how each reaction affects each variable in your code.

---

## Primary Production (Phytoplankton Growth)

### Academic Background

Phytoplankton cells produce biomass using **light**, **inorganic nutrients** (N, P, sometimes Si if they are diatoms), and **CO₂** (or HCO₃⁻) from the water. A generic stoichiometry for “new biomass” might be:

$$ 
\text{Photosynthesis Reaction:} \quad \nu_C\;\mathrm{CO_2} + \nu_N\;\mathrm{NH_4^+} + \nu_P\;\mathrm{PO_4^{3-}} \;\longrightarrow\; \mathrm{(CH_2O)}_{\alpha}\mathrm{(NH_3)}_{\beta}\mathrm{(H_3PO_4)}_{\gamma} \;\;+\; \dots 
$$

In practice, **Redfield** stoichiometry often lumps it as:
\[ 106\, \mathrm{CO_2} + 16\, \mathrm{NH_4^+} \quad (\text{or NO}_3^-) + 1\, \mathrm{HPO_4^{2-}} + \dots \;\;\longrightarrow\;\; \mathrm{C}_{106}\mathrm{H}_{175}\mathrm{O}_{110}\mathrm{N}_{16}\mathrm{P}_{1} + \dots \]
The exact stoichiometric coefficients vary across references, but in your code, it’s typically simplified and separated into “NO₃ uptake fraction” vs. “NH₄ uptake fraction.”

#### If Silica is needed (for diatoms):
\[ \mathrm{SiO_2 \;somehow\;incorporated\;into\;cell\;wall.} \]

### Code Implementation

In **computePrimaryProduction()**:
1. The code calculates **Gross Primary Production** (GPP) from light-limitation + nutrient-limitation factor.  
2. It splits GPP into two net productions:  
   - \( \mathrm{NPP\_NO3}[i][s] \) for the fraction that uses NO\(_3\),  
   - \( \mathrm{NPP\_NH4}[i][s] \) for the fraction that uses NH\(_4\).  

Hence we might see a reaction like:

\[ \underbrace{ (\alpha)\,\mathrm{CO_2} + (\beta)\,\mathrm{NO_3^-} + (\gamma)\,\mathrm{NH_4^+} + (\delta)\,\mathrm{PO_4^{3-}} + (\epsilon)\,\mathrm{SiO_2} }_{\text{consumed}} \quad \longrightarrow \quad \text{Phytoplankton biomass} + \text{O}_2 \]

**Effects** on variables:
- **DIC** decreases (because CO₂ is taken up),
- **NO₃** or **NH₄** decreases (nutrient used),
- **PO₄** might decrease,
- **Si** might decrease (for diatoms),
- **O₂** typically **increases**.

Furthermore, the code also includes:

- **Mortality**: a fraction of the newly formed biomass is lost at rate `kmort(t,s)`, returning to organic matter or releasing NH\(_4\).

---

## Organic Matter Degradation (Mineralization / Respiration)

### Academic Background

When organic matter (represented by \(\mathrm{(CH_2O)}_n(\mathrm{NH_3})_m(\mathrm{PO_4})_p ...\)) is respired:

- **Aerobic respiration** (if O₂ is available):
  \[ \mathrm{(CH_2O)}_n + \alpha\,\mathrm{NH_3} + ... + O_2 \;\longrightarrow\; n\,\mathrm{CO_2} + \alpha\,\mathrm{NH_4^+} + \dots + \text{(some H_2O)}. \]
  This yields CO₂ (+DIC) and consumes O₂.

### Code Implementation

In your function `computeBiogeochemicalReactions()`, the line:
```c
adegrad[i] = ...
```
represents the “rate of aerobic degradation” of TOC, modulated by O₂ availability. The model might track total organic carbon “TOC” or two fractions (fast vs. slow). Numerically, for each 1 mgC of organic matter respired:
- DIC (CO₂) **increases** by 1 mgC,
- O₂ **decreases** proportionally,
- Alkalinity shift is small if we assume the organic matter’s N is in NH₂ form, but the code can incorporate small stoichiometric offsets.

---

## Nitrification

### Academic Background

**Nitrification**:  
\[ \mathrm{NH_4^+} + 1.5 \, \mathrm{O_2} \;\longrightarrow\; \mathrm{NO_2^-} + 2\,\mathrm{H^+} \]
then
\[ \mathrm{NO_2^-} + 0.5\,\mathrm{O_2} \;\longrightarrow\; \mathrm{NO_3^-} \]
Often simplified as a single step:
\[ \mathrm{NH_4^+} + 2 \,\mathrm{O_2} \;\longrightarrow\; \mathrm{NO_3^-} + 2\,\mathrm{H^+} + \mathrm{H_2O}. \]
Generates 2 protons per NH\(_4^+\), strongly **lowering** alkalinity. Also **consumes** O₂.

### Code Implementation

In `computeBiogeochemicalReactions()`:
```c
nitrif[i] = (Fnit(t)*v[O2].c[i]/(v[O2].c[i]+KO2_nit))*(v[NH4].c[i]/(v[NH4].c[i]+KNH4));
```
**Stoichiometry effect** on variables:
- **NH₄** decreases,
- **NO₃** increases,
- **O₂** decreases,
- **Alkalinity** decreased by 2 eq. per mole NH₄ nitrified (the code implements it with `- 2.0*nitrif[i]` in `reactionTA[i]`).

---

## Denitrification

### Academic Background

In anoxic or low-O₂ conditions, bacteria use NO\(_3\) as an electron acceptor to oxidize organic matter:

$$
\mathrm{NO_3^-} + \mathrm{(CH_2O)} \;\longrightarrow\; \mathrm{CO_2} + \mathrm{N_2} + \dots + \text{Alk gain}.
$$
This **consumes** NO\(_3\), **produces** CO₂ (+DIC) and typically **raises** alkalinity (since removing the negative charge from the water frees up base equivalents).

### Code Implementation

```c
denit[i] = (Fhetden(t)* v[TOC].c[i]/(v[TOC].c[i]+KTOC)) *
           (KinO2/(v[O2].c[i]+KinO2)) *
           (v[NO3].c[i]/(v[NO3].c[i]+KNO3));
```
The factor `(KinO2/(v[O2].c[i] + KinO2))` ensures denitrification is favored at low O₂.  
**Stoichiometric effect**:
- **NO₃** decreases,
- **DIC** increases,
- **Alkalinity** increases,
- Possibly N₂ is formed (the model typically doesn’t track N₂ explicitly, it just disappears from the system).

---

## Putting It Together: reactionDIC & reactionTA

Your code lumps these individual reaction stoichiometries into two arrays:

- `reactionDIC[i] = (adegrad[i]) + (denit[i]) - NPP[i]`
- `reactionTA[i] = (some function of adegrad, denit, nitrif, etc.)`

For instance:
```c
reactionTA[i] = (15.0/106.0)*adegrad[i] 
              + (93.4/106.0)*denit[i] 
              - 2.0 * nitrif[i]
              + ...
```
Here, `15.0/106.0` or `93.4/106.0` come from partial expansions of the Redfield ratio (C:N:P = 106:16:1) and typical subreactions for organic matter mineralization or denitrification. They are an approximate approach to keep track of each reaction’s net effect on alkalinity (H⁺ consumed/produced).

---

# 2. Gas Exchange with Atmosphere

## O₂ Gas Exchange
\[ F_{O_2} = k_{O2}( [O_2]_\mathrm{sat} - [O_2]_\mathrm{local} ) \]
If local O₂ < saturation, flux is positive.  
In code:  
```c
o2air[i] = (k600_O2 / PROF[i]) * (O2sat(t, i) - v[O2].c[i]);
```
**O₂** is updated by `+ (o2air[i] * DELTI)` if the flux is positive.

## CO₂ Exchange
After the pH solver calculates `[CO₂(aq)]`, the partial pressure is compared to atmospheric pCO₂. If `[CO₂(aq)]` > CO₂_sat, the flux to air is positive. The code uses:
```c
co2air[i] = (k600_CO2 / PROF[i]) * ( v[CO2].c[i] - CO2_saturation );
```
Then subtracted from `DIC`:

```c
v[DIC].c[i] -= co2air[i]*PROF[i]*DELTI;
```

---

# 3. Carbonate Chemistry and pH

## Full Reaction Set

We have equilibrium equations for:
1. \( \mathrm{CO_2(aq)} + \mathrm{H_2O} \rightleftharpoons \mathrm{HCO_3^-} + \mathrm{H^+} \quad (K_1)\)
2. \( \mathrm{HCO_3^-} \rightleftharpoons \mathrm{CO_3^{2-}} + \mathrm{H^+} \quad (K_2)\)
3. Possibly boron, water autoionization, etc.

**Alkalinity** is defined (in simplified form) as
\[ \mathrm{AT} = [\mathrm{HCO_3^-}] + 2[\mathrm{CO_3^{2-}}] + \dots \]
**DIC** is
\[ \mathrm{DIC} = [\mathrm{CO_2(aq)}] + [\mathrm{HCO_3^-}] + [\mathrm{CO_3^{2-}}]. \]
Hence we solve for pH by ensuring that the updated \(\mathrm{DIC}\) and \(\mathrm{AT}\) match the equilibrium distribution consistent with \(\mathrm{K}_1,\mathrm{K}_2,\dots\).

### Code Steps

1. Start from old pH guess: `H = 10^( - v[PH].c[i] )`.
2. Evaluate the partial fractions of DIC (xi1, xi2, etc.).
3. Evaluate the difference: `temp = AT - f(H, DIC, K1, K2, ...)`.
4. Refine `H` with some numerical approach (Newton or bisection).
5. Once converged, store `v[PH].c[i] = -log10(H)`.
6. Partition DIC:
   \[ [\mathrm{CO_2(aq)}] = \frac{\mathrm{DIC}}{ 1 + \frac{K_1}{H} + \frac{K_1 K_2}{H^2} },\dots \]
7. Then do CO₂ outgassing step to correct DIC if the partial pressure is above atmospheric.

---

# 4. Full Example of Stoichiometric Reactions

Here is a **combined** set of expansions that demonstrate typical “Redfield-based” transformations. We approximate organic matter as \(\mathrm{C}_{106}\mathrm{H}_{175}\mathrm{O}_{110}\mathrm{N}_{16}\mathrm{P}\). You might only track “TOC,” ignoring the exact atomic ratio, but academically:

**(A) Primary Production** (using NO₃ as the main N source, ignoring micronutrients):
\[ 106\,\mathrm{CO_2} + 16\,\mathrm{NO_3^-} + \mathrm{HPO_4^{2-}} + \dots \;\longrightarrow\; \mathrm{C}_{106}\mathrm{H}_{175}\mathrm{O}_{110}\mathrm{N}_{16}\mathrm{P}_1 + 106\,\mathrm{O_2}. \]

If half the N is from NH₄, we adjust the stoichiometry. Similarly, if diatoms need Si, we might add \(\mathrm{n\,Si(OH)_4}\).

**(B) Aerobic Mineralization**:
\[ \mathrm{C}_{106}\mathrm{H}_{175}\mathrm{O}_{110}\mathrm{N}_{16}\mathrm{P} + 106\,\mathrm{O_2} \;\longrightarrow\; 106\,\mathrm{CO_2} + 16\,\mathrm{NH_4^+} + \mathrm{HPO_4^{2-}} + \dots \]
(If we assume some fraction of NH₄ is nitrified, we separate that out.)

**(C) Nitrification** (entirely):
\[ \mathrm{NH_4^+} + 2\,\mathrm{O_2} \;\longrightarrow\; \mathrm{NO_3^-} + 2\,\mathrm{H^+} + \mathrm{H_2O}. \]

**(D) Denitrification**:
$$
\mathrm{NO_3^-} + \mathrm{(CH_2O)} \;\longrightarrow\; \mathrm{CO_2} + \mathrm{N_2} + \dots + \text{Alk gain}.
$$

---

# 5. Limitations and Suitability of These Assumptions

1. **1D Well-Mixed Approach**  
   - The model treats each cell as vertically and laterally “well-mixed.” This is fine for relatively narrow, shallow rivers or estuaries with strong tidal mixing, but may be **less accurate** if the cross-sectional variation is large or if there's strong stratification.

2. **Constant Stoichiometric Ratios**  
   - The partial expansions for `reactionTA[i]` or `reactionDIC[i]` rely on **fixed** stoichiometries (like $15/106$) that do not vary with changing algal composition or seasonal changes in organic matter quality. This is **typical** for many water-quality models, but real systems might have more complex elemental ratios.

3. **No S or Fe cycles**  
   - The model focuses on carbon, nitrogen, phosphorus, silica. It does not incorporate sulfate reduction, iron transformations, or other advanced redox processes. In reality, these can matter in highly anoxic sediments or water columns.

4. **Ignoring Microbial Kinetics**  
   - The model lumps large sets of microbial species (ammonia oxidizers, nitrite oxidizers, etc.) into single rate laws. This is a typical approach, but it is a **simplification** that may fail if specialized processes like anammox become important.

5. **Single Gas Transfer Approach**  
   - O₂ and CO₂ fluxes to atmosphere use a single "k600" style formula. Real gas exchange can vary with wind fetch, waves, etc. Also, we do not track, e.g., CH₄ or N₂O, so greenhouse gas fluxes from other processes are neglected.

6. **pH Solver**  
   - We assume equilibrium. If the timescale of acid-base rearrangements is extremely fast, that’s correct. But if you had superfast pH changes or partial chemical disequilibrium, that might not hold.

7. **Timescales**  
   - This model uses a certain time step (e.g., seconds to hours). If your user tries to run it with a huge time step that surpasses stability conditions, the results can be numerically inaccurate.

8. **Continuous Input Data**  
   - We assume boundary conditions and tributary data are available. If those data are poor quality or missing, the model reliability declines.

### When This Model is **Suitable**:
- Eutrophic or mesotrophic **estuarine** or **river** systems with strong mixing, where major redox processes revolve around O₂, NO₃, NH₄.  
- Applications focusing on **pH, CO₂ flux,** and **nutrient-limited** algal growth.  
- Seasonal to multi-year timescales for management or climate change scenarios.  
- Systems where a 1D approach is enough to capture the main gradient (fresh to brackish to marine).

### When It’s **Less Suitable**:
- Strongly stratified estuaries with big vertical gradients.  
- Highly ephemeral or short timescale events (e.g., pulses of anoxia).  
- Need for explicit Fe, S, or trace metal cycles.  
- Very shallow or complex geometry requiring 2D or 3D flow fields.

---

# 6. Conclusion

Your code merges **academic stoichiometries** for primary production, mineralization, nitrification, and denitrification with **practical** numeric approximations (like partial Redfield expansions in `reactionTA[i]` and `reactionDIC[i]`). It **updates** each variable’s concentration at every time step, factoring in:

1. **Transport & Inflows** (advection, dispersion, tributary dilution),
2. **Biological transformations** (the four big processes above),
3. **Gas exchange** (O₂, CO₂),
4. **pH** (through a carbonate equilibrium solver based on DIC & alkalinity changes).

**Limitations** revolve around the **1D assumption**, **fixed stoichiometric** ratios, **no advanced redox** beyond NO₃, **no multi-dimensional** flow fields, and **equilibrium** pH approach. But these are standard in many well-known water-quality models, making your approach quite **suitable** for broad, well-mixed **tidal rivers** or **coastal** systems, especially for analyses of eutrophication, oxygen depletion, and **CO₂** fluxes over timescales from days to seasons to years.

**6. BIOGEOCHEMICAL REACTION CALCULATIONS**

This section provides a detailed overview of the biogeochemical reactions calculated within the C-GEM model. It explains the key processes, rate equations, and parameters involved in simulating the transformations of various chemical species. We will focus particularly on eutrophication and the inorganic carbon module.

## Code Implementation
// Indicate calls to Biogeo(t) for each time step


### Primary Production


**Primary production** is the synthesis of organic compounds from atmospheric or aquatic carbon dioxide, primarily through photosynthesis. In the C-GEM model, primary production is simulated for two phytoplankton groups: siliceous (Phy1) and non-siliceous (Phy2).

#### Photosynthesis Rate

The gross primary production (GPP) rate for each phytoplankton group is calculated as:

$
GPP[i][s] = P_b[s] \cdot \alpha[s] \cdot I[i] \cdot \text{NutrientLimitation}[i][s] \cdot \text{PhyBiomass}[i][s]
$

where:
*   $GPP[i][s]$ is the gross primary production rate for phytoplankton group $s$ at cell $i$ (e.g., mg C/L/s).
*   $P_b[s]$ is the maximum photosynthetic rate for phytoplankton group $s$ (e.g., /s).  This parameter is often temperature-dependent and can be modeled using a Q10 function (see references).
*   $\alpha[s]$ is the photosynthetic efficiency for phytoplankton group $s$ (e.g., mg C/L/s per unit light).
*   $I[i]$ is the light intensity at cell $i$ (e.g., \(\mu\)E/m²/s).
*   $\text{NutrientLimitation}[i][s]$ is the nutrient limitation factor for phytoplankton group $s$ at cell $i$ (dimensionless, 0 to 1).
*   $\text{PhyBiomass}[i][s]$ is the biomass of phytoplankton group $s$ at cell $i$ (e.g., mg C/L).

#### Nutrient Limitation

The nutrient limitation factor is calculated based on the availability of essential nutrients such as nitrogen (N), phosphorus (P), and silica (Si):

$
\text{NutrientLimitation}[i][s] = \min \left( f_N[i][s], f_P[i][s], f_{Si}[i][s] \right)
$

where:
*   $f_N[i][s]$ is the nitrogen limitation factor.
*   $f_P[i][s]$ is the phosphorus limitation factor.
*   $f_{Si}[i][s]$ is the silica limitation factor (only for siliceous phytoplankton).

The individual nutrient limitation factors are calculated using Michaelis-Menten kinetics:

$
f_N[i][s] = \frac{NO_3[i] + NH_4[i]}{K_N[s] + NO_3[i] + NH_4[i]}
$

$
f_P[i][s] = \frac{PO_4[i]}{K_{PO4}[s] + PO_4[i]}
$

$
f_{Si}[i][s] = \frac{Si[i]}{K_{Si}[s] + Si[i]}
$

where:
*   $NO_3[i]$ is the nitrate concentration at cell $i$ (e.g., mg N/L).
*   $NH_4[i]$ is the ammonium concentration at cell $i$ (e.g., mg N/L).
*   $PO_4[i]$ is the phosphate concentration at cell $i$ (e.g., mg P/L).
*   $Si[i]$ is the silica concentration at cell $i$ (e.g., mg Si/L).
*   $K_N[s]$, $K_{PO4}[s]$, and $K_{Si}[s]$ are the half-saturation constants for nitrogen, phosphorus, and silica, respectively, for phytoplankton group $s$ (e.g., mg/L).  These constants represent the nutrient concentration at which the growth rate is half of its maximum value.

#### Light Limitation

The light intensity $I[i]$ at cell $i$ is affected by depth and turbidity:

$
I[i] = I_0 \cdot e^{(-k_{bg} \cdot z[i] - k_{spm} \cdot SPM[i] \cdot z[i])}
$

where:
*   $I_0$ is the surface light intensity (e.g., \(\mu\)E/m²/s).
*   $k_{bg}$ is the background light attenuation coefficient (e.g., /m).
*   $k_{spm}$ is the light attenuation coefficient due to suspended particulate matter (SPM) (e.g., m²/mg).
*   $z[i]$ is the depth of cell $i$ (m).
*   $SPM[i]$ is the concentration of suspended particulate matter at cell $i$ (e.g., mg/L).

#### Net Primary Production

The net primary production (NPP) rate is calculated by subtracting respiration and excretion losses from the GPP rate:

$
NPP[i][s] = GPP[i][s] - k_{excr}[s] \cdot \text{PhyBiomass}[i][s] - k_{maint}[s] \cdot \text{PhyBiomass}[i][s]
$

where:
*   $k_{excr}[s]$ is the excretion rate constant for phytoplankton group $s$ (e.g., /s).
*   $k_{maint}[s]$ is the maintenance respiration rate constant for phytoplankton group $s$ (e.g., /s).

**Code Reference**: These parameters are typically assigned in the `assignBiogeochemicalRateConstants()` function in `init.c`.


### Nutrient Cycling and Eutrophication


The C-GEM model simulates the cycling of key nutrients, including nitrogen, phosphorus, and silica.  Excessive nutrient loading, particularly of nitrogen and phosphorus, can lead to **eutrophication**, characterized by excessive phytoplankton growth, oxygen depletion, and potential harm to aquatic life.

#### Nitrogen Cycle

The nitrogen cycle includes processes such as nitrification, denitrification, and ammonification.

*   **Nitrification**: The oxidation of ammonium ($NH_4$) to nitrite ($NO_2$) and then to nitrate ($NO_3$):

    $ NH_4^+ \xrightarrow{\text{Nitrification}} NO_2^- \xrightarrow{\text{Nitrification}} NO_3^- $

    The nitrification rate is calculated as:

    $ \text{Nitrification}[i] = k_{nit} \cdot \frac{O_2[i]}{K_{O2\_nit} + O_2[i]} \cdot NH_4[i] $

    where:
    *   $k_{nit}$ is the nitrification rate constant (e.g., /s).
    *   $O_2[i]$ is the oxygen concentration at cell $i$ (e.g., mg/L).
    *   $K_{O2\_nit}$ is the half-saturation constant for oxygen in nitrification (e.g., mg/L).  This term reflects the oxygen dependence of nitrifying bacteria.

*   **Denitrification**: The reduction of nitrate to nitrogen gas ($N_2$) under anaerobic conditions:

    $ NO_3^- \xrightarrow{\text{Denitrification}} N_2 $

    The denitrification rate is calculated as:

    $ \text{Denitrification}[i] = k_{denit} \cdot \frac{K_{inO2}}{K_{inO2} + O_2[i]} \cdot NO_3[i] $

    where:
    *   $k_{denit}$ is the denitrification rate constant (e.g., /s).
    *   $K_{inO2}$ is the inhibition constant for oxygen in denitrification (e.g., mg/L).  This term reflects the oxygen inhibition of denitrifying bacteria.

*   **Ammonification**: The decomposition of organic matter, releasing ammonium:

    $ \text{Organic Matter} \xrightarrow{\text{Ammonification}} NH_4^+ $

    The ammonification rate is linked to the aerobic degradation of total organic carbon (TOC):

    $ \text{Ammonification}[i] = k_{ox} \cdot \frac{O_2[i]}{K_{O2\_ox} + O_2[i]} \cdot redn \cdot TOC[i] $

    where:
    *   $k_{ox}$ is the aerobic degradation rate constant (e.g., /s).
    *   $K_{O2\_ox}$ is the half-saturation constant for oxygen in aerobic degradation (e.g., mg/L).
    *   $redn$ is the nitrogen-to-carbon ratio in organic matter.
    *   $TOC[i]$ is the total organic carbon concentration at cell $i$ (e.g., mg C/L).

**Code Reference**: These reactions are typically implemented in the `computeBiogeochemicalReactions()` function in `biogeo.c`.

#### Phosphorus Cycle

The phosphorus cycle primarily involves the uptake and release of phosphate ($PO_4$).

*   **Phosphate Uptake**: Phytoplankton uptake of phosphate is already accounted for in the nutrient limitation term of primary production.
*   **Phosphate Release**: Decomposition of organic matter releases phosphate, similar to ammonification:

    $ \text{Phosphate Release}[i] = k_{ox} \cdot \frac{O_2[i]}{K_{O2\_ox} + O_2[i]} \cdot redp \cdot TOC[i] $

    where $redp$ is the phosphorus-to-carbon ratio in organic matter.

#### Silica Cycle

The silica cycle is relevant for siliceous phytoplankton (diatoms).

*   **Silica Uptake**: Diatoms uptake silica for cell wall formation, accounted for in the nutrient limitation term of primary production.
*   **Silica Release**: Dissolution of diatom frustules releases silica:

    $ \text{Silica Release}[i] = k_{dissolution} \cdot \text{DiatomBiomass}[i] $

    where $k_{dissolution}$ is the dissolution rate constant for diatom frustules.


### Inorganic Carbon Module


The inorganic carbon module simulates the speciation of dissolved inorganic carbon (DIC) and its interactions with pH and alkalinity. This is crucial for understanding carbon cycling and the impacts of eutrophication on pH and CO2 fluxes.

#### Carbonate Chemistry

The key components of the inorganic carbon system are:

*   Dissolved carbon dioxide ($CO_2(aq)$)
*   Carbonic acid ($H_2CO_3$)
*   Bicarbonate ion ($HCO_3^−$)
*   Carbonate ion ($CO_3^{2−}$)

These species are related through the following equilibrium reactions:

$ CO_2(g) \rightleftharpoons CO_2(aq) $

$ CO_2(aq) + H_2O \rightleftharpoons H_2CO_3 $

$ H_2CO_3 \rightleftharpoons H^+ + HCO_3^- $

$ HCO_3^- \rightleftharpoons H^+ + CO_3^{2-} $

The equilibrium constants for these reactions are temperature-dependent and can be calculated using empirical formulas (see references).  For example, the first and second dissociation constants for carbonic acid ($K_1$ and $K_2$) are often calculated using equations from:

*   **Millero, F. J. (1995).** *Chemical Oceanography*. CRC Press.
*   **Dickson, A. G., & Riley, J. P. (1979).** *Marine Chemistry*, 7(2), 89-99.

The temperature dependence of $K_1$ and $K_2$ can be expressed as:

$ \log K_1 = a_1 + \frac{b_1}{T} + c_1 \log(T) $

$ \log K_2 = a_2 + \frac{b_2}{T} + c_2 \log(T) $

where $T$ is the temperature in Kelvin, and $a_i$, $b_i$, and $c_i$ are empirical constants.

#### pH Calculation

The pH is calculated based on the concentrations of the inorganic carbon species and the total alkalinity (AT). Alkalinity is defined as the acid-neutralizing capacity of the water and is primarily determined by the concentrations of bicarbonate and carbonate ions.

The pH can be calculated iteratively using a charge balance equation:

$ [H^+] + \sum \text{Cations} = [OH^-] + \sum \text{Anions} $

where the cations and anions include the inorganic carbon species, as well as other ions such as calcium, magnesium, and sulfate.  A simplified charge balance equation often used in freshwater systems is:

$ [H^+] + 2[Ca^{2+}] + 2[Mg^{2+}]  = [OH^-] + [HCO_3^-] + 2[CO_3^{2-}] + [Cl^-] + [SO_4^{2-}] $

Total Alkalinity (TA) is defined as:

$ TA = [HCO_3^-] + 2[CO_3^{2-}] + [OH^-] - [H^+] $

The concentrations of $HCO_3^-$ and $CO_3^{2-}$ can be expressed in terms of $CO_2(aq)$, $K_1$, $K_2$, and $[H^+]$:

$ [HCO_3^-] = \frac{K_1 [H_2CO_3]}{[H^+]} $

$ [CO_3^{2-}] = \frac{K_2 [HCO_3^-]}{[H^+]} = \frac{K_1 K_2 [H_2CO_3]}{[H^+]^2} $

#### CO2 Air-Water Exchange

The exchange of CO2 between the water and the atmosphere is driven by the difference in partial pressure of CO2:

$ F_{CO2} = k_{gas} \cdot (pCO2_{water} - pCO2_{atmosphere}) $

where:
*   $F_{CO2}$ is the CO2 flux (e.g., mmol/m²/day).
*   $k_{gas}$ is the gas transfer velocity, which depends on wind speed and temperature.  A common formulation for $k_{gas}$ is based on wind speed (see references):

    $ k_{gas} = 0.31 \cdot U_{10}^2 \cdot (Sc / 600)^{-0.5} $

    where $U_{10}$ is the wind speed at 10 meters above the surface, and $Sc$ is the Schmidt number for CO2. The Schmidt number is temperature-dependent and can be calculated using empirical formulas:

    $ Sc = A - B \cdot T + C \cdot T^2 - D \cdot T^3 $

    where $T$ is the temperature in Celsius, and A, B, C, and D are empirical constants (Wanninkhof, 1992).
*   $pCO2_{water}$ is the partial pressure of CO2 in the water.
*   $pCO2_{atmosphere}$ is the partial pressure of CO2 in the atmosphere.

The partial pressure of CO2 in water is related to the concentration of dissolved CO2 by Henry's Law:

$ pCO2_{water} = [CO_2(aq)] / K_H $

where $K_H$ is Henry's constant, which is also temperature-dependent.

**Code Reference**: The carbonate chemistry calculations are typically implemented in the `computeCarbonateChemistry()` function in `biogeo.c`.


### Other Reactions


#### Aerobic Degradation of TOC

The aerobic degradation of total organic carbon (TOC) is a key process in the carbon cycle:

$ \text{TOC Degradation}[i] = k_{ox} \cdot \frac{O_2[i]}{K_{O2\_ox} + O_2[i]} \cdot TOC[i] $

This process consumes oxygen and releases carbon dioxide, contributing to oxygen depletion and changes in the inorganic carbon system.

#### Phytoplankton Death

Phytoplankton mortality releases organic matter and nutrients:

$ \text{Phytoplankton Death}[i][s] = k_{mortality}[s] \cdot \text{PhyBiomass}[i][s] $

where $k_{mortality}[s]$ is the mortality rate constant for phytoplankton group $s$.


### Stoichiometry


Stoichiometric ratios (e.g., Redfield ratios) are used to link the different biogeochemical cycles. For example, the carbon-to-nitrogen-to-phosphorus ratio (C:N:P) is approximately 106:16:1. These ratios are used to calculate the release or uptake of nutrients during organic matter decomposition or primary production.


### References


*   **Chapra, S. C. (2008).** *Surface Water-Quality Modeling*. Waveland Press.
*   **Soetaert, K., & Herman, P. M. J. (2009).** *A Practical Guide to Ecological Modelling*. Springer.
*   **Wetzel, R. G. (2001).** *Limnology: Lake and River Ecosystems*. Academic Press.
*   **Zeebe, R. E., & Wolf-Gladrow, D. (2001).** *CO2 in Seawater: Equilibrium, Kinetics, Isotopes*. Elsevier.
*   **Millero, F. J. (1995).** *Chemical Oceanography*. CRC Press.
*   **Dickson, A. G., & Riley, J. P. (1979).** *Marine Chemistry*, 7(2), 89-99.
*   **Wanninkhof, R. (1992).** Relationship between wind speed and gas exchange over the ocean. *Journal of Geophysical Research: Oceans*, 97(C5), 7373-7382.