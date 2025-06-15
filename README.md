
# Introduction to the project


This project involves analyzing historical car insurance claim data for AlphaCare Insurance Solutions (ACIS) in South Africa.
The primary objectives are to optimize marketing strategies and identify low-risk customer segments eligible for reduced premiums,
thereby attracting new clients and enhancing the company's competitive edge in the market.


# Insurance Risk Analytics - Predictive Modeling

This project provides tools and workflows for analyzing insurance risk data, including data cleaning, exploratory analysis, and predictive modeling. Data versioning and reproducibility are managed using [DVC](https://dvc.org/).

## Project Structure

Insurance-Risk-Analytics-Predictive-Modeling/
│
├── data/                # Raw and processed data (DVC tracked)
├── notebooks/           # Jupyter notebooks for analysis
├── scripts/             # Python scripts for preprocessing and plotting
├── dvc.yaml             # DVC pipeline definition
├── dvc.lock             # DVC pipeline lock file
├── .dvc/                # DVC metadata
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Insurance-Risk-Analytics-Predictive-Modeling.git
cd Insurance-Risk-Analytics-Predictive-Modeling
```

### 2. Install Python Dependencies

It is recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Install DVC

```bash
pip install dvc
```

Or, for system-wide installation:

```bash
pipx install dvc
```

### 4. Configure DVC Remote (Optional)

If you want to share data with collaborators, set up a DVC remote (e.g., S3, GDrive):

```bash
dvc remote add -d myremote <remote-url>
dvc remote modify myremote <options>
```

### 5. Pull Data with DVC

To download the data files tracked by DVC:

```bash
dvc pull
```

This will fetch the required data into the `data/` directory.

### 6. Run the Analysis

Open the main notebook:

```bash
jupyter notebook inital_analysis.ipynb
```

Or use VS Code's Jupyter support.

### 7. Reproduce the Pipeline

If you have a DVC pipeline set up (see `dvc.yaml`), you can reproduce all steps:

```bash
dvc repro
```

## Adding and Tracking Data with DVC

To add new data files and track them with DVC:

```bash
dvc add data/new_data_file.csv
git add data/new_data_file.csv.dvc .gitignore
git commit -m "Add new data file and track with DVC"
dvc push
```

## References

- [DVC Documentation](https://dvc.org/doc)
- [Project Wiki](docs/)

---

**Note:**  
Never commit large data files directly to Git. Always use DVC for data versioning and sharing.
```