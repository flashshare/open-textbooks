# Hydrodynamic Theory in Tidal Rivers

## Learning Objectives

After completing this chapter, you will be able to: - Understand the derivation and limitations of the Saint-Venant equations - Identify when 1D assumptions are valid or break down - Apply appropriate boundary conditions for tidal systems - Recognize potential numerical instabilities

## Theoretical Background

### From 3D to 1D: The Saint-Venant Approximation

Starting from the full 3D Navier-Stokes equations, we make several key assumptions: 1. Hydrostatic pressure distribution 2. Small vertical accelerations 3. Cross-sectionally averaged velocities 4. Well-mixed conditions

These lead to the 1D Saint-Venant equations:

### Continuity Equation

The continuity equation expresses the conservation of mass:

$$ \frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = 0 $$

where:

-   $A$ is the cross-sectional area of the flow (m²).
-   $Q$ is the discharge (m³/s).
-   $t$ is time (s).
-   $x$ is the distance along the channel (m).

### Momentum Equation

The momentum equation expresses the conservation of momentum:

$$ \frac{\partial Q}{\partial t} + \frac{\partial}{\partial x} \left( \frac{Q^2}{A} \right) + gA \frac{\partial h}{\partial x} + gA S_f = 0 $$

where:

-   $g$ is the acceleration due to gravity (m/s²).
-   $h$ is the water depth (m).
-   $S_f$ is the friction slope (dimensionless).

### Limitations of the 1D Approach

The model may NOT perform well when: - Strong vertical stratification exists - Significant lateral circulation occurs - Complex bathymetry creates 3D flow patterns - Sharp bends cause secondary flows

## Current Model Formulation

### Continuity (Mass Conservation)

In one spatial dimension, let: - (A(x, t)) = cross-sectional area at location (x) and time (t). - (Q(x, t) = U(x, t) \times A(x, t)) = volumetric discharge, where (U) is the mean velocity in the cross-section.

The **continuity equation** for an incompressible fluid (water) in open-channel flow is:

$$ \frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = 0. \tag{1} $$

-   The first term (\partial A / \partial t) accounts for changes in water cross-sectional area with time (i.e., the rise or fall of water level).
-   The second term (\partial Q / \partial x) is the net inflow/outflow rate along the channel ((x)-direction).

This equation essentially states that **the rate of change of water volume in a slice of the river** (which depends on (A)) must be balanced by the **net flow of water into or out of that slice** ((\partial Q / \partial x)).

In your code, (A) often appears as: $$ A_i = B_i \times H_i $$ if assuming a rectangular channel of width (B_i) and depth (H_i). For more complex cross-sections, (A_i) can be determined from geometry files (e.g., your slope/bathymetry or storage ratio factors).

### Momentum (Force Balance)

The second **Saint-Venant** equation enforces conservation of momentum in the flow. In differential form, it is commonly written as:

$$ \frac{\partial Q}{\partial t} + \frac{\partial}{\partial x} \Bigl(\frac{Q^2}{A}\Bigr) + gA\frac{\partial h}{\partial x} = -\text{(friction \& other source terms)} \tag{2} $$

where: - (h(x,t)) = water depth, - (g) = gravitational acceleration (9.81 m/s(\^2) in SI units), - (\frac{Q^2}{A}) arises from convective acceleration, - (gA\frac{\partial h}{\partial x}) accounts for the hydrostatic pressure gradient (slope of the free surface).

**Friction** can be modeled in various ways—your code uses the **Chezy** formulation (some references use Manning’s (n) or Darcy–Weisbach friction). A typical Chezy-based friction term is of the form:

$$ \tau_{\text{fric}} = f \cdot Q \,\|Q\| \,/\, A, \quad \text{where} \quad f = \frac{1}{C^2}, $$

and (C) is the Chezy coefficient. In the code, you often see something like:

$$ \text{FRIC}[i] = \frac{1}{(\text{Chezy}[i])^2} $$

applied to the momentum equation.

Thus, the 1D momentum equation in your model tracks how discharge (Q) (or velocity (U)) evolves over time and space, balancing inertial (acceleration), gravitational (slope), and frictional forces.

### Practical Example: Tidal Wave Propagation

Here is an **Python animation** that includes **velocity illustration** and a **semi-diurnal tidal boundary condition** at the downstream. This improved visualization now:
- Shows **water depth \( H(x,t) \) evolution**.
- Illustrates **velocity \( U = Q/A \)** with arrows.
- Applies a **semi-diurnal tide** at the **downstream boundary**.

✔ **Velocity field \( U = Q/A \) displayed with arrows.**  
✔ **Semi-diurnal tidal forcing** at **downstream boundary** using a sinusoidal function.  
✔ **More realistic hydrodynamics visualization** for **Saint-Venant equations**.

**Python Animation Code**

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
L = 1000  # Channel length (meters)
dx = 10   # Spatial step
dt = 0.5  # Time step
g = 9.81  # Gravity acceleration (m/s^2)
nx = int(L / dx)  # Number of spatial points
nt = 400  # Number of time steps

# Initialize variables
H = np.ones(nx) * 2.0  # Initial water depth (meters)
Q = np.zeros(nx)       # Initial discharge (m^3/s)
U = np.zeros(nx)       # Initial velocity (m/s)

# Initial perturbation (wave) at center
H[nx//2] += 1.0

# Boundary conditions
Q[0] = 5.0  # Constant discharge at upstream
tide_amplitude = 0.5  # Tidal variation in meters
tide_period = 12 * 3600  # Semi-diurnal tide period in seconds
tide_omega = 2 * np.pi / tide_period

# Set up figure for animation
fig, ax = plt.subplots(2, 1, figsize=(8, 8))
ax[0].set_xlim(0, L)
ax[0].set_ylim(1, 4)
ax[1].set_xlim(0, L)
ax[1].set_ylim(-1, 2)

line_H, = ax[0].plot(np.linspace(0, L, nx), H, 'b-', lw=2)
line_U, = ax[1].plot(np.linspace(0, L, nx), U, 'r-', lw=2)
quiver_U = ax[1].quiver(np.linspace(0, L, nx), np.zeros(nx), U, np.zeros(nx), scale=10)

ax[0].set_ylabel("Water Depth H (m)")
ax[0].set_title("Saint-Venant Equations: Water Depth & Velocity Evolution")

ax[1].set_ylabel("Velocity U (m/s)")
ax[1].set_xlabel("Distance (m)")

# Update function for animation
def update(n):
    global H, Q, U

    H_new = H.copy()
    Q_new = Q.copy()
    
    # Apply tidal forcing at downstream boundary
    H[-1] = 2.0 + tide_amplitude * np.sin(tide_omega * n * dt)

    for i in range(1, nx - 1):
        # Continuity equation (finite difference)
        H_new[i] = H[i] - dt / (2 * dx) * (Q[i+1] - Q[i-1])

        # Momentum equation (finite difference)
        Q_new[i] = Q[i] - dt / (2 * dx) * (g * (H[i+1] - H[i-1]))

    # Update values
    H[:] = H_new
    Q[:] = Q_new

    # Compute velocity (U = Q / A)
    U[:] = Q / H

# Animation function
def animate(n):
    update(n)
    line_H.set_ydata(H)
    line_U.set_ydata(U)
    quiver_U.set_UVC(U, np.zeros(nx))
    return line_H, line_U, quiver_U

ani = animation.FuncAnimation(fig, animate, frames=nt, interval=50, blit=True)

plt.show()
```

**Key Features in this Animation**
1. **Tidal forcing at downstream:**  
   - Semi-diurnal tide modeled with **\( H_{down} = H_0 + A \sin(\omega t) \)**
   - Mimics **ocean tides influencing estuarine hydrodynamics**.

2. **Velocity Visualization:**  
   - **Red line:** Instantaneous velocity \( U(x,t) \).  
   - **Arrows:** Velocity field using `quiver` (magnitude and direction).  

3. **Water Depth Evolution:**  
   - **Blue line:** Propagation of **wavefronts** along the channel.

✔ **Wave propagation and backflow due to tides**  
✔ **Velocity \( U(x,t) \) changes due to depth variations**  
✔ **Effects of finite difference discretization of Saint-Venant equations**  


## Code Implementation Details

### Boundary Conditions for a Tidal River

#### Downstream Boundary (Tidal Elevation)

In a tidal river, the **downstream boundary** is typically the mouth, where the water surface elevation (\eta(t)) changes with ocean or tidal fluctuations. In your code:

-   **File**: `bcforcing.c`\
-   **Function**: `double Tide(int t)` or direct array `lbElevation[nhour]`

If the user provides a time series of tidal elevations (\eta(t)) in `lbElevationFile`, the code interpolates them each time step:

``` c
H[1] = B[1] * Tide(t);
```

or sometimes:

``` c
H[1] = Tide(t);
```

depending on whether you multiply by channel width. This sets the water depth (or free surface) at the mouth, forcing the rest of the domain.

#### Upstream Boundary (Discharge)

At the **upstream** end, the model imposes a known volumetric flow rate (discharge (Q)):

-   **Function**: `double Discharge_ups(int t)`
-   **File**: `bcforcing.c`

This typically reads a measured time series from `ubDischargeFile` (e.g., cubic meters per second), then the model applies:

``` c
U[M] = Discharge(t, M) / D[M];
```

where `M` is the upstream-most cell index. (Sometimes you see `Discharge_ups(t)` used to set negative or positive flows, depending on sign conventions in the code.)

#### Tributaries

Intermediate inflows can enter the main channel from side rivers or canals. Your code reads each **tributary** from `config.txt`, including:

-   **cellIndex**: where the tributary enters,
-   **dischargeFile**: the Q(t) time series.

The function `Discharge(t, i)` in `bcforcing.c` sums all relevant tributary flows if the cell index is downstream of (i). That way, each cross-section’s net flow includes upstream discharge plus or minus any lateral inflows.

**In summary**:\ 1. The 1D **Saint-Venant** equations (continuity + momentum) track water depth and discharge along the river.\ 2. **Boundary forcing** at the downstream end imposes tidal elevations, while the upstream end imposes a known inflow.\ 3. **Tributaries** add or remove water at specified internal cells.

This forms the backbone of your tidal river hydrodynamics model. By solving these equations, the code predicts the water level and velocity distribution that subsequently drives transport of nutrients, sediments, and other constituents.

## Differences and Strengths of C-GEM Compared to Other 1D Models

### Key Strengths

-   **Coupled Biogeochemical Processes**: Unlike many 1D models, C-GEM integrates detailed biogeochemical processes, allowing for comprehensive water quality assessments.
-   **Semi-Implicit Scheme**: The semi-implicit numerical scheme enhances stability and efficiency, particularly for tidal systems with rapid changes.
-   **Modular Structure**: The modular design facilitates customization and extension, making it adaptable to various estuarine and riverine environments.

### Unique Features

-   **Advanced Boundary Handling**: C-GEM's boundary condition handling, including tidal forcing and tributary inputs, is more sophisticated than many traditional 1D models.
-   **Detailed Reaction Networks**: The model includes detailed reaction networks for nutrient cycling, primary production, and organic matter degradation, providing a more accurate representation of biogeochemical dynamics.

### Limitations and Considerations

-   **1D Assumptions**: The model assumes well-mixed conditions vertically and laterally, which may not be valid in all systems.
-   **Simplified Geometry**: Complex bathymetry and lateral variations are not fully captured.
-   **Numerical Stability**: Care must be taken with time step selection and boundary condition implementation to avoid numerical instabilities.

### Practical Considerations

-   **Data Requirements**: Accurate boundary and initial condition data are crucial for reliable model predictions.
-   **Calibration and Validation**: Regular calibration and validation against observed data are necessary to ensure model accuracy.
-   **Sensitivity Analysis**: Conducting sensitivity analyses helps identify key parameters and reduce uncertainty.

## Summary

The C-GEM model offers a robust framework for simulating hydrodynamics and biogeochemical processes in tidal rivers and estuaries. By leveraging the strengths of the Saint-Venant equations and integrating advanced biogeochemical modules, C-GEM provides a comprehensive tool for water quality assessment and management.

## Study Questions

1.  What are the key assumptions underlying the Saint-Venant equations, and when might they break down?
2.  How does the C-GEM model handle boundary conditions differently from other 1D models?
3.  What are the advantages of using a semi-implicit numerical scheme in the C-GEM model?
4.  How can you ensure numerical stability when running the C-GEM model?

## References

-   Cunge, J. A., Holly, F. M., & Verwey, A. (1980). *Practical aspects of computational river hydraulics*. Pitman, London.
-   Abbott, M. B., & Ionescu, F. (1967). On the numerical computation of nearly horizontal flows. *Journal of Hydraulic Research*, 5(2), 97–117.
-   Fischer, H. B., List, E. J., Koh, R. C. Y., Imberger, J., & Brooks, N. H. (1979). *Mixing in inland and coastal waters*. Academic Press.
-   USACE (U.S. Army Corps of Engineers) (2002). *EM 1110-2-1416: River Hydraulics*.