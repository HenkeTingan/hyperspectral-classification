# Data Directory

This directory contains the hyperspectral datasets used in this analysis.

## Data Structure
```
data/
├── raw/
│   └── LRG07-PC04/           # Raw hyperspectral data from Geotek system
│       ├── LRG07-PC04_0001/
│       ├── LRG07-PC04_0002/
│       ├── LRG07-PC04_0003/
│       └── LRG07-PC04_0004/
├── processed/                # Preprocessed data files
└── reference_library/        # Spectral reference libraries
```

## Data Source
- **Instrument**: Geotek hyperspectral system
- **Sample Type**: Core samples LRG07-PC04
- **File Formats**: .txt files with spectral measurements

## Data Access
The raw data files are not included in this repository due to size constraints.
To reproduce this analysis:
1. Obtain the LRG07-PC04 dataset
2. Place files in the `data/raw/LRG07-PC04/` directory
3. Run the data loading notebooks

## File Descriptions
- `geotek.txt`: Main spectral data file
- `geotek_in.txt`: Input parameters
- `complete.txt`: Processing completion status
- `MinSpecFolderMonitorAudit.txt`: System audit log 