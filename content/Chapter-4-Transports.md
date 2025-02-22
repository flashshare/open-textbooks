# Transport Module Theory and Numerical Methods

## Theoretical Background

### Advection-Dispersion Equation
The transport of dissolved and particulate substances in the C-GEM model is governed by the advection-dispersion equation:

$
\frac{\partial c}{\partial t} + U \frac{\partial c}{\partial x} = \frac{\partial}{\partial x} \left( D \frac{\partial c}{\partial x} \right) + S
$

where:

*   $c$ is the concentration of the substance.
*   $U$ is the flow velocity.
*   $D$ is the dispersion coefficient.
*   $S$ is a source/sink term representing local production or consumption.

### TVD Schemes
To minimize numerical oscillations and ensure stability, the C-GEM model uses a Total Variation Diminishing (TVD) scheme for advection. TVD schemes limit the amount of variation in the solution, preventing spurious oscillations.

## Numerical Implementation

### TVD Scheme Implementation

**4. NUMERICAL METHOD FOR TRANSPORT**

After the hydrodynamics step determines water depth and velocity (or discharge) at each grid cell, the model calculates the **transport** of scalar quantities (e.g., nutrients, oxygen, salinity) along the river. This step is essential for water quality and ecological modeling, as it updates the spatial distribution of various chemical species based on advection and dispersion.



### Implementation Overview



The primary files and functions for transport are:

1.  **Transport(t)** in **transport.c**

    *   High-level routine called each time step *after* the hydrodynamics solver finishes.
    *   Iterates over each chemical species in your model (e.g., `v[s].c` for species \(s\)).

2.  **TVD(...)** and **Disp(...)** in **uptransport.c**

    *   **TVD(...)** (Total Variation Diminishing) method for advection.
    *   **Disp(...)** for solving the diffusion/dispersion equation via another tri-diagonal approach.

Overall sequence each time step:

1.  **Openbound(...)** – sets open boundary conditions for each species.
2.  **TVD(...)** – performs the advection step (convective transport).
3.  **Disp(...)** – performs the dispersion (mixing) step using a tri-diagonal solver.

This sequential approach (advection first, then dispersion) is a common **operator splitting** technique.



### Advection with TVD



**Advection** in 1D follows the hyperbolic transport equation:

$
\frac{\partial c}{\partial t} + U\frac{\partial c}{\partial x} = 0,
$

where $c(x,t)$ is the concentration of a given scalar and $U(x,t)$ is the velocity field provided by the hydrodynamic model.

Naive finite-difference schemes can produce **numerical oscillations** or **over-/undershoot**. To mitigate this, your code applies a **TVD (Total Variation Diminishing)** method.

#### TVD Method

*   **Function**: `void TVD(double* co, int s)` in **uptransport.c**
*   **Core Idea**:

    1.  Compute the flux $F_j = U_j \, D_j \, c_j$ at cell interfaces.
    2.  Use slope-limiters (e.g., minmod, superbee, or other) to prevent spurious oscillations.
    3.  Update cell-averaged concentrations with limited slopes to maintain monotonicity.

Typical snippet (schematic):
```c
cfl = fabs(U[j]) * (DELTI) / (2.0 * DELXI);
...
// slope-limiter code
co[j+1] = ...
co[j]   = ...
```

**References** for TVD schemes:
*   Harten, A. (1983). High resolution schemes for hyperbolic conservation laws. *Journal of Computational Physics*, 49(3), 357–393.
*   LeVeque, R. J. (2002). *Finite Volume Methods for Hyperbolic Problems*. Cambridge University Press.



### Dispersion



After the advection step, the model solves a **diffusion-like** (or dispersion) equation:

$
\frac{\partial c}{\partial t} = \frac{\partial}{\partial x} \left( \nu \frac{\partial c}{\partial x} \right),
$

where $\nu$ is the **dispersion coefficient**. In rivers and estuaries, dispersion represents sub-grid mixing due to turbulence, shear flows, and other processes not resolved by the 1D approach.

*   **Function**: `void Disp(double* co)` in **uptransport.c**
*   **Algorithm**: Another tri-diagonal solve, analogous to the hydrodynamic approach:

    1.  Construct a tri-diagonal matrix for $\nu\, \partial^2 c / \partial x^2$.
    2.  Solve it via the Thomas algorithm or a similar direct method.

#### Computing the Dispersion Coefficient

In your model, `Dispcoef(int t)` calculates $\nu$ (stored in `disp[i]`) for each cell $i$. You reference a formula akin to:

$
\nu_i = \nu_0 \;\bigl(\text{some function of }U, B, \text{and flow geometry}\bigr),
$

or the **Van den Burgh** approach. For instance:

```c
void Dispcoef(int t) {
  // e.g., K = ...
  // disp[i] = D0 * ( 1 - beta * (exp( (i - i_dis)*DELXI / AC) - 1 ) );
}
```
This captures how the local flow structure influences mixing. If $\nu_i$ is set too small, mixing is minimal; if too large, numerical diffusion is dominated by the dispersion term.

**References** for river/estuary dispersion:
*   Fischer, H. B. (1979). Mixing in inland and coastal waters. *Academic Press*.
*   LeVeque, R. J. (1996). *Numerical Methods for Conservation Laws.* Birkhäuser.

**7. CONCENTRATION VARIATIONS AND POLLUTANT FATE**

This section explains how the concentrations of various chemical species, including pollutants, vary along the river over time. It considers the combined effects of advection, dispersion, and net reactions in determining the fate and transport of these substances.

|                                                       |
|:------------------------------------------------------|
| \### 7.1 Factors Influencing Concentration Variations |

The concentration of a chemical species at a given location and time is influenced by several factors:

1.  **Advection**: The transport of the species due to the bulk flow of water.
2.  **Dispersion**: The mixing of the species due to turbulence and other processes.
3.  **Net Reactions**: The production or consumption of the species due to biogeochemical reactions.
4.  **Boundary Conditions**: The concentrations of the species at the upstream and downstream boundaries.
5.  **Lateral Inputs**: The addition of the species from tributaries or other sources.

The overall change in concentration can be described by the advection-dispersion-reaction equation:

\$ \frac{\partial c}{\partial t} = -U \frac{\partial c}{\partial x} + \frac{\partial}{\partial x} \left( D \frac{\partial c}{\partial x} \right) + \sum R + S \$

where: \* $c$ is the concentration of the species (e.g., mg/L). \* $t$ is time (s). \* $x$ is the spatial coordinate along the river (m). \* $U$ is the flow velocity (m/s). \* $D$ is the dispersion coefficient (m²/s). \* $\sum R$ represents the sum of all biogeochemical reactions that produce or consume the species (mg/L/s). \* $S$ represents the source or sink terms due to lateral inputs (e.g., tributaries) (mg/L/s).

|                    |
|:-------------------|
| \### 7.2 Advection |

Advection is the primary mechanism for transporting chemical species along the river. The advective flux is given by:

\$ F\_{adv} = U \cdot c \$

where: \* $F_{adv}$ is the advective flux (e.g., mg/L m/s).

The change in concentration due to advection is:

\$ \frac{\partial c}{\partial t}\Big\|\_{adv} = -U \frac{\partial c}{\partial x} \$

This term represents the rate of change of concentration due to the bulk movement of water. The TVD scheme used in the C-GEM model ensures that the advection is simulated accurately and without numerical oscillations. The Courant number ($C_r$) is often used to assess the stability of the numerical scheme:

\$ C_r = \frac{U \Delta t}{\Delta x} \$

where $\Delta t$ is the time step and $\Delta x$ is the spatial step. For stability, $C_r$ should be less than or equal to 1.

|                     |
|:--------------------|
| \### 7.3 Dispersion |

Dispersion accounts for the mixing of chemical species due to turbulence and other processes not resolved by the 1D model. The dispersive flux is given by:

\$ F\_{disp} = -D \frac{\partial c}{\partial x} \$

where: \* $F_{disp}$ is the dispersive flux (e.g., mg/L m/s).

The change in concentration due to dispersion is:

\$ \frac{\partial c}{\partial t}\Big\|\_{disp} = \frac{\partial}{\partial x} \left( D \frac{\partial c}{\partial x} \right) \$

This term represents the rate of change of concentration due to mixing. The dispersion coefficient $D$ is typically parameterized based on flow characteristics and channel geometry. A common formulation is:

\$ D = \alpha\_L U x \$

where $\alpha_L$ is the longitudinal dispersivity (m) and $x$ is the distance downstream from the source.

|                        |
|:-----------------------|
| \### 7.4 Net Reactions |

Biogeochemical reactions can either produce or consume chemical species, affecting their concentrations. The net reaction rate is the sum of all production and consumption rates:

\$ \sum R = \text{Production} - \text{Consumption} \$

The change in concentration due to net reactions is:

\$ \frac{\partial c}{\partial t}\Big\|\_{reac} = \sum R \$

For example, the net reaction rate for nitrate ($NO_3$) would include nitrification (production) and denitrification and phytoplankton uptake (consumption). The specific equations for these reactions are detailed in Section 6.

|                       |
|:----------------------|
| \### 7.5 Tidal Impact |

Tidal forcing can significantly influence the transport and fate of pollutants in tidal rivers.

-   **Tidal Reversal**: Tidal currents can reverse the flow direction, causing pollutants to move upstream and downstream. The tidal velocity can be represented as:

    \$ U\_{tidal} = A \cos(\omega t) \$

    where $A$ is the tidal amplitude and $\omega$ is the tidal frequency.

-   **Tidal Mixing**: Tidal turbulence enhances mixing and dispersion, diluting pollutant concentrations. The effective dispersion coefficient can be increased due to tidal mixing.

-   **Residence Time**: Tidal forcing can increase the residence time of pollutants in certain areas, affecting their exposure to biogeochemical reactions. The residence time can be estimated as:

    \$ T = \frac{V}{Q} \$

    where $V$ is the volume of the river segment and $Q$ is the discharge.

|                                       |
|:--------------------------------------|
| \### 7.6 Case Studies: Pollutant Fate |

#### 7.6.1 Conservative Pollutants

Conservative pollutants are those that do not undergo significant biogeochemical reactions (e.g., chloride). Their fate is primarily determined by advection and dispersion.

-   **Upstream Release**: A pulse release of a conservative pollutant upstream will be advected downstream, with its concentration decreasing due to dispersion. The concentration profile can be approximated by a Gaussian distribution:

    \$ c(x, t) = \frac{M}{\sqrt{4 \pi D t}} \exp \left( -\frac{(x - Ut)^2}{4Dt} \right) \$

    where $M$ is the mass of the pollutant released.

-   **Downstream Release**: A continuous release of a conservative pollutant downstream will result in a plume that extends upstream and downstream, with concentrations decreasing with distance from the source.

#### 7.6.2 Reactive Pollutants

Reactive pollutants are those that undergo significant biogeochemical reactions (e.g., organic matter, nutrients). Their fate is influenced by both physical transport and reaction processes.

-   **Organic Matter**: Organic matter is subject to aerobic degradation, which consumes oxygen and releases carbon dioxide. The concentration of organic matter will decrease over time and distance due to degradation. The degradation can be modeled as a first-order decay:

    \$ \frac{dc}{dt} = -k c \$

    where $k$ is the decay rate constant.

-   **Nutrients**: Nutrients such as nitrogen and phosphorus are subject to uptake by phytoplankton, nitrification, denitrification, and other processes. Their concentrations will vary depending on the balance between these processes.

|                                  |
|:---------------------------------|
| \### 7.7 Management Implications |

Understanding the factors that influence concentration variations and pollutant fate is essential for effective water quality management.

-   **Source Control**: Reducing pollutant inputs at the source is the most effective way to improve water quality.
-   **Flow Management**: Managing river flows can help to control advection and dispersion, affecting pollutant transport.
-   **Habitat Restoration**: Restoring riparian habitats can enhance nutrient uptake and reduce pollutant concentrations.

By simulating these processes, the C-GEM model provides valuable insights into the fate and transport of pollutants in tidal rivers, supporting informed decision-making for water quality management.

Below is a **Markdown-style document** that consolidates the biogeochemical processes (as implemented in **biogeo.c**, **bgboundary.c**, etc.) into one **comprehensive** description, followed by a separate section explaining how final concentrations result from **advection**, **dispersion**, **tidal forcing**, and **net reactions** over time.

------------------------------------------------------------------------

# Comprehensive Guide to Biogeochemical Reactions in C-GEM

## 1. Overview of Biogeochemical Routine

The biogeochemical calculations in C-GEM occur primarily within:

-   **bgboundary()** (in bcforcing.c) – sets boundary concentrations of chemical species each time step.\
-   **Biogeo(t)** (in biogeo.c) – applies local reaction processes (nitrification, O₂ consumption, phytoplankton growth, carbonate equilibria, etc.) after transport has moved species around.

### 1.1 Where Biogeochemistry Fits in the Model Loop

Recall the main time-stepping flow:

1.  **Hyd(t)** – Solve water depth/velocity.\
2.  **bgboundary(t)** – Update boundary concentrations (and lateral inflows).\
3.  **Transport(t)** – Advection and dispersion of each chemical species.\
4.  **Biogeo(t)** – Biogeochemical transformations within each grid cell.

Biogeochemistry always follows the transport step: it modifies concentrations *after* they have been advected or dispersed.

------------------------------------------------------------------------

## 2. Detailed Steps: Biogeo(t)

Inside **biogeo.c**, the function `Biogeo(int t)` typically calls:

1.  **applyDilution(t)**:
    -   Applies tributary inflows to the local cell at each tributary’s `cellIndex`.\
    -   For each species (e.g., O₂, NO₃, TOC, NH₄, etc.), it calculates the difference between the tributary concentration and the local concentration, then partially “mixes” them based on inflow volume and local water volume.
2.  **computeHydrodynamicFluxes(t, i)**:
    -   Often calculates shear stress `tau_b[i]`, potential sediment erosion or deposition rates, and gas exchange parameters (k600, wind-driven flux).\
    -   Example: `o2air[i]` for oxygen flux to/from the atmosphere, or `co2air[i]` for CO₂ evasion.
3.  **computePrimaryProduction(t, i)**:
    -   Phytoplankton growth:
        -   Light-limited production using an irradiance function `I0(t)` and an exponential decay with depth.\
        -   Nutrient-limited uptake for N, P, Si (depending on the type of phytoplankton).\
    -   Mortality (e.g., `phydeath[i][s]`).\
    -   The net effect: some fraction of nutrients is converted into phytoplankton biomass, and oxygen can be produced (photosynthesis) or consumed (dark respiration).
4.  **computeSedimentFluxes(t, i)**:
    -   Erosion/deposition for suspended particulate matter (SPM).\
    -   Links bed shear stress (function of velocity U\[i\], Chezy friction) to net sediment mass exchange.
5.  **computeBiogeochemicalReactions(t, i)**:
    -   **Nitrification**: ( \text{NH}\_4\^+ \rightarrow \text{NO}\_3\^- ) requiring O₂.\
    -   **Denitrification**: ( \text{NO}\_3\^- \rightarrow \text{N}\_2 ) under low-oxygen or anoxic conditions (also consuming TOC).\
    -   **Organic Matter Degradation** (aerobic mineralization of TOC).\
    -   **Stoichiometric Coupling**: e.g., consumption of O₂ or production of CO₂ as by-products of these processes.\
    -   Accumulates “source” or “sink” terms for each species.
6.  **computeCarbonateChemistry(t, i)**:
    -   pH, alkalinity, DIC (Dissolved Inorganic Carbon), CO₂ speciation.\
    -   Potential outgassing or ingassing of CO₂ to/from the atmosphere.\
    -   Updates variables like `v[CO2].c[i]`, `v[DIC].c[i]`, `v[PH].c[i]`.
7.  **updateBiogeochemicalState(t, i)**:
    -   Commits all the reaction terms to the final concentration arrays `v[s].c[i]`.\
    -   For example, O₂ might decrease from nitrification and organic matter oxidation, while NO₃ might increase from nitrification but decrease from denitrification.\
    -   DIC might be added from mineralization or removed by photosynthesis.

### 2.1 Rate Constants and Stoichiometry

The code uses a set of parameters (e.g., `kox, kdenit, knit, kmortality, kmaint`) that often depend on temperature. For instance:

-   `Fhetox(t)` – T-dependent aerobic degradation rate.\
-   `Fnit(t)` – T-dependent nitrification rate.\
-   `Fhetden(t)` – T-dependent denitrification rate.

Stoichiometric ratios, such as Redfield constants, are embedded (e.g., `redn`, `redp`, `redsi`) for how C, N, P, and Si couple in primary production and decomposition.

------------------------------------------------------------------------

## 3. Post-Reaction Concentrations: Tidal Impact, Advection, Dispersion

After each call to **Biogeo(t)**, the code obtains **updated** concentrations of all species. However, in the next time step, these concentrations can change further due to:

1.  **Tidal Elevation** – Water can move downstream or even upstream if tidal forcing is strong, redistributing the mass of each pollutant or nutrient.\
2.  **Advection** – The “bulk flow” of water carrying solutes. If velocity is positive (downstream), substances move in that direction; with tide reversal, velocity can become negative (upstream).\
3.  **Dispersion** – Sub-grid mixing. The function `Disp(...)` in `uptransport.c` handles the second pass of each time step, smoothing concentration gradients.

### 3.1 Combining Advection, Dispersion, and Net Reactions

A typical 1D advection-dispersion-reaction model step for species (c) is:

\[ \frac{\partial c}{\partial t} ;+; U,\frac{\partial c}{\partial x} ;=; D ,\frac{\partial^2 c}{\partial x^2} ;+; \text{(reaction source/sink terms)}, \]

where: - (U) = velocity from hydrodynamics (could be positive or negative due to tidal motion). - (D) = dispersion coefficient. - Reaction terms are the net effect of nitrification, denitrification, phytoplankton uptake, etc.

In C-GEM, this equation is **split** into:

1.  **Advection + Dispersion** (in `Transport(t)`).
2.  **Reactions** (in `Biogeo(t)`).

Hence a pollutant or nutrient “parcel” can experience:

1.  **Transport** – moving along the channel or mixing due to velocity and dispersion.\
2.  **Reactions** – transformation or consumption/production due to biological and chemical processes.

### 3.2 Tidal Effects on Concentration

Because **tidal** forcing at the downstream boundary can reverse velocities or alter flow rates, it can:

-   Cause upstream “push” of saline or polluted water during flood tide.\
-   Increase or decrease local depth (H\[i\]), affecting cross-sectional area and thus impacting concentration (due to volume changes).\
-   Modify the net flux of pollutants, sometimes trapping them in the estuary if tidal amplitude is large relative to river discharge.

### 3.3 Final Concentration Evolution Over Time

At the end of each time step, the concentration in each cell is effectively:

\[ c\_{i}\^{n+1} ;=; \underbrace{\text{AdvDisp}(c_{i}^{n})}*{*\text{Transport}(t)} ;+; \underbrace{\text{Reaction}(c_{i}^{n})}{\text{Biogeo}(t)} . \]

When you run the simulation up to `t=MAXT`, you get a time series of concentrations that reflect:

-   **Flow Patterns** (including tidal oscillations).\
-   **Mixing** (dispersive and advective).\
-   **Reaction Transformations** (production/consumption of each species).

------------------------------------------------------------------------

## 4. Key Takeaways

1.  **bgboundary(t)** sets boundary or lateral inflows for chemical species each time step, ensuring external forcing is correct (tidal salinity, upstream nutrient input, tributary loadings).
2.  **Biogeo(t)** modifies each species internally at each cell, accounting for the entire “reaction network.”\
3.  **Concentrations** are then *transported* in the next time step, subject to tidal forcing, velocity fields, and dispersion.\
4.  The cycle repeats, capturing both **spatial** and **temporal** changes in the water column.

By carefully calibrating the reaction rates and boundary data, C-GEM can simulate how a pollutant or nutrient slug enters the river, moves with the tide, and is partially consumed or transformed by microbial and chemical processes—ultimately giving a dynamic concentration profile along the tidal river over time.

## 

## \### 7.9 References

-   **Chapra, S. C. (2008).** *Surface Water-Quality Modeling*. Waveland Press.
-   **Fischer, H. B. (1979).** *Mixing in Inland and Coastal Waters*. Academic Press.
-   **Thomann, R. V., & Mueller, J. A. (1987).** *Principles of Surface Water Quality Modeling and Control*. Harper & Row.
-   **Wanninkhof, R. (1992).** Relationship between wind speed and gas exchange over the ocean. *Journal of Geophysical Research: Oceans*, 97(C5), 7373-7382.

## \### 7.8 Water Quality Simulation Process Flowchart

Below is a Mermaid flowchart summarizing the steps involved in simulating water quality in each river cell over time within the C-GEM model.
