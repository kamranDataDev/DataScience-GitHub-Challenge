"""Beginner-friendly Iris dataset analysis.

This script does the following:
1. Loads the Iris dataset from scikit-learn.
2. Saves a clean CSV copy into the data folder.
3. Creates summary tables and saves them into the output folder.
4. Generates common exploratory charts and saves them into the charts folder.
5. Prints a short report so the analysis can be understood from the terminal.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib  # type: ignore[import-not-found]

# Use a non-interactive backend so charts can be saved in any environment.
matplotlib.use("Agg")

import matplotlib.pyplot as plt  # type: ignore[import-not-found]
import pandas as pd
import seaborn as sns  # type: ignore[import-not-found]
from sklearn.datasets import load_iris


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
CHARTS_DIR = PROJECT_ROOT / "charts"
OUTPUT_DIR = PROJECT_ROOT / "output"
DATA_FILE = DATA_DIR / "iris.csv"
SUMMARY_FILE = OUTPUT_DIR / "summary.csv"
GROUP_STATS_FILE = OUTPUT_DIR / "group_statistics.csv"


def prepare_directories() -> None:
	"""Create the project folders if they do not already exist."""
	DATA_DIR.mkdir(exist_ok=True)
	CHARTS_DIR.mkdir(exist_ok=True)
	OUTPUT_DIR.mkdir(exist_ok=True)


def load_iris_dataframe() -> pd.DataFrame:
	"""Load the Iris dataset into a clean pandas DataFrame.

	The built-in scikit-learn version is reliable and avoids manual downloads.
	We convert it to a DataFrame, rename the numeric target to a readable species
	column, and keep only the analysis-ready fields.
	"""
	iris = load_iris(as_frame=True)
	frame = iris.frame.copy()
	frame["species"] = frame["target"].map(dict(enumerate(iris.target_names)))
	frame = frame.drop(columns=["target"])
	frame = frame[[
		"sepal length (cm)",
		"sepal width (cm)",
		"petal length (cm)",
		"petal width (cm)",
		"species",
	]]
	return frame


def save_dataset(frame: pd.DataFrame) -> None:
	"""Save the dataset into the data folder for easy reuse."""
	frame.to_csv(DATA_FILE, index=False)


def save_summary_tables(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
	"""Create and save the statistical summary tables.

	Returns
	-------
	(summary, group_statistics)
		The two tables are returned so they can also be shown in the console.
	"""
	feature_columns = [column for column in frame.columns if column != "species"]
	summary = frame[feature_columns].describe().round(3)
	group_statistics = frame.groupby("species")[feature_columns].agg(["mean", "median", "std"]).round(3)
	group_statistics.columns = [f"{feature}__{statistic}" for feature, statistic in group_statistics.columns]

	summary.to_csv(SUMMARY_FILE)
	group_statistics.to_csv(GROUP_STATS_FILE)
	return summary, group_statistics


def create_histogram(frame: pd.DataFrame) -> Path:
	"""Create a histogram to show the distribution of one key feature."""
	chart_path = CHARTS_DIR / "histogram_sepal_length.png"
	plt.figure(figsize=(8, 5))
	sns.histplot(data=frame, x="sepal length (cm)", bins=12, kde=True, color="#2a9d8f")
	plt.title("Histogram of Sepal Length")
	plt.xlabel("Sepal Length (cm)")
	plt.ylabel("Count")
	plt.tight_layout()
	plt.savefig(chart_path, dpi=150)
	plt.close()
	return chart_path


def create_scatter_plot(frame: pd.DataFrame) -> Path:
	"""Create a scatter plot for two flower measurements."""
	chart_path = CHARTS_DIR / "scatter_petal_dimensions.png"
	plt.figure(figsize=(8, 5))
	sns.scatterplot(
		data=frame,
		x="petal length (cm)",
		y="petal width (cm)",
		hue="species",
		palette="deep",
		s=70,
	)
	plt.title("Petal Length vs Petal Width")
	plt.xlabel("Petal Length (cm)")
	plt.ylabel("Petal Width (cm)")
	plt.legend(title="Species")
	plt.tight_layout()
	plt.savefig(chart_path, dpi=150)
	plt.close()
	return chart_path


def create_box_plot(frame: pd.DataFrame) -> Path:
	"""Create a box plot to compare measurements across species."""
	chart_path = CHARTS_DIR / "box_plot_measurements_by_species.png"
	long_frame = frame.melt(id_vars="species", var_name="measurement", value_name="value")
	plt.figure(figsize=(12, 6))
	sns.boxplot(data=long_frame, x="measurement", y="value", hue="species")
	plt.title("Measurement Distribution by Species")
	plt.xlabel("Measurement")
	plt.ylabel("Value (cm)")
	plt.xticks(rotation=15)
	plt.legend(title="Species", loc="upper left", bbox_to_anchor=(1, 1))
	plt.tight_layout()
	plt.savefig(chart_path, dpi=150)
	plt.close()
	return chart_path


def create_correlation_heatmap(frame: pd.DataFrame) -> Path:
	"""Create a heatmap showing how the numeric features relate to each other."""
	chart_path = CHARTS_DIR / "correlation_heatmap.png"
	feature_columns = [column for column in frame.columns if column != "species"]
	correlation = frame[feature_columns].corr()

	plt.figure(figsize=(8, 6))
	sns.heatmap(correlation, annot=True, cmap="YlGnBu", fmt=".2f", square=True)
	plt.title("Correlation Heatmap")
	plt.tight_layout()
	plt.savefig(chart_path, dpi=150)
	plt.close()
	return chart_path


def print_report(frame: pd.DataFrame, summary: pd.DataFrame, group_statistics: pd.DataFrame) -> None:
	"""Print a concise beginner-friendly report in the terminal."""
	print("Iris Dataset Analysis")
	print("=====================")
	print(f"Dataset saved to: {DATA_FILE}")
	print(f"Summary saved to: {SUMMARY_FILE}")
	print(f"Group statistics saved to: {GROUP_STATS_FILE}")
	print()

	print("Preview of the dataset")
	print(frame.head().to_string(index=False))
	print()

	print("Species counts")
	print(frame["species"].value_counts().to_string())
	print()

	print("Statistical summary")
	print(summary.to_string())
	print()

	print("Group statistics by species")
	print(group_statistics.to_string())


def main() -> None:
	"""Run the full Iris analysis workflow."""
	prepare_directories()
	frame = load_iris_dataframe()
	save_dataset(frame)
	summary, group_statistics = save_summary_tables(frame)
	chart_paths = [
		create_histogram(frame),
		create_scatter_plot(frame),
		create_box_plot(frame),
		create_correlation_heatmap(frame),
	]
	print_report(frame, summary, group_statistics)
	print()
	print("Charts created")
	for chart_path in chart_paths:
		print(f"- {chart_path}")


if __name__ == "__main__":
	main()
