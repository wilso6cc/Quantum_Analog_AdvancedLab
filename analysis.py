import matplotlib.pyplot as plt
from config import spectra_style, plot_style
from data import linear, linear_filenames, onedimensional, onedimensional_filenames
import numpy as np

def single_full_spectra(dataframe, filename, folder):
    
    absmax = np.max(dataframe['frequency']/1000)
    absmin = np.min(dataframe['frequency']/1000)
    
    params = {'lw': 2, 'color': 'black'}
    
    plt.style.use(spectra_style)
    plt.figure()
    
    plt.plot(dataframe['frequency']/1000, dataframe['amplitude'], **params)
    
    plt.xlim(left=absmin, right=absmax)
    plt.xlabel("Frequency [kHz]")
    plt.ylabel("Amplitude [a.u.]")
    plt.xticks(list(range(0, 11, 1)))
    
    save_path = f"./Plots/full_spectra/{folder}/{filename}_spectrum.png"
    plt.tight_layout()
    plt.grid(True, alpha=0.25, linestyle='--')
    plt.savefig(save_path)
    
    return

if __name__ == "__main__":
    for n in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven']:
        single_full_spectra(dataframe=linear[n], filename=linear_filenames[n], folder='linear')
        
    for n in ['0mm', '10mm', '13mm', '16mm']:
        single_full_spectra(dataframe=onedimensional[n], filename=onedimensional_filenames[n], folder='onedimensional')