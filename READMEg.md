# ScreenSense

A data analysis and preprocessing project.

## Project Structure

```
screensense/
├── data/
│   ├── raw/          # Raw data files
│   └── processed/    # Processed data files
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_feature_engineering.ipynb
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   └── feature_engineering.py
├── outputs/
│   └── figures/      # Generated figures and visualizations
└── README.md
```

## Getting Started

1. Place your raw data files in the `data/raw/` directory
2. Run the notebooks in order:
   - `01_data_understanding.ipynb` - Explore and understand the data
   - `02_preprocessing.ipynb` - Clean and preprocess the data
   - `03_feature_engineering.ipynb` - Create engineered features (age bands, weekday/weekend flags, screentime buckets)
3. Processed data will be saved in `data/processed/`
4. Figures and visualizations will be saved in `outputs/figures/`

## Features

The feature engineering module creates:
- **Age bands**: 3-5, 6-9, 10-13, 14-17
- **Weekday vs Weekend flag**: Identifies weekdays and weekends
- **Screentime buckets** (optional): Low/Medium/High usage categories

## Requirements

- Python 3.9+
- pandas
- numpy
- matplotlib
- jupyter

## Installation

```bash
pip install pandas numpy matplotlib jupyter
```

## Usage

Start Jupyter Notebook:
```bash
jupyter notebook
```

Then navigate to the `notebooks/` directory and open the notebooks.
