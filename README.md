# HeunSimulation
This repository contains the code necessary to perform monodromy simulations with the Heun Equation.

## Steps to conduct a simulation
To conduct a simulation, complete the following:
1. Download all python files within this repository.
2. Change the parameters at the top of `main.py` to the desired form of the Heun Equation.
3. Run the `get_data` function in `VisualizationDatasetGenerator.py` with the desired number of iterations on each pixel, resolution, and image size as well as an appropriate naming modification.
   1. This will generate a .csv file of different resultant eigenvalues on each pixel.
   2. This step takes a fairly long time to run.
4. To obtain a Convergence Map, input the resultant CSV file into the `eigvis` function in `EigenValueVisualization.py` along with the appropriate resolution and size of the image.
5. To obtain refined approximations, run the `compileEigenvalues` function in `Eigenvalue Processing.py` with the appropriate epsilon/delta parameters and an already generated dataset for said parameter values.
