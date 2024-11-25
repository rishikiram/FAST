import glob
import os

bits = ["(0,3355190520)",
    "(6711522136,10066732088)",
    "(13422637104,16778064008)",
    "(20133538888,23488928632)",
    "(26844495728,30199909296)",
    "(40266958712,43621969240)",
    "(46978042304,50333352128)",
    "(33555546984,36910721320)",
    "(53689281656,57044507912)",
    "(60400301584,63755659736)",
    "(67112012032,70467249832)",
    "(73823453544,77178857192)",
    "(80535046984,83890252960)",
    "(87246375720,90601365128)",
    "(93957510976,97312858008)",
    "(100668863744,104024236584)"
    ]
template = "../data/waveformsFORK/fingerprints/candidate_pairs_FORK_GHZ_4,2(0,6918718)_%s_pairs_tmp"



# Define the directory and pattern
directory = "../data/waveformsFORK/fingerprints/"
pattern = "*_pairs_tmp"  # Example: match all .txt files

# Use glob to get files matching the pattern
for file_path in glob.glob(f"{directory}/{pattern}"):
    is_good = False
    for b in bits:
        if b in file_path:
            is_good = True
    if not is_good:
        print("Removing %s"%file_path)
        # os.remove(file_path)