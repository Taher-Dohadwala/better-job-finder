"""
This script is used to add labels to data for initial training
"""

"""
Data format for binary classifier
{
  "text": "string",
  "label": [
    "neg",
    "pos"
  ]
}

"""
import pandas as pd
import numpy as np
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow, blue

# helper function to reset labels
def quick_reset():
    df = pd.read_csv("data/combined_data.csv")
    df["Label"] = np.nan
    df.to_csv("data/combined_data_withlabel.csv")
    

# load raw data in
df = pd.read_csv("data/combined_data_withlabel.csv")

# finds place where previous labeling session ended
def find_continue_point(df):
    t = df.index[df["Label"] == 999]
    
    # First time labeling check
    if not t.any():
        start = 0
    else:
        start = int(t.tolist()[0])
    return start


start = find_continue_point(df)
print(f"Starting at {start}")
jobs_to_label = df["Job Description"]
current = start

try:
    # display job and ask for label
    for idx,job in enumerate(jobs_to_label[start:]):
        current = start + idx
        print(yellow(f"Example number: {current}"))
        print(job)
        print(red("-"*100))
        label = int(input("Label: "))
        df.iloc[current,df.columns.get_loc("Label")] = label
# ctrl-c will end labeling session and save progress
except KeyboardInterrupt:
    print(blue(f"ENDING AT: {current}"))
    print(green("SAVING LABELING RESULTS"))
    df['Label'][current] = 999
    df.to_csv("data/combined_data_withlabel.csv")
