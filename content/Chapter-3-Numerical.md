---
jupyter: python3
---

# Numerical Solution of the Hydrodynamic Equations

## Learning Objectives
After completing this chapter, you will be able to:
- Understand the finite difference discretization of Saint-Venant equations
- Implement semi-implicit numerical schemes for hydrodynamic modeling
- Apply appropriate boundary conditions numerically
- Identify and resolve numerical stability issues

## Theoretical Background

### Finite Difference Approximation
Starting from the continuous Saint-Venant equations:

$$
\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = 0
$$

We apply finite differences in space and time:

$$
\frac{A_i^{n+1} - A_i^n}{\Delta t}
\;+\;
\frac{Q_{i+1}^n - Q_{i-1}^n}{2\,\Delta x}
= 0
$$

where superscript n denotes time level and subscript i denotes spatial location.

### Semi-Implicit Scheme
To ensure stability while maintaining efficiency, C-GEM uses a semi-implicit approach where:
- Some terms are treated implicitly (future time level)
- Others are treated explicitly (current time level)


To provide a **comprehensive animation suite** that helps visualize how your **hydrodynamic model** solves the **Saint-Venant equations** numerically, I'll include **multiple animations** covering:
1. **Finite Difference Discretization** of the continuity and momentum equations.
2. **Tri-diagonal Solver (Thomas Algorithm)** to visualize how the linear system is solved step by step.
3. **Semi-Implicit Scheme Convergence** to show how iterations stabilize.
4. **Tidal Variation Influence** at the downstream boundary.
5. **Velocity and Water Depth Evolution** over time with an interactive player.

---

### **1️⃣ Animation: Finite Difference Discretization**
This animation will **illustrate how numerical discretization** works for the **continuity equation**:

$$
\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = 0
$$

and the **momentum equation**:

$$
\frac{\partial Q}{\partial t} + \frac{\partial}{\partial x} \left( \frac{Q^2}{A} \right) + gA \frac{\partial h}{\partial x} + gA S_f = 0
$$

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define a small spatial grid
nx = 10
dx = 1
dt = 0.1
g = 9.81  # Gravity

# Initial conditions
H = np.ones(nx) * 2.0  # Water depth (m)
Q = np.zeros(nx)       # Discharge (m^3/s)
U = np.zeros(nx)       # Velocity (m/s)

fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(0, nx * dx, nx)
bar = ax.bar(x, H, color='blue', alpha=0.7)

def update(n):
    global H, Q, U
    
    H_new = H.copy()
    Q_new = Q.copy()
    
    for i in range(1, nx - 1):
        # Finite difference form of continuity equation
        H_new[i] = H[i] - dt / (2 * dx) * (Q[i+1] - Q[i-1])

        # Finite difference form of momentum equation
        Q_new[i] = Q[i] - dt / (2 * dx) * (g * (H[i+1] - H[i-1]))

    # Update fields
    H[:] = H_new
    Q[:] = Q_new
    for rect, h in zip(bar, H):
        rect.set_height(h)
    
    return bar,

ani1 = animation.FuncAnimation(fig, update, frames=50, interval=100)
plt.title("Finite Difference Discretization of Continuity Equation")
plt.show()
```

✅ **What This Shows:**  
✔ How **depth and discharge evolve over time** due to numerical approximation.  
✔ How **finite difference discretization** updates cell values step by step.


### **2️⃣ Animation: Tri-diagonal Solver (Thomas Algorithm)**
Since your model uses a **tri-diagonal matrix system**, this animation will **illustrate step-by-step how the solver works**.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of grid points
N = 10
x = np.arange(N)
A = np.zeros((N, N))  # Tri-diagonal matrix
rhs = np.random.rand(N)  # Random right-hand side
solution = np.zeros(N)  # Solution array

# Construct a tri-diagonal matrix
for i in range(N):
    A[i, i] = 4  # Main diagonal
    if i > 0:
        A[i, i - 1] = -1  # Lower diagonal
    if i < N - 1:
        A[i, i + 1] = -1  # Upper diagonal

fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(A, cmap="coolwarm", vmin=-1, vmax=4)

def update(n):
    global A
    if n < N:
        A[n, n] = 1  # Simulating elimination step
    im.set_data(A)
    return im,

ani2 = animation.FuncAnimation(fig, update, frames=N, interval=500)
plt.title("Step-by-Step Visualization of the Thomas Algorithm")
plt.show()
```

✅ **What This Shows:**  
✔ **Forward elimination** step in the **Thomas algorithm**.  
✔ **Matrix transformation** during solving.


### **3️⃣ Animation: Semi-Implicit Scheme Convergence**
Your **semi-implicit scheme** iterates until the solution **converges**. This animation will **track convergence** using a tolerance measure.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Iterative method convergence example
iterations = 50
tolerance = 1e-3
errors = np.exp(-np.linspace(0, 5, iterations))  # Simulated decreasing error

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, iterations)
ax.set_ylim(0, 1)
ax.set_xlabel("Iterations")
ax.set_ylabel("Convergence Error")
ax.set_title("Convergence of Semi-Implicit Scheme")

line, = ax.plot([], [], 'r-', lw=2)

def update(n):
    line.set_data(np.arange(n), errors[:n])
    return line,

ani3 = animation.FuncAnimation(fig, update, frames=iterations, interval=100)
plt.show()
```

✅ **What This Shows:**  
✔ How **error reduces over iterations**.  
✔ **Convergence behavior** of the numerical solver.


### **4️⃣ Animation: Velocity and Water Depth Evolution**
This combines **tidal variation**, **wave propagation**, and **velocity arrows**.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Simulation parameters
L = 1000
dx = 20
dt = 0.5
nx = int(L / dx)
nt = 200
g = 9.81

# Initialize fields
H = np.ones(nx) * 2.0
Q = np.zeros(nx)
U = np.zeros(nx)

# Tidal boundary condition
tide_amplitude = 0.5
tide_period = 12 * 3600
tide_omega = 2 * np.pi / tide_period

# Figure setup
fig, ax = plt.subplots(2, 1, figsize=(8, 8))
x = np.linspace(0, L, nx)
line_H, = ax[0].plot(x, H, 'b-', lw=2)
line_U, = ax[1].plot(x, U, 'r-', lw=2)
quiver_U = ax[1].quiver(x, np.zeros(nx), U, np.zeros(nx), scale=10)

ax[0].set_ylabel("Water Depth H (m)")
ax[1].set_ylabel("Velocity U (m/s)")
ax[1].set_xlabel("Distance (m)")

def update(n):
    global H, Q, U
    H_new = H.copy()
    Q_new = Q.copy()

    # Apply tidal forcing at downstream
    H[-1] = 2.0 + tide_amplitude * np.sin(tide_omega * n * dt)

    for i in range(1, nx - 1):
        H_new[i] = H[i] - dt / (2 * dx) * (Q[i+1] - Q[i-1])
        Q_new[i] = Q[i] - dt / (2 * dx) * (g * (H[i+1] - H[i-1]))

    H[:] = H_new
    Q[:] = Q_new
    U[:] = Q / H

    line_H.set_ydata(H)
    line_U.set_ydata(U)
    quiver_U.set_UVC(U, np.zeros(nx))
    
    return line_H, line_U, quiver_U

ani4 = animation.FuncAnimation(fig, update, frames=nt, interval=50, blit=True)
plt.show()
```


## Numerical Implementation

### Grid Structure

**Numerical Method for Hydrodynamics**

In your tidal river model, after specifying the **Saint-Venant equations** (continuity and momentum), you must discretize and solve them at each time step in a manner suitable for **1D open-channel flow**. This section describes how the code constructs and solves a **tri-diagonal linear system** that updates water depth $H$ and velocity (or discharge) $U$ in time, as well as how friction and storage are included.

### Implementation Overview

Key routines and files:

1.  **Coeffa(t)** in **tridaghyd.c**:

    *   Builds the coefficients of the tri-diagonal matrix (sub-, main-, super-diagonal) for each cell $j$.
    *   Incorporates physical parameters: time step (\(\text{DELTI}\)), friction coefficients, geometry, etc.

2.  **Tridag()** in **tridaghyd.c**:

    *   Solves the tri-diagonal system using the **Thomas algorithm** (a classic method for tri-diagonal matrices).

3.  **Hyd(t)** in **hyd.c**:

    *   The main driver for hydrodynamics each time step.
    *   Repeatedly calls `Coeffa()` and `Tridag()`, checking for convergence.
    *   Applies boundary conditions (`Newbc(t)`), updates arrays, and writes output (if needed).

Conceptually, each iteration tries to solve for $\Delta H$ and $\Delta U$ from the discretized system. If the solution does not converge within a set number of iterations (e.g., 10,000), you see a message:
```
❌ Convergence loop hit max iteration!
```
This indicates a failure to converge—often due to input data issues, dry cells, or large time steps.

## Semi-Implicit Scheme Derivation

Because **both** water depth and velocity are updated at once, and because the momentum equation is non-linear (it includes terms like $U |U|$, friction, and free-surface slope), the code uses a **semi-implicit** or partially linearized approach:

1.  **Linearization**:

    *   Certain terms (like friction or advection) are linearized or approximated with previous-iteration values.
    *   This yields a system $\mathbf{A}(\mathbf{x}^{n}) \,\Delta\mathbf{x} = \mathbf{b}(\mathbf{x}^{n})$, where $\mathbf{x}^n$ is the solution from the previous iteration.

2.  **Tri-Diagonal Structure**:

    *   By only relating cell $j$ to neighbors $j-1$ and $j+1$, the coefficient matrix remains tri-diagonal. This is computationally efficient ($\mathcal{O}(N)$ complexity).

3.  **Convergence Criterion**:

    *   After solving, the model checks some measure of the change in water depth and velocity, for example:
        $$
        \text{Conv}(H) = \frac{ \sum_i |H_i^{\text{(new)}} - H_i^{\text{(old)}}| }{ \sum_i |H_i^{\text{(old)}}| }
        $$
        or a simpler absolute difference. If $\text{Conv}(H) + \text{Conv}(U) \le \text{TOL}$, the iteration stops.

4.  **Iteration Limit**:

    *   A loop can run up to a large number (e.g., 10,000) to ensure numerical stability. If it never converges, you get the “hit max iteration” error (see **hyd.c**).

**References**:

*   Cunge, J. A., Holly, F. M., & Verwey, A. (1980). *Practical aspects of computational river hydraulics*. Pitman, London.
*   Abbott, M. B., & Ionescu, F. (1967). On the numerical computation of nearly horizontal flows. *Journal of Hydraulic Research*, 5(2), 97–117.

## Practical Notes & Code Details

### The Tri-Diagonal System (Coeffa & Tridag)

**Tridag** stands for “Tri-Diagonal.” The discretized forms of the Saint-Venant equations at cell $j$ connect $(j-1)$, $j$, and $(j+1)$. Consequently, each row $j$ in the matrix has:

*   `C[j][1]` (sub-diagonal) → coefficient for unknown at $(j-1)$.
*   `C[j][2]` (main diagonal) → coefficient for unknown at $j$.
*   `C[j][3]` (super-diagonal) → coefficient for unknown at $(j+1)$.
*   `Z[j]` → the right-hand side (RHS), including known terms or boundary contributions.

When **Coeffa(t)** is called, it computes these arrays for every $j$. Then:

```c
Tridag();  // solves C * x = Z
```

*   **Thomas Algorithm** Steps:

    1.  **Forward elimination**: modifies the sub- and main-diagonal to produce a simpler system with only one unknown in each row.
    2.  **Pivot** (`bet`): if `bet == 0`, the system is singular → “❌ Error: bet is zero at j=…”.
    3.  **Back-substitution**: recovers the solution array (e.g., $\Delta H, $\Delta U$).

If everything is stable (non-dry cells, valid friction, etc.), it converges quickly. Otherwise, you may see singularities or blow-ups.

### Friction, Storage Ratio, and Other Terms

1.  **Chezy Friction**:

    $
    f \;=\; \frac{1}{C^2},
    $
    where $C$ is the Chezy coefficient. The friction force in the momentum equation is typically proportional to $ f \cdot |U| U $.

    *   In the code, you see:

    ```c
    FRIC[i] = 1.0 / (Chezy[i] * Chezy[i]);
    ```

    *   That friction is inserted into the matrix in `Coeffa()` to damp velocity changes.

2.  **Storage Ratio** $\mathrm{Rs}$:

    *   Some channels have lateral storage or floodplains, effectively increasing volume for a given water level.
    *   The code parameterizes this with `rs_val * H[j] / DELTI` in the diagonal terms. This can be interpreted as adding extra volume at node $j$.

3.  **Time Step** $\Delta t$ (DELTI):

    *   The hydrodynamic equations are advanced in increments of $\Delta t$.
    *   A large time step can cause instability or slow convergence, since you are solving a strongly non-linear system.

**References** (Friction & Implementation):

*   M. B. Abbott (1979). *Computational Hydraulics: Elements of the Theory of Free Surface Flows*.
*   M. Bruneau and R. Egashira (1996). Analytical and numerical solutions of the shallow-water equations with bottom friction. *Journal of Hydraulic Engineering*, 122(1), 25–31.

### Summary of Hydrodynamic Solver Flow

1.  **Newbc(t)**: Impose boundary conditions (tide downstream, discharge upstream).
2.  **Coeffa(t)**:

    *   Build tri-diagonal arrays `C` (sub-, main-, super-diagonal) based on continuity & momentum.
    *   Incorporate friction, geometry, storage ratio, previous iteration’s velocity/depth, etc.
    *   Fill the RHS vector `Z`.

3.  **Tridag()**:

    *   Solve $ C \times \mathbf{x} = Z $ for increments in depth/velocity.
    *   If the pivot (`bet`) becomes zero, the system is singular → error.

4.  **Update & Convergence**:

    *   Update $(H, U)$ or $(H, Q)$.
    *   Check difference between old and new solutions. If below tolerance, exit the iteration. Otherwise, keep looping.

When this procedure completes successfully each time step, the model has new hydrodynamic fields $\{H[i]\}, \{U[i]\}$ that then feed into the **transport** and **biogeochemical** calculations.

## Detailed Code Explanation

### Coeffa(t) Function

The `Coeffa(t)` function constructs the tri-diagonal matrix coefficients for the Saint-Venant equations. Here is a detailed breakdown of the function:

```c
void Coeffa(int t) {
    int j;
    double dt = DELTI;
    double dx = DELXI;

    for (j = 1; j <= M; j++) {
        // Compute coefficients for the continuity equation
        C[j][1] = -dt / (2.0 * dx);
        C[j][2] = 1.0;
        C[j][3] = dt / (2.0 * dx);
        Z[j] = A[j] - A[j-1];

        // Compute coefficients for the momentum equation
        double Uj = U[j];
        double Hj = H[j];
        double Aj = A[j];
        double Fric = FRIC[j];

        C[j][1] += -dt * Uj / (2.0 * dx);
        C[j][2] += dt * (g * Hj + Fric * fabs(Uj));
        C[j][3] += dt * Uj / (2.0 * dx);
        Z[j] += dt * (g * Hj * S[j] - Fric * Uj * fabs(Uj));
    }
}
```

### Explanation of Coeffa(t) Function

1. **Continuity Equation Coefficients**:
   - The continuity equation $\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = 0$ is discretized using finite differences.
   - The coefficients for the tri-diagonal matrix are computed as:
     $
     C[j][1] = -\frac{\Delta t}{2 \Delta x}, \quad C[j][2] = 1.0, \quad C[j][3] = \frac{\Delta t}{2 \Delta x}
     $
   - The right-hand side (RHS) vector $Z[j]$ is initialized with the difference in cross-sectional area $A$ between adjacent cells.

2. **Momentum Equation Coefficients**:
   - The momentum equation $\frac{\partial Q}{\partial t} + \frac{\partial}{\partial x} \left( \frac{Q^2}{A} \right) + gA \frac{\partial h}{\partial x} + gA S_f = 0$ is discretized.
   - The coefficients for the tri-diagonal matrix are updated to include terms for velocity $U$, water depth $H$, cross-sectional area $A$, and friction $Fric$.
   - The RHS vector $Z[j]$ is updated to include terms for gravitational acceleration $g$, water depth $H$, and friction $Fric$.

### Tridag() Function

The `Tridag()` function solves the tri-diagonal system using the Thomas algorithm. Here is a detailed breakdown of the function:

```c
void Tridag() {
    int j;
    double bet;
    double gam[MAXM];

    // Forward elimination
    bet = C[1][2];
    if (bet == 0.0) {
        printf("❌ Error: bet is zero at j=1\n");
        exit(EXIT_FAILURE);
    }
    Z[1] /= bet;
    for (j = 2; j <= M; j++) {
        gam[j] = C[j][1] / bet;
        bet = C[j][2] - C[j][1] * gam[j];
        if (bet == 0.0) {
            printf("❌ Error: bet is zero at j=%d\n", j);
            exit(EXIT_FAILURE);
        }
        Z[j] = (Z[j] - C[j][1] * Z[j-1]) / bet;
    }

    // Back-substitution
    for (j = M-1; j >= 1; j--) {
        Z[j] -= gam[j+1] * Z[j+1];
    }
}
```

### Explanation of Tridag() Function

1. **Forward Elimination**:
   - The forward elimination step modifies the sub-diagonal and main diagonal coefficients to produce a simpler system with only one unknown in each row.
   - The pivot (`bet`) is checked to ensure it is non-zero to avoid a singular system.
   - The RHS vector $Z$ is updated by dividing by the pivot and subtracting the product of the sub-diagonal coefficient and the previous RHS value.

2. **Back-Substitution**:
   - The back-substitution step recovers the solution array by iterating from the last row to the first row.
   - The RHS vector $Z$ is updated by subtracting the product of the super-diagonal coefficient and the next RHS value.

### Newbc(t) Function

The `Newbc(t)` function sets the boundary conditions for the hydrodynamic model. Here is a detailed breakdown of the function:

```c
void Newbc(int t) {
    if (M <= 0) {
        printf("❌ Error: M is not initialized properly!\n");
        exit(EXIT_FAILURE);
    }

    H[1] = B[1] * Tide(t);
    TH[1] = H[1];
    D[1] = H[1] + ZZ[1];

    if (B[1] == 0) {
        printf("❌ Error: B[1] is zero! Check initialization.\n");
        exit(EXIT_FAILURE);
    }

    if (D[1] == 0) { // total cross-sectional area at the first grid
        printf("❌ Error: D[1] is zero! Check initialization.\n");
        
        // Add a small value to D[1] to prevent division by zero
        D[1] = 0.0001;  // A small, non-zero value
        printf("⚠️ Warning: D[1] was zero, set to 0.0001 to avoid division by zero.\n");
    }

    // Set upstream boundary condition for discharge
    U[M] = Discharge(t, M) / D[M];
}
```

### Explanation of Newbc(t) Function

1. **Downstream Boundary Condition**:
   - The downstream boundary condition is set by interpolating the tidal elevation using the `Tide(t)` function.
   - The water depth $H[1]$ and total cross-sectional area $D[1]$ are updated accordingly.

2. **Upstream Boundary Condition**:
   - The upstream boundary condition is set by interpolating the discharge using the `Discharge(t, M)` function.
   - The velocity $U[M]$ is updated by dividing the discharge by the total cross-sectional area $D[M]$.

### Update Function

The `Update()` function updates the hydrodynamic variables after solving the tri-diagonal system. Here is a detailed breakdown of the function:

```c
void Update() {
    int j;
    for (j = 1; j <= M; j++) {
        H[j] += Z[j];
        U[j] += Z[j];
        D[j] = H[j] + ZZ[j];
    }
}
```

### Explanation of Update Function

1. **Update Hydrodynamic Variables**:
   - The water depth $H[j]$, velocity $U[j]$, and total cross-sectional area $D[j]$ are updated using the solution array $Z[j]$ obtained from the tri-diagonal solver.

### Conv Function

The `Conv()` function checks the convergence of the hydrodynamic solution. Here is a detailed breakdown of the function:

```c
double Conv() {
    int j;
    double rsum = 0.0;
    for (j = 1; j <= M; j++) {
        rsum += fabs(H[j] - TH[j]) + fabs(U[j] - TU[j]);
    }
    return rsum;
}
```

