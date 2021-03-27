import pandas as pd

# read the data
data = pd.read_csv("../data/joined_dataset_final.csv")

# create a unique identifier made of the 4 fields which duplicates have in common
data["unique_id"] = ( data["WRBTR"].astype("str") + data["BUKRS"].astype("str") + data["BLDAT"] + data["XBLNR"] )

# data storage containers
masterList = []
duplicateIDs = []
dataFrames = []

# Build a master list of what we have seen as we go along
# Aim to iterate just once through the file

for i, row in data.iterrows():
    if row["unique_id"] not in masterList:                  # if there's new entry, add to our 'seen' list
        masterList.append(row["unique_id"]) 
    else:                                                   # if the entry's already there, we filter it out
        duplicateIDs.append(row["unique_id"])

for i in duplicateIDs:                                      # use found duplicate IDs to pick out matching invoices
    dataFrames.append(data.loc[data["unique_id"] == i])

# save the found duplicates to CSV
dataFrames = pd.concat(dataFrames)
dataFrames.to_csv("../data/duplicates.csv")
