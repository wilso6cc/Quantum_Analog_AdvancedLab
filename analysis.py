import matplotlib.pyplot as plt
from config import spectra_style, plot_style
from data import linear, linear_filenames, onedimensional, onedimensional_filenames
import numpy as np
import os
from scipy.special import eval_legendre

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
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.tight_layout()
    plt.grid(True, alpha=0.25, linestyle='--')
    plt.savefig(save_path)
    plt.close()
    
    return

def linear_spectra_comparisons(dataframe, folder):
    
    for groupname in [['zero', 'one'], ['two', 'three'], ['four', 'five'], ['six', 'seven']]:
        
        absmax = np.max(dataframe[groupname[0]]['frequency']/1000)
        absmin = np.min(dataframe[groupname[0]]['frequency']/1000)
        
        plt.style.use(spectra_style)
        plt.figure()
        
        plt.plot(dataframe[groupname[0]]['frequency']/1000, dataframe[groupname[0]]['amplitude'], color='red', label={groupname[0]})
        plt.plot(dataframe[groupname[1]]['frequency']/1000, dataframe[groupname[1]]['amplitude'], color='blue', label={groupname[1]})
        
        plt.xlim(left=absmin, right=absmax)
        plt.xlabel("Frequency [kHz]")
        plt.ylabel("Amplitude [a.u.]")
        plt.xticks(list(range(0, 11, 1)))
        
        save_path = f"./Plots/full_spectra/{folder}/{groupname[0]}_vs_{groupname[1]}_spectra.png"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.tight_layout()
        plt.grid(True, alpha=0.25, linestyle='--')
        plt.legend()
        plt.savefig(save_path)
        plt.close()
    
    return

def all_legendre_plots(folder='polar_legendre'):
    
    theta_deg = np.linspace(0, 360, 361)
    theta_rad = np.deg2rad(theta_deg)

    for i in range(0, 9):

        amplitude = np.abs(eval_legendre(i, np.cos(theta_rad)))
        
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        
        ax.plot(theta_rad, amplitude)
        ax.fill_between(theta_rad, 0, amplitude)
        
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)
        
        # ax.set_title(f'Legendre Polynomial {i}', va='bottom')
        
        save_path = f"./Plots/full_spectra/molecule/{folder}/legendre{i}.png"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path)
        plt.close(fig)
        
    return

def onedimensional_frequencyrange_comparison(dataframe, folder):
    
    keys = ['10mm', '13mm', '16mm']
    
    for region in [[2, 4], [4, 6], [6, 8]]:
        
        absmax = region[1]
        absmin = region[0]
        
        plt.style.use(spectra_style)
        plt.figure()
        
        for key, color in zip(keys, ['r', 'b', 'g']):
            plt.plot(dataframe[key]['frequency']/1000, dataframe[key]['amplitude'], color=color, lw=2, alpha=0.75)
        
        plt.xlim(left=absmin, right=absmax)
        plt.xlabel("Frequency [kHz]")
        plt.ylabel("Amplitude [a.u.]")
        plt.xticks(list(np.arange(region[0], region[1]+0.5, 0.5)))
        
        save_path = f"./Plots/full_spectra/{folder}/{region[0]}-{region[1]}kHz_comparison.png"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.tight_layout()
        plt.grid(True, alpha=0.25, linestyle='--')
        plt.savefig(save_path)
        plt.close()
    
    return

if __name__ == "__main__":
    
    for n in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven']:
        single_full_spectra(dataframe=linear[n], filename=linear_filenames[n], folder='linear')
        
    for n in ['0mm', '10mm', '13mm', '16mm']:
        single_full_spectra(dataframe=onedimensional[n], filename=onedimensional_filenames[n], folder='onedimensional')
        
    all_legendre_plots()

    onedimensional_frequencyrange_comparison(dataframe=onedimensional, folder='onedimensional')
    linear_spectra_comparisons(dataframe=linear, folder='linear')