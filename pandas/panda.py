# Dataframe: A 2D table of data, like excel sheet or SQL table
# In panadas it is the main DS to store and manage tabular data


# %%
import pandas as pd

df = pd.read_csv('./telco_churn.csv')

df.tail()

# %%
tempDict = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
dictdf = pd.DataFrame.from_dict(tempDict)

dictdf.head()

# %%
df.columns
# %%
df.dtypes
# %%
df.describe()

# %%
df.describe(include="object")
# %%
