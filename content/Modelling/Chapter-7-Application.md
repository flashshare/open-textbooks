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

### TMDL Development
The C-GEM model can be used to develop Total Maximum Daily Loads (TMDLs) for pollutants in tidal rivers and estuaries.

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
