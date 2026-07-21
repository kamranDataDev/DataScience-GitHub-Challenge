# Iris Dataset Analysis Project

This repository is a beginner-friendly data science project that explores the classic Iris dataset with Python, pandas, and visualization libraries.

The project loads the dataset, saves a clean CSV copy, creates summary tables, generates charts, and stores every result in an organized folder structure.

## Project Overview

The Iris dataset is a small but famous machine learning dataset that contains measurements of iris flowers from three species:

- Setosa
- Versicolor
- Virginica

This project demonstrates a simple end-to-end workflow for exploring the dataset using pandas and saving the results in a reusable format.

## Objectives

- Load the Iris dataset into a pandas DataFrame.
- Save the dataset as a CSV file for later reuse.
- Calculate descriptive statistics and group statistics.
- Create beginner-friendly charts for exploration.
- Organize data, charts, and outputs into separate folders.

## Dataset Information

- Source: built-in Iris dataset from scikit-learn
- Samples: 150 rows
- Features: 4 numeric measurements
- Classes: 3 species

Columns used in the analysis:

- sepal length (cm)
- sepal width (cm)
- petal length (cm)
- petal width (cm)
- species

## Technologies Used

- Python
- pandas
- matplotlib
- seaborn
- scikit-learn

## Folder Structure

```text
DataScience-GitHub-Challenge/
├── analysis.py
├── README.md
├── requirements.txt
├── data/
│   └── iris.csv
├── charts/
│   ├── histogram_sepal_length.png
│   ├── scatter_petal_dimensions.png
│   ├── box_plot_measurements_by_species.png
│   └── correlation_heatmap.png
└── output/
	├── summary.csv
	└── group_statistics.csv
```

## Installation Guide

1. Open a terminal in the project folder.
2. Install the required packages:

```bash
python -m pip install -r requirements.txt
```

If you prefer to use a virtual environment, create and activate it first, then run the same command.

## How to Run

Run the analysis script from the project root:

```bash
python analysis.py
```

The script will:

- load the Iris dataset,
- save a clean copy to `data/iris.csv`,
- save statistical tables to `output/`,
- generate charts in `charts/`,
- print a short report in the terminal.

## Expected Output

After running the script, you should see:

- `data/iris.csv` with the full dataset
- `output/summary.csv` with descriptive statistics
- `output/group_statistics.csv` with grouped statistics by species
- `charts/histogram_sepal_length.png`
- `charts/scatter_petal_dimensions.png`
- `charts/box_plot_measurements_by_species.png`
- `charts/correlation_heatmap.png`

## Learning Outcomes

By studying this project, you can learn how to:

- load real-world data into pandas,
- inspect and summarize a dataset,
- save clean datasets and analysis results,
- create basic charts for exploratory data analysis,
- structure a small data science project in a clear and reusable way.

## Notes

- The dataset is loaded from scikit-learn, so no manual download is required.
- The script creates the `data/`, `charts/`, and `output/` folders automatically if they do not already exist.
