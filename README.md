# PBA Analysis
### Summary
For this project, I am using Python to analyze computational data on Prussian Blue Analogue (PBA) structures for use in battery electrodes. Specifically, I am looking at how the atoms present in the structure affect the stability, cyclability, and electrochemical performance. Eventually, I plan to build a machine learning model capable of predicting battery performance given atom identities.

This research is being completed under the Persson Group at Lawrence Berkeley National Laboratory.

### Data
The data used in this project comes from high throughput calculations using density functional theory (DFT) using the projector augmented wave (PAW) method. Structure optimization and ground state energy were calculated with self-documented workflows in Atomate, which uses Fireworks for workflow management and pymatgen for materials analysis.

The majority of the analysis uses the pymatgen library (Python Materials Genomics), which is a computational materials science package maintained by the Ong group at University of California, San Diego.
