# Hyperspectral Data Analysis Thesis

This repository contains the code and analysis for a hyperspectral data analysis thesis project. The project focuses on processing, analyzing, and classifying hyperspectral imagery data.

## Project Structure

```
Hyperspectral_Thesis/
├── data/
│   ├── raw/                    # Raw hyperspectral data files
│   │   ├── LRG07-PC04_0001/
│   │   ├── LRG07-PC04_0002/
│   │   ├── LRG07-PC04_0003/
│   │   └── LRG07-PC04_0004/
│   ├── processed/              # Preprocessed data
│   └── reference_library/      # Spectral reference libraries
├── notebooks/                  # Jupyter notebooks for analysis
│   ├── 01_data_exploration.ipynb
│   ├── 02_spectral_analysis.ipynb
│   └── 03_ml_classification.ipynb
├── src/                        # Source code modules
│   ├── __init__.py
│   ├── data_loader.py         # Data loading and preprocessing
│   ├── spectral_analysis.py   # Spectral analysis functions
│   └── plotting.py            # Visualization functions
├── outputs/                    # Analysis outputs
│   ├── plots/                 # Generated plots and figures
│   ├── models/                # Trained models
│   └── results/               # Analysis results
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Hyperspectral_Thesis
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Data Loading
The `src/data_loader.py` module provides functions for loading hyperspectral data in various formats:

```python
from src.data_loader import load_hyperspectral_data
data, metadata = load_hyperspectral_data('path/to/data', file_format='envi')
```

### Spectral Analysis
Use the `src/spectral_analysis.py` module for spectral signature analysis:

```python
from src.spectral_analysis import calculate_spectral_indices, smooth_spectrum
indices = calculate_spectral_indices(data, wavelengths)
smoothed = smooth_spectrum(spectrum, method='savgol')
```

### Visualization
The `src/plotting.py` module provides various plotting functions:

```python
from src.plotting import plot_spectrum, plot_rgb_composite
fig = plot_spectrum(spectrum, wavelengths)
rgb_fig = plot_rgb_composite(data, rgb_bands=(29, 19, 9))
```

### Jupyter Notebooks
The analysis is organized into three main notebooks:

1. **01_data_exploration.ipynb**: Initial data exploration and visualization
2. **02_spectral_analysis.ipynb**: Spectral signature analysis and feature extraction
3. **03_ml_classification.ipynb**: Machine learning classification of hyperspectral data

## Data Format

This project expects hyperspectral data in standard formats such as:
- ENVI format (.hdr/.dat files)
- HDF5 format (.h5/.hdf5 files)
- MATLAB format (.mat files)

## Key Features

- **Data Loading**: Support for multiple hyperspectral data formats
- **Preprocessing**: Normalization, bad band removal, and noise reduction
- **Spectral Analysis**: Calculation of spectral indices, continuum removal, absorption feature detection
- **Visualization**: Comprehensive plotting functions for spectra and hyperspectral images
- **Machine Learning**: Classification algorithms optimized for hyperspectral data
- **Modular Design**: Well-organized code structure for easy extension and maintenance

## Dependencies

Key dependencies include:
- NumPy, Pandas, SciPy for numerical computing
- Scikit-learn for machine learning
- Matplotlib, Seaborn for visualization
- Spectral library for hyperspectral data handling
- Jupyter for interactive analysis

See `requirements.txt` for the complete list of dependencies.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or collaboration opportunities, please contact [Your Name] at [your.email@example.com].

## Acknowledgments

- Thanks to the hyperspectral remote sensing community
- Special thanks to thesis advisors and collaborators
- Data provided by [Data Source/Institution] 