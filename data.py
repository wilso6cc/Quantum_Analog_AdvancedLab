import os
from pathlib import Path
import pandas as pd
from config import linear_spectra, one_dimensional_spectra

def dat_spectra(folderpath, args={'sep': '\s+', 'names': ['frequency', 'amplitude']}, print_option=False) -> dict:
    dataframe, filenames = {}, {}
    
    for file in Path(folderpath).iterdir():
        if file.is_file():
            key = file.name.split("_")[0]
            path = os.path.join(folderpath, file.name)
            dataframe[key] = pd.read_csv(path, **args)
            filenames[key] = file.name.split(".")[0]
            
    if print_option:
        print(dataframe.keys())
    
    return dataframe, filenames

linear, linear_filenames = dat_spectra(folderpath=linear_spectra)
onedimensional, onedimensional_filenames = dat_spectra(folderpath=one_dimensional_spectra)