import pandas as pd
import argparse

def reorder_matrix(input_file, output_file, column_index, reverse=False):
    """
    Reorders rows in a space-separated matrix based on a specified column using pandas.

    Args:
        input_file (str): Path to the input .txt file.
        output_file (str): Path to save the reordered .txt file.
        column_index (int): Index of the column to sort by (0-based).
        reverse (bool): Whether to sort in descending order.
    """
    # Load the file into a pandas DataFrame
    try:
        df = pd.read_csv(input_file, delim_whitespace=True, header=None)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Sort the DataFrame by the specified column
    try:
        sorted_df = df.sort_values(by=column_index, ascending=(not reverse))
    except KeyError:
        print(f"Error: Column index {column_index} is out of range.")
        return

    # Save the sorted DataFrame back to a file
    sorted_df.to_csv(output_file, sep=' ', index=False, header=False)
    print(f"Matrix sorted by column {column_index} and saved to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reorder rows in a space-separated matrix based on a column using pandas.")
    parser.add_argument("input_file", help="Path to the input .txt file containing the matrix.")
    parser.add_argument("output_file", help="Path to the output .txt file to save the reordered matrix.")
    parser.add_argument("column_index", type=int, help="Column index (0-based) to sort by.")
    parser.add_argument("--reverse", action="store_true", help="Sort in descending order (default is ascending).")

    args = parser.parse_args()
    reorder_matrix(args.input_file, args.output_file, args.column_index, args.reverse)