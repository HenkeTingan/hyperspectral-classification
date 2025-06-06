"""
Plotting Module

This module contains functions for visualizing hyperspectral data and analysis results.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from typing import Optional, List, Tuple, Dict
import warnings


def plot_spectrum(spectrum: np.ndarray, 
                 wavelengths: np.ndarray,
                 title: str = "Spectral Signature",
                 xlabel: str = "Wavelength (nm)",
                 ylabel: str = "Reflectance",
                 figsize: Tuple[int, int] = (10, 6)) -> plt.Figure:
    """
    Plot a single spectrum.
    
    Parameters:
    -----------
    spectrum : np.ndarray
        Spectral values
    wavelengths : np.ndarray
        Corresponding wavelengths
    title : str
        Plot title
    xlabel, ylabel : str
        Axis labels
    figsize : tuple
        Figure size
    
    Returns:
    --------
    fig : matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(wavelengths, spectrum, linewidth=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig


def plot_spectrum_comparison(spectra: List[np.ndarray], 
                           wavelengths: np.ndarray,
                           labels: List[str],
                           title: str = "Spectral Comparison",
                           figsize: Tuple[int, int] = (12, 8)) -> plt.Figure:
    """
    Plot multiple spectra for comparison.
    
    Parameters:
    -----------
    spectra : list
        List of spectral arrays
    wavelengths : np.ndarray
        Corresponding wavelengths
    labels : list
        Labels for each spectrum
    title : str
        Plot title
    figsize : tuple
        Figure size
    
    Returns:
    --------
    fig : matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    for spectrum, label in zip(spectra, labels):
        ax.plot(wavelengths, spectrum, label=label, linewidth=2)
    
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Reflectance")
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig


def plot_rgb_composite(data: np.ndarray, 
                      rgb_bands: Tuple[int, int, int] = (29, 19, 9),
                      title: str = "RGB Composite",
                      figsize: Tuple[int, int] = (10, 8)) -> plt.Figure:
    """
    Create RGB composite image from hyperspectral data.
    
    Parameters:
    -----------
    data : np.ndarray
        Hyperspectral data (height, width, bands)
    rgb_bands : tuple
        Band indices for R, G, B channels
    title : str
        Plot title
    figsize : tuple
        Figure size
    
    Returns:
    --------
    fig : matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Extract RGB bands
    r_band, g_band, b_band = rgb_bands
    rgb_image = np.stack([
        data[:, :, r_band],
        data[:, :, g_band],
        data[:, :, b_band]
    ], axis=2)
    
    # Normalize to 0-1 range
    rgb_image = (rgb_image - rgb_image.min()) / (rgb_image.max() - rgb_image.min())
    
    ax.imshow(rgb_image)
    ax.set_title(title)
    ax.axis('off')
    plt.tight_layout()
    return fig


def plot_spectral_indices(indices: Dict[str, np.ndarray],
                         figsize: Tuple[int, int] = (15, 10)) -> plt.Figure:
    """
    Plot multiple spectral indices as subplots.
    
    Parameters:
    -----------
    indices : dict
        Dictionary of spectral indices
    figsize : tuple
        Figure size
    
    Returns:
    --------
    fig : matplotlib.figure.Figure
        Figure object
    """
    n_indices = len(indices)
    n_cols = min(3, n_indices)
    n_rows = (n_indices + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    if n_indices == 1:
        axes = [axes]
    elif n_rows == 1:
        axes = axes.reshape(1, -1)
    
    for i, (name, index_data) in enumerate(indices.items()):
        row = i // n_cols
        col = i % n_cols
        ax = axes[row, col] if n_rows > 1 else axes[col]
        
        im = ax.imshow(index_data, cmap='viridis')
        ax.set_title(name)
        ax.axis('off')
        plt.colorbar(im, ax=ax, shrink=0.8)
    
    # Hide empty subplots
    for i in range(n_indices, n_rows * n_cols):
        row = i // n_cols
        col = i % n_cols
        ax = axes[row, col] if n_rows > 1 else axes[col]
        ax.axis('off')
    
    plt.tight_layout()
    return fig


def plot_confusion_matrix(y_true: np.ndarray, 
                         y_pred: np.ndarray,
                         class_names: Optional[List[str]] = None,
                         title: str = "Confusion Matrix",
                         figsize: Tuple[int, int] = (8, 6)) -> plt.Figure:
    """
    Plot confusion matrix.
    
    Parameters:
    -----------
    y_true : np.ndarray
        True labels
    y_pred : np.ndarray
        Predicted labels
    class_names : list, optional
        Class names for labels
    title : str
        Plot title
    figsize : tuple
        Figure size
    
    Returns:
    --------
    fig : matplotlib.figure.Figure
        Figure object
    """
    from sklearn.metrics import confusion_matrix
    
    cm = confusion_matrix(y_true, y_pred)
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=class_names, yticklabels=class_names)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.set_title(title)
    plt.tight_layout()
    return fig


def plot_pca_components(components: np.ndarray,
                       wavelengths: np.ndarray,
                       n_components: int = 5,
                       figsize: Tuple[int, int] = (12, 8)) -> plt.Figure:
    """
    Plot PCA components.
    
    Parameters:
    -----------
    components : np.ndarray
        PCA components
    wavelengths : np.ndarray
        Wavelength values
    n_components : int
        Number of components to plot
    figsize : tuple
        Figure size
    
    Returns:
    --------
    fig : matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    for i in range(min(n_components, components.shape[0])):
        ax.plot(wavelengths, components[i], label=f'PC{i+1}', linewidth=2)
    
    ax.set_xlabel('Wavelength (nm)')
    ax.set_ylabel('Component Loading')
    ax.set_title('Principal Components')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig 