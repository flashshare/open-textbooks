# Model Implementation and Configuration

## Learning Objectives

After completing this chapter, you will be able to:

-   Set up a C-GEM model run
-   Configure key model parameters
-   Calibrate and validate the model
-   Analyze model output data

## Model Setup and Workflow

The C-GEM model simulates hydrodynamics, transport, and biogeochemical processes in tidal rivers and estuaries. Setting up a model run involves several key steps:

1.  **Configuration:** Defining the model domain, boundary conditions, and process parameters.
2.  **Initialization:** Loading data and setting initial conditions.
3.  **Execution:** Running the simulation.
4.  **Analysis:** Interpreting and visualizing the model outputs.

## Configuration Files

The C-GEM model is configured using a set of parameters and configuration files. These files specify the model domain, boundary conditions, and process parameters.

### config.txt

The `config.txt` file is the primary configuration file for the C-GEM model. It specifies the paths to the input data files, the number of grid cells, the simulation time step, and other model parameters.

Key parameters in `config.txt` include:

-   **File Paths:** Paths to boundary condition files (upstream discharge, downstream tidal elevation, tributary inflows), geometry file, and other input data files.
-   **Model Domain:** Number of grid cells (`M`), domain length (`L`), and cell size (`DELXI`).
-   **Time Step:** Simulation time step (`DELTI`) and total simulation time (`MAXT`).
-   **Tributaries:** Number of tributaries and their properties (location, discharge, nutrient concentrations).

The `readConfigFile()` function in `init.c` reads the `config.txt` file and assigns the parameter values to the corresponding model variables.

### params.txt

The `params.txt` file contains the values of various process parameters used in the model, such as reaction rate constants, half-saturation constants, and stoichiometric ratios.

The `read_parameters()` function in `main.c` reads the `params.txt` file and assigns the parameter values to the corresponding model variables.

### init.c

The `init.c` file contains the `Init()` function, which performs the following tasks:

-   Reads the configuration files (`config.txt` and `params.txt`).
-   Allocates memory for the model variables.
-   Reads the boundary condition data from the input files.
-   Initializes the hydrodynamic, transport, and biogeochemical variables.

## Calibration and Validation

Calibration and validation are essential steps in the model development process. Calibration involves adjusting the model parameters to improve the agreement between the model predictions and the observed data. Validation involves evaluating the model performance using an independent dataset.

### Calibration

Calibration typically involves adjusting the following parameters:

-   **Hydrodynamic Parameters:** Chezy coefficient, Manning's n, or other friction parameters.
-   **Transport Parameters:** Dispersion coefficient, longitudinal dispersivity.
-   **Biogeochemical Parameters:** Reaction rate constants, half-saturation constants, stoichiometric ratios.

The calibration process can be performed manually or using automated optimization techniques.

### Validation

Validation involves comparing the model predictions with an independent dataset that was not used for calibration. The model performance can be evaluated using various statistical metrics, such as:

-   **Root Mean Square Error (RMSE)**
-   **Nash-Sutcliffe Efficiency (NSE)**
-   **Coefficient of Determination (R²)**

## Practical Output Analysis

The C-GEM model generates a variety of output data, including:

-   **Hydrodynamic Variables:** Water depth, flow velocity, discharge.
-   **Transport Variables:** Concentrations of dissolved and particulate substances.
-   **Biogeochemical Variables:** Concentrations of nutrients, oxygen, phytoplankton biomass, and other chemical and biological constituents.
-   **Reaction Rates:** Rates of various biogeochemical processes, such as nitrification, denitrification, and primary production.

The output data can be analyzed using various tools, such as:

-   **Spreadsheet Software:** Excel, Google Sheets, etc.
-   **Data Analysis Software:** Python, R, MATLAB, etc.
-   **Visualization Software:** ParaView, VisIt, etc.

### Output Logs in hyd.c

The `hyd.c` file contains the `Hydwrite()` function, which writes the hydrodynamic output data to a file. The output data includes the water depth, flow velocity, and discharge at each grid cell.

The `Hydwrite()` function is called at each time step, and the output data is written to a file in CSV format.

## Model Structure and Data Flow

The C-GEM model consists of three primary modules:

1.  **Hydrodynamics:** Simulates water flow, water depth, and velocity.
2.  **Transport:** Simulates the movement and mixing of dissolved and particulate substances.
3.  **Biogeochemistry:** Simulates the transformation of chemical and biological constituents.

The data flow between the modules is as follows:

1.  The Hydrodynamics module calculates the water depth and flow velocity at each grid cell.
2.  The Transport module uses the water depth and flow velocity to simulate the advection and dispersion of dissolved and particulate substances.
3.  The Biogeochemistry module uses the concentrations of dissolved and particulate substances to simulate the biogeochemical reactions.


# Chapter 7: Model Applications and Limitations

## Learning Objectives
After completing this chapter, you will be able to:
- Identify appropriate applications of the C-GEM model
- Understand the limitations and assumptions of the model
- Interpret model results with caution
- Apply the model to real-world case studies

## Typical Applications

### Eutrophication Assessment
The C-GEM model can be used to assess the impact of nutrient loading on water quality and ecosystem health.

### Climate Change Impact Assessment
The C-GEM model can be used to assess the impact of climate change on water quality and ecosystem dynamics.

## Limitations

### One-Dimensionality
The C-GEM model is a one-dimensional model, which limits its ability to simulate complex flow patterns and stratification.

### Simplified Biogeochemistry
The C-GEM model uses simplified representations of biogeochemical processes, which may not capture all of the complexities of real-world systems.

## Example Case Studies
Consider a case study:
- Chesapeake Bay
- San Francisco Bay
- Baltic Sea

The model can be used to:
- Simulate nutrient loading
- Predict phytoplankton blooms
- Assess oxygen depletion

Expand references to bcforcing.c for boundary definitions.

## Tutorial: Applying C-GEM to a New River

This section guides you through setting up C-GEM for a different river system, from data preparation to interpreting final results.

### Data Preparation
1. Gather boundary data:
   - Upstream inflow time series (discharge, temperature, nutrients).
   - Downstream (tidal) water levels or stage data.
   - Tributary inputs (if any).
2. Geometry & Bathymetry:
   - Cross-sectional profiles or width/depth estimates per segment.
   - Longitudinal bed slope.
3. Biogeochemical properties:
   - Initial concentrations of nutrients and oxygen.
   - Reaction rate constants for nitrification, phytoplankton growth, etc.

### Configuring the Model
Open **config.txt** (or your chosen configuration file):
- Update [Paths] to point to your new boundary files, geometry file, and tributary data.
- Adjust the number of cells, domain length, and any new parameter sets for reaction kinetics.

### Minimal Code Edits
Review and modify:
```c
// bcforcing.c
double Discharge_ups(int t) {
    // Replace with function to read or interpolate your new upstream flow file
    // e.g., read from "RiverX_upstream.txt"
    return upstreamFlowArray[t];
}
```
- Ensure readConfigFile() references the correct filenames for your system.  
- In bcforcing.c, confirm that any new tributary indexes match your domain setup.

### Running the Model
1. Compile the model:
   ```bash
   make clean
   make
   ```
2. Execute:
   ```bash
   ./cgem.exe
   ```
   Confirm that “Init successful!” messages appear, indicating correct file reading.

### Output Interpretation
1. Hydrodynamic Output:
   - Check water depth (H) and flow velocity (U) time series. Look for physical consistency (no negative depths).
2. Transport Output:
   - Compare computed concentration profiles at key locations with observed data.
   - Plot nutrient dispersion along the river over time.
3. Biogeochemical Output (if enabled):
   - Evaluate oxygen levels, algal biomass, or nitrification rates.
   - Identify any unrealistic spikes or negative concentrations (possible numeric instabilities).
4. Sensitivity & Uncertainty:
   - Test different reaction rates or boundary conditions to see how the solution changes.
   - Document each variation carefully for your final report.

### Advanced Tips
- For strongly tidal rivers: use smaller time steps or refine the mesh near the mouth.
- For large tributaries: ensure each lateral inflow is represented in bcforcing.c with correct indices.

## Study Questions
1. What are the key limitations of the C-GEM model?
2. When is it appropriate to use a 1D model versus a 2D or 3D model?
3. How can you account for uncertainty in model predictions?

## References

*   Jorgensen, S. E., & Bendoricchio, G. (2001). *Fundamentals of Ecological Modelling*. Elsevier.
*   Beck, M. B. (1987). *Water Quality Modeling: A Review of the Analysis of Uncertainty*. IIASA.
