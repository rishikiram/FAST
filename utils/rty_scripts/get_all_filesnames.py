import os
import glob
import re
DATA_DIR = "/home/rootrish/FAST/data/waveformsFORK"
ETB_DIR =  "/home/rootrish/FAST/data/waveformsFORK"


def rename_files_with_regex(folder_path, regex_pattern, replacement):
    try:
        # Get a list of all files in the folder
        file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        # Compile the regex pattern
        pattern = re.compile(regex_pattern)
        
        # Loop through the files and rename them
        for file_name in file_names:
            # Check if the pattern matches the file name
            if pattern.search(file_name):
                # Replace the pattern with the replacement string
                new_name = pattern.sub(replacement, file_name)
                
                # Perform the renaming
                old_path = os.path.join(folder_path, file_name)
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed: {file_name} -> {new_name}")
        
        print("All applicable files renamed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    rename_files_with_regex(DATA_DIR, r'timeseries_', 'Deci500.')
    rename_files_with_regex(DATA_DIR, r'_pm', '-12-00-00')
    rename_files_with_regex(DATA_DIR, r'_am', '-00-00-00')
    rename_files_with_regex(DATA_DIR, r'.mseed', '.UU.FORK.01.GHZ.mseed')
    single_digit = r'(?<!\d)(\d)(?!\d)'
    insert_0 = r'0\1'
    rename_files_with_regex(DATA_DIR, single_digit, insert_0)
   
    file_arr = sorted(glob.glob(DATA_DIR+'*.mseed'))
    array_string = f"[{',\n'.join(f'\"{ETB_DIR+os.path.basename(file)}\"' for file in file_arr)}]"
    print(array_string)