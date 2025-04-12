import pandas as pd

df = pd.read_csv("C:/data analytics projects/abc_pvt_ltd/ABC_pvt_ltd.csv")

# General operations on the Dataset
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

# Stastical computaions
print("statistics of Purchase column is:\n",
      "mean: ", df['Purchase'].mean(), "\n",
      "Median: ", df['Purchase'].median(), "\n ",
      "Mode :", df['Purchase'].mode(), "\n ",
      "Standard Deviation: ", df['Purchase'].std(), "\n ",
      "Variance: ", df['Purchase'].var(),
      "Minimum: ", df['Purchase'].min(),
      "Maximum: ", df['Purchase'].max(),
      "Range: ", df['Purchase'].min() - df['Purchase'].max())

# Replacing the null values
df['Product_Category_2'] = df['Product_Category_2'].fillna(0)
df['Product_Category_3'] = df['Product_Category_3'].fillna(0)

print(df["Age"].value_counts())

# Printing the unique values in each Categorical attribute
print(df.nunique())
print(df['Product_ID'].value_counts())
print(df['Gender'].value_counts())
print(df['Occupation'].value_counts())
print(df['Age'].value_counts())
print(df['Stay_In_Current_City_Years'].value_counts())

# dropping unuseful data "Stay_In_Current_City_Years"
df.drop('Stay_In_Current_City_Years', axis=1, inplace=True)
df.to_csv("data_final.csv", index=False)
