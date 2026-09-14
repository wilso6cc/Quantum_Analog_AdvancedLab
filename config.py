import os

linear_folder = "./data/Linear_Particle_Box/"
linear_spectra = os.path.join(linear_folder, "spectra")

one_dimensional_folder = "./data/One-Dimensional_Solid/"
one_dimensional_spectra = os.path.join(one_dimensional_folder, "spectra")

modeling_hydrogen_atom_folder = "./data/Modeling_Hydrogen_Atom/"
modeling_molecule_folder = "./data/Modeling_Molecule/"

atom_spectra = os.path.join(modeling_hydrogen_atom_folder, "Spectra")
molecule_spectra = os.path.join(modeling_molecule_folder, "Spectra")

spectra_style = "./spectra_plot_style.txt"
plot_style = "./plot_style.txt"