---
jupyter: python3
---

# Introduction to the C-GEM Model

## Learning Objectives

After completing this chapter, you will be able to: - Understand the fundamental principles of estuarine modeling - Identify key processes in tidal river systems - Recognize the coupling between physical and biogeochemical processes - Navigate the C-GEM model structure and implementation

## Theoretical Background

### Estuarine Systems

Estuaries are transitional zones where rivers meet the sea, characterized by: - Tidal influence - Salinity gradients - Complex biogeochemical processes - Anthropogenic pressures


```python
import pandas as pd
import 
```

### Modeling Approach

Based on Volta et al. (2016), C-GEM adopts a one-dimensional approach because: - Most estuaries are well-mixed vertically - Longitudinal gradients dominate over lateral variations - Computational efficiency is critical for long-term simulations

## Model Framework

The C-GEM model is a one-dimensional (1D) numerical model designed to simulate hydrodynamics, transport, and biogeochemical processes in tidal rivers and estuaries. It is intended for use in:

-   Water quality assessment
-   Eutrophication studies
-   Total Maximum Daily Load (TMDL) development
-   Climate change impact assessment

Refer to key functions: Hyd(t) in hyd.c, Transport(t) in transport.c, Biogeo(t) in biogeo.c

## Equation Summaries

The model couples three main systems of equations:

1.  **Hydrodynamics**: Saint-Venant equations $\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = 0$

2.  **Transport**: Advection-dispersion equation $\frac{\partial c}{\partial t} + u\frac{\partial c}{\partial x} = \frac{\partial}{\partial x}(D\frac{\partial c}{\partial x})$

3.  **Biogeochemistry**: Reaction networks $\frac{dc_i}{dt} = \sum_j R_{ij}(c_1,...,c_n)$

## Code Implementation Details

The C-GEM model consists of three primary modules:

1.  **Hydrodynamics:** Simulates water flow, water depth, and velocity.
2.  **Transport:** Simulates the movement and mixing of dissolved and particulate substances.
3.  **Biogeochemistry:** Simulates the transformation of chemical and biological constituents.

Example: “Look up readConfig() in init.c for configuration reading logic.”

## Model Limitations and Assumptions

The C-GEM model is based on the following assumptions:

-   One-dimensional flow: The model assumes that the river or estuary is well-mixed vertically and laterally.
-   Hydrostatic pressure: The model assumes that the pressure is hydrostatic.
-   Incompressible fluid: The model assumes that water is incompressible.
-   Constant water density: The model assumes that the water density is constant.
-   Simplified biogeochemical processes: The model uses simplified representations of biogeochemical processes.

# Overview of the C-GEM Model

Below is a **complete overview** of how the **C-GEM** model is structured and how each primary function and file interacts. The model follows a standard pattern for **1D river/estuary** simulations: it initializes all data, runs hydrodynamics (flow and water depth), updates transport of chemical species, and then runs biogeochemical transformations.

## Main Execution Flow

Everything starts in **main.c**:

``` c
int main()
{
    // 1) Load parameters and configurations
    read_parameters("params.txt");
    Init();  // see init.c

    // 2) Time loop for simulation
    for (t = 0; t <= MAXT; t += DELTI)
    {
        // a) Solve hydrodynamics
        Hyd(t);

        // b) Update boundary conditions & lateral sources
        bgboundary(t);

        // c) Solve transport
        Transport(t);

        // d) (Optional) Solve biogeochemical reactions
        Biogeo(t);  // if enabled

        // e) Possibly write output
        // ...
    }

    // End
    return 0;
}
```

Thus, the **main** steps are: 1. **Initialization** – sets up arrays, reads boundary files, etc. 2. **Time-Loop** – for each time step: - **Hydrodynamics**: solve water levels and velocities. - **Boundary Conditions**: e.g., tidal forcing, upstream discharge, and all chemical boundary concentrations. - **Transport**: advect and disperse any scalar (nutrient, oxygen, etc.). - **Biogeochemistry**: apply reaction processes (optional, or integrated in certain runs).

## Initialization (init.c)

**init.c** organizes all reading and setup tasks:

1.  **readConfigFile("config.txt")**
    -   Locates input file paths (e.g., upstream boundary files, downstream boundary files, wind data, tributary configuration).
2.  **allocateBoundaryMemory()** and **readBoundaryData()**
    -   Allocates large arrays for boundary time-series: `ubDischarge`, `lbElevation`, etc.\
    -   Reads data from CSV or text files into these arrays.
3.  **readTributaryConfigFile("config.txt")** and **allocateTributaryMemory()**
    -   Reads how many tributaries, each name, cellIndex, and file paths for discharge and chemical data.\
    -   Allocates memory for each tributary’s time series (discharge, nutrients, etc.).
4.  **initializeHydrodynamics()**
    -   Reads or sets river geometry: `B[i]` (width), `slope[i]` (or bed profile).\
    -   Initializes arrays for depth `H[i]`, velocity `U[i]`, cross-section `D[i]`.
5.  **initializeTransportVariables()** and **initializeBiogeochemistry()**
    -   Sets up arrays for chemical concentrations `v[s].c[i]`.\
    -   Defines default or zero initial values for reaction terms.
6.  **assignBiogeochemicalRateConstants()**
    -   Assigns or reads from parameter files the rates for nitrification, denitrification, phyto growth, etc.

By the end of **Init()**, your model has loaded all **inputs** and **arrays** so it can run the main time-stepping loop.

## Hydrodynamics (hyd.c, tridaghyd.c, uphyd.c)

Within each time step, **Hyd(t)** is invoked to compute water depth and velocity. It proceeds as follows:

1.  **Newbc(t)** (in uphyd.c) – sets boundary values for downstream depth (`Tide(t)`) and upstream velocity from `Discharge(t)`.\
2.  **Iterative Solver**:
    -   **Coeffa(t)** (in tridaghyd.c) – constructs a tri-diagonal system representing the discretized Saint-Venant equations.\
    -   **Tridag()** (in tridaghyd.c) – solves that tri-diagonal system with the Thomas algorithm.\
    -   **Update()** (in uphyd.c) – updates water depth arrays (`H[i]`), cross-section (`D[i]`), velocity (`U[i]`).\
    -   **Check Convergence** – uses a function like `Conv(...)` to compare new vs. old solutions. If not converged, repeat.

If the solver hits too many iterations without converging, you get:

```         
❌ Convergence loop hit max iteration!
```

Otherwise, after **Hyd(t)** finishes, you have up-to-date water levels and velocities for all cells.

## Boundary Conditions & Biogeochemical Initialization (bcforcing.c)

Right after hydrodynamics, the model calls something like **bgboundary(t)**, which:

-   Interpolates boundary concentrations for each chemical species from arrays loaded at initialization (e.g., `ubO2`, `lbNO3`).\
-   Assigns these boundary concentrations at upstream or downstream cells.\
-   Potentially sets initial distributions across the domain (if it’s the first iteration or warm-up).\
-   Accounts for any **wind** data or other meteorological forcing.

Additionally, **Discharge(t, i)** in bcforcing.c is used by the hydrodynamic solver to incorporate tributary flows or upstream inflow at each cell index `i`.

## Transport (transport.c, uptransport.c)

Having updated velocities (`U[i]`) and cross-sections (`D[i]`), the model advects and disperses each chemical species:

1.  **Transport(t)** in **transport.c**:
    -   Loops over species `s` in the array `v[s]`.\
    -   Calls:
        1.  `Openbound(v[s].c, s)` – sets boundary concentrations (e.g., upstream inflow, downstream outflow).\
        2.  `TVD(v[s].c, s)` – does the advection step using a TVD scheme to prevent oscillations.\
        3.  `Disp(v[s].c)` – solves a tri-diagonal system for the dispersion term.\
        4.  If needed, writes results to output files.

Hence each species moves according to the flow and is mixed by dispersion.

## Biogeochemistry (bgboundary.c, biogeo.c)

Depending on your compilation flags or code settings, after transport the model can update:

1.  **bgboundary(t)** – used for boundary condition concentrations, but also sets certain “lateral boundary” or “initial distributions” for the chemical states.

2.  **Biogeo(t)** in **biogeo.c** – the main reaction solver:

    -   **applyDilution** for tributaries.\
    -   **computePrimaryProduction** (phytoplankton growth).\
    -   **computeBiogeochemicalReactions** (e.g., nitrification, denitrification, organic matter decay).\
    -   **computeCarbonateChemistry** (pH, CO₂, alkalinity).\
    -   **updateBiogeochemicalState** – merges all reaction source/sink terms into final concentrations for O₂, NO₃, NH₄, etc.

This step ensures **process-based** changes in chemistry occur after purely physical transport.

## Putting It All Together

Below is a **comprehensive flowchart** in text form, illustrating how the major functions and files of the C-GEM model connect and interact. This helps readers see at a glance which routines call each other and in what order, from **initialization** through **hydrodynamics**, **transport**, and **biogeochemical** updates.

```         
                                 ┌─────────────────────────────────────────┐
                                 │              main.c                   │
                                 │  1) read_parameters("params.txt")      │
                                 │  2) Init()   --> init.c               │
                                 │  3) for (t=0; t<=MAXT; t+=DELTI) {     │
                                 │      Hyd(t);        // hyd.c          │
                                 │      bgboundary(t); // bcforcing.c    │
                                 │      Transport(t);  // transport.c    │
                                 │      Biogeo(t);     // biogeo.c (opt) │
                                 │  }                                     │
                                 └─────────────────────────────────────────┘
                                              |
                                              v
┌──────────────────────────────────────────────────────────────────────────┐
│                          init.c  (Initialization)                       │
│                                                                          │
│  Init() {                                                                │
│     readConfigFile("config.txt");        // get file paths              │
│     allocateBoundaryMemory();            // prepare arrays              │
│     readBoundaryData();                  // read CSV time series        │
│     readTributaryConfigFile("config.txt");                               │
│     allocateTributaryMemory();                                          │
│                                                                          │
│     initializeHydrodynamics();           // sets B[i], slope[i], ...    │
│     initializeTransportVariables();                                     │
│     initializeBiogeochemistry();                                        │
│                                                                          │
│     assignBiogeochemicalRateConstants(); // load reaction rates         │
│                                                                          │
│     // Done. Model is ready.                                            │
│  }                                                                       │
└──────────────────────────────────────────────────────────────────────────┘

                                              |
                                              v
┌──────────────────────────────────────────────────────────────────────────┐
│                        Hyd(t)  (hyd.c)                                  │
│                                                                          │
│  Hyd(t) {                                                               │
│    Newbc(t);                 // uphyd.c -> sets tidal depth at mouth    │
│                                                                          │
│    iteration = 0;                                                      │
│    do {                                                                 │
│       Coeffa(t);           // tridaghyd.c -> build tri-diagonal matrix  │
│       Tridag();            // tridaghyd.c -> solve matrix w/ Thomas alg │
│       rsum = Conv(...);    // check H,U difference for convergence      │
│       Update();            // uphyd.c -> finalize H[i], U[i] updates    │
│       iteration++;                                                      │
│       if (iteration > max_its) {                                        │
│          // ❌ Convergence loop hit max iteration!                       │
│          break;                                                         │
│       }                                                                  │
│    } while (rsum != 2.0);                                               │
│                                                                          │
│    NewUH();    // uphyd.c -> finalize arrays post-solve                  │
│    Hydwrite(t); // optional, writes hydrodynamics output                │
│  }                                                                       │
└──────────────────────────────────────────────────────────────────────────┘

                                              |
                                              v
┌──────────────────────────────────────────────────────────────────────────┐
│                      bgboundary(t)  (bcforcing.c)                       │
│                                                                          │
│  bgboundary(t) {                                                        │
│    // For each chemical var (Phy1, Phy2, NO3, etc.):                    │
│    //   1) Interpolate upstream boundary data  (ubXTime, ubX )          │
│    //   2) Interpolate downstream boundary data (lbXTime, lbX )         │
│    //   3) Assign v[var].cub, v[var].clb                                 │
│    //   4) Possibly fill initial distribution across domain.            │
│                                                                          │
│    // Also handles tributary concentrations, wind forcing, etc.         │
│  }                                                                       │
└──────────────────────────────────────────────────────────────────────────┘

                                              |
                                              v
┌──────────────────────────────────────────────────────────────────────────┐
│                       Transport(t)  (transport.c)                       │
│                                                                          │
│  Transport(t) {                                                         │
│    for (s = 0; s < MAXV; s++) { // For each chemical species            │
│       Openbound(v[s].c, s);        // uptransport.c                     │
│       TVD(v[s].c, s);             // uptransport.c (advection)          │
│       Disp(v[s].c);               // uptransport.c (dispersion)         │
│                                                                          │
│       Boundflux(s); // optional flux calculations                       │
│       if (time to write?) Transwrite(...);                              │
│    }                                                                     │
│  }                                                                       │
└──────────────────────────────────────────────────────────────────────────┘

                                              |
                                              v
┌──────────────────────────────────────────────────────────────────────────┐
│                        Biogeo(t)  (biogeo.c)                             │
│                                                                          │
│  Biogeo(t) {                                                             │
│    applyDilution(t); // tributary mixing into main channel               │
│                                                                          │
│    for (i=0; i<=M; i++) {                                               │
│       computeHydrodynamicFluxes(t, i);  // gas exchange, shear, etc.    │
│       computePrimaryProduction(t, i);   // phytoplankton growth, light   │
│       computeSedimentFluxes(t, i);      // erosion/deposition of SPM     │
│       computeBiogeochemicalReactions(t, i); // nitrification, O2 use, etc│
│       computeCarbonateChemistry(t, i);  // pH, CO2 speciation, alkal.    │
│       updateBiogeochemicalState(t, i);  // finalize changes in each var  │
│    }                                                                     │
│                                                                          │
│    // Possibly write reaction rates, fluxes, or debug info               │
│  }                                                                       │
└──────────────────────────────────────────────────────────────────────────┘
```

## Study Questions

1.  Why is a 1D approach appropriate for many estuarine systems?
2.  What are the key assumptions in the C-GEM model and when might they break down?
3.  How do the three main modules (hydrodynamics, transport, biogeochemistry) interact?
4.  What role does time-stepping play in numerical stability?

## Practical Example: Setting Up a Simple Case

Consider modeling a 50km tidal river with: - Upstream flow: 100 m³/s - Tidal range: 2m - Single nutrient (NO₃) input

Key steps: 1. Define geometry (width, depth) 2. Set boundary conditions 3. Choose time step 4. Configure output variables

## Additional References

-   Volta et al. (2016). C-GEM (v 1.0): a new, cost-efficient biogeochemical model for estuaries. *Geosci. Model Dev.*, 9, 1271-1295.
-   MacCready, P., & Geyer, W. R. (2010). Estuarine physics and their influence on biogeochemistry. *Treatise on Estuarine and Coastal Science*, 2, 19-49.

## References

-   Fischer, H. B., List, E. J., Koh, R. C. Y., Imberger, J., & Brooks, N. H. (1979). *Mixing in inland and coastal waters*. Academic Press.
-   USACE (U.S. Army Corps of Engineers) (2002). *EM 1110-2-1416: River Hydraulics*.