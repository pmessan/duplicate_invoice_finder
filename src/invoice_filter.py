import pandas as pd


# read the data
data = pd.read_csv("../data/joined_dataset_final.csv")

data["unique_id"] = ( data["WRBTR"].astype("str") + data["BUKRS"].astype("str") + data["BLDAT"] + data["XBLNR"] )
# print(data["unique_id"].shape)
# data.to_csv("data/unique_id.csv")
# print(data["unique_id"].shape)

masterList = []     # store the different unique ids

for r in data["unique_id"]:
    if r not in masterList:
        masterList.append(str(r))


# print(len(masterList))

for i in masterList:
    print(masterList.index(i))
    basket = data.loc[data["unique_id"] == i]
    print(basket)
    input()
    # if basket.shape[1] > 1:
    #     print("Duplicates found!")
    # else:
    #     print("No duplicates found!")
    
    



# df.filter(like='bbi', axis=0)

"""
#Python program to remove duplicate elements in an array


def remove_duplicate_elements(arr, n):

if n == 0 or n == 1:
return n

temp = list(range(n))

j = 0;
for i in range(0, n-1):

if arr[i] != arr[i+1]:
temp[j] = arr[i]
j += 1

temp[j] = arr[n-1]
j += 1

for i in range(0, j):
arr[i] = temp[i]

return j


n = int(input())
sum = 0
arr = []
for i in range(0,n):
temp = int(input())
arr.append(temp)
n = remove_duplicate_elements(arr,n)
print(“Array after removing : “,end = “”)
for i in range(0,n):
print(arr[i], end = ” “)
"""