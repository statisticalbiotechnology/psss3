#!/usr/bin/python

import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import seaborn as sns

result_file = Path("wideint.pkl")

if not result_file.exists():
    long = pd.read_table("../../data/PSSS3_triqlerFormatted_nonShared.csv")
    #long = pd.read_table("../data/test.tsv")
    wideInt = long.pivot_table(index=['proteins','peptide'], columns='run', values='intensity')
    wideInt.to_pickle(result_file)
else:
    wideInt = pd.read_pickle(result_file)

#wideScore = long.pivot_table(index=['proteins','peptide'], columns='run', values='searchScore')

for sampleGroup in range(1,10):
    f, ax = plt.subplots(figsize=(7, 7))
    ax.set(yscale="log")
    for replicate in range(1,6):
        series = "S0{}_R0{}".format(sampleGroup,replicate)
        print(series)
        sns.distplot(wideInt[series], hist=False, ax=ax)
    plt.xlabel("Intensity")
    plt.ylabel("Relative Frequency")
    f.savefig("scoredist_0{}.png".format(sampleGroup))
plt.show()
