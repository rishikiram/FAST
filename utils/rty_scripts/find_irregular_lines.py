import sys

def find_irregular_lines(input_file, output_file):
    """
    Searches a text file for lines that do not have exactly three elements when split by spaces
    and writes those lines to an output file.

    :param input_file: Path to the input text file.
    :param output_file: Path to the output text file where irregular lines will be stored.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            line_number = 0
            for line in infile:
                line_number += 1
                # Strip the line of leading/trailing whitespaces and split by spaces
                elements = line.strip().split()
                # Check if the line does not contain exactly 3 elements
                if len(elements) != 3:
                    outfile.write(f"Line {line_number}: {line}")
        print(f"Irregular lines have been written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        find_irregular_lines(input_file_path, output_file_path)