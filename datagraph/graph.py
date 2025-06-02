import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import argparse

def generate_plot(csv_path, x_column=None, y_columns=None, chart_type="line",
                  output_path="output.png", title=None, figsize=(10, 6), palette="muted"):
    """
    Generate a graph from a CSV file.

    Args:
        csv_path (str): Path to the CSV file.
        x_column (str): Column for X-axis (not required for pie/hist).
        y_columns (list): Columns for Y-axis or values (depends on chart type).
        chart_type (str): Type of chart.
        output_path (str): Path to save the graph.
        title (str): Title of the graph.
        figsize (tuple): Size of the figure.
        palette (str): Seaborn color palette.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"File not found: {csv_path}")

    df = pd.read_csv(csv_path)
    plt.figure(figsize=figsize)

    if chart_type in ["line", "bar", "scatter", "area"]:
        if not x_column or not y_columns:
            raise ValueError("x_column and y_columns must be specified")
        for y in y_columns:
            if chart_type == "line":
                sns.lineplot(data=df, x=x_column, y=y, label=y, palette=palette)
            elif chart_type == "bar":
                sns.barplot(data=df, x=x_column, y=y, palette=palette)
            elif chart_type == "scatter":
                sns.scatterplot(data=df, x=x_column, y=y, label=y, palette=palette)
            elif chart_type == "area":
                plt.fill_between(df[x_column], df[y], label=y, alpha=0.4)
    elif chart_type == "hist":
        if not y_columns:
            raise ValueError("y_columns must be specified for histogram")
        for y in y_columns:
            sns.histplot(df[y], kde=True, label=y, palette=palette)
    elif chart_type == "pie":
        if not y_columns or len(y_columns) != 1:
            raise ValueError("Specify one y_column for pie chart")
        counts = df[y_columns[0]].value_counts()
        counts.plot.pie(autopct='%1.1f%%', startangle=90)
        plt.ylabel('')
    else:
        raise ValueError(f"Unsupported chart_type: {chart_type}")

    if title:
        plt.title(title)
    if chart_type != "pie":
        plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def main():
    parser = argparse.ArgumentParser(description="Generate a graph from a CSV file.")
    parser.add_argument("csv", help="Path to CSV file")
    parser.add_argument("--x", help="X-axis column (not needed for pie/hist)")
    parser.add_argument("--y", nargs='+', required=True, help="Y-axis column(s)")
    parser.add_argument("--type", default="line", help="Type of chart (line, bar, scatter, area, hist, pie)")
    parser.add_argument("--output", default="output.png", help="Output image file")
    parser.add_argument("--title", help="Title of the chart")
    parser.add_argument("--size", nargs=2, type=float, default=[10, 6], help="Figure size (width height)")
    parser.add_argument("--palette", default="muted", help="Seaborn color palette")

    args = parser.parse_args()
    generate_plot(args.csv, args.x, args.y, args.type, args.output, args.title, tuple(args.size), args.palette)

if __name__ == "__main__":
    main()
