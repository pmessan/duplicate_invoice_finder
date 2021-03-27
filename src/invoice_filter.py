import pandas as pd


# read the data
data = pd.read_csv("../data/joined_dataset_final.csv")

data["unique_id"] = ( data["WRBTR"].astype("str") + data["BUKRS"].astype("str") + data["BLDAT"] + data["XBLNR"] )
# print(data["unique_id"].shape)
# data.to_csv("data/unique_id.csv")
# print(data.iloc[0:5, 53])
# print(data.head())

# sub_data = data.iloc[0:30]

masterList = []
duplicatesList = []

for i, row in data.iterrows():
    # print("Index: ", i)
    if row["unique_id"] not in masterList:
        masterList.append(row["unique_id"])
    else:   #if it's already there, we filter it out
        duplicatesList.append(row)
        
print("Duplicates found: ", len(duplicatesList))
# print(duplicatesList)

clms = list(data.columns)

df = pd.DataFrame(columns=clms)
for i in range(len(duplicatesList)):
    df.loc[i] = duplicatesList[i]

df.to_excel("../data/duplicates.xlsx")

print(df.head(8))