# Dataframe: A 2D table of data, like excel sheet or SQL table
# In panadas it is the main DS to store and manage tabular data


# %%
import pandas as pd

df = pd.read_csv('./telco_churn.csv')

## READ--------------------------------------------

# Show top and bottom 5 rows
# %%
df.head()

#%%
df.tail()

# %%
tempDict = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
dictdf = pd.DataFrame.from_dict(tempDict)

dictdf.head()

# Show coulmns and data types
# %%
df.columns
# %%
df.dtypes

# Create summary statistics
# %%
df.describe()

# %%
df.describe(include="object")

# Filter on columns
# %%
df[["State", "International plan"]]

# %%
df.Churn.unique()

# Filter on rows
# %%
df[df['International plan']=='Yes']
# %%
df[(df['International plan']=='Yes') & (df['Churn']==False)]

# Indexing with iloc [row, column]

#%%
df.iloc[14]
# %%
df.iloc[14, 0]
# segment of our df
# %%
df.iloc[22:33]

# Indexing with loc
#%%
state = df.copy()
state.set_index('State', inplace=True)
# state.head()
state.loc['OH']



### UPDATE--------------------
#%%
df.isnull().sum()

# Drop rows with missing values
#%%
df.dropna(inplace=True)

# Drop Column
# %%
df.drop("Voice mail plan", axis=1)

# Add new Column
#%%
df['New column'] = df['Total day minutes'] + df['Total intl minutes']

#%%
df.head()

# Updating a single value
#%%
df.iloc[0, 0] = 'BS'

#%%
df['Churn Binary'] = df['Churn'].apply(lambda x: 1 if x==True else 0)
# %%
df[df['Churn'] == True].head()



## DELETE/Output ---------------------------------

#%%
# Output to CSV
df.to_csv('output.csv')

 #%%
json=df.to_json()
print(json)

#%%
df.to_html()

# Delet a dataframe
#%%
del df


#%%
df.head()