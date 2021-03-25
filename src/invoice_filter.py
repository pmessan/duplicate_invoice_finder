import pandas as pd


# read the data
data = pd.read_csv("data/joined_dataset_final.csv")

data["unique_id"] = ( data["WRBTR"].astype("str") + data["BUKRS"].astype("str") + data["BLDAT"] + data["XBLNR"] )
# print(data["unique_id"].shape)
# data.to_csv("data/unique_id.csv")
print(data["unique_id"])
