#!/usr/bin/env python3

#### Extracting data from data frames ####

#### Objectives ####

# Today:
# selecting data using labels
# summarizing data
# sequences and dictionaries
# defining functions

#### Getting set up ####

# Make sure pandas is loaded
import pandas as pd

# Read in the survey CSV
clinical_df = pd.read_csv("data/clinical.csv") # import data as csv file

# What does this do?
clinical_df.loc[0, ['species_id', 'plot_id', 'weight']]

# conditional subsetting (using a criteria)
clinical_df[clinical_df.year == 2002]

# not containing
clinical_df[clinical_df.year != 2002]

# sets of criteria
clinical_df[(clinical_df.year >= 1980) & (clinical_df.year <= 1985)]

#### Summarizing data ####

pd.unique(clinical_df['disease'])

# calculate basic stats for all records in single column
clinical_df['age_at_diagnosis'].describe()

# each metric one at a time (only prints last if all executed in one cell!)
clinical_df['age_at_diagnosis'].min()
clinical_df['age_at_diagnosis'].max()
clinical_df['age_at_diagnosis'].mean()
clinical_df['age_at_diagnosis'].std()
clinical_df['age_at_diagnosis'].count()

# Group data by sex
grouped_data = clinical_df.groupby('disease')

# Summary statistics for all numeric columns by disease
grouped_data.describe()
# Provide the mean for each numeric column by disease
grouped_data.mean()

# Count the number of each race by disease
disease_counts = clinical_df.groupby('race')['disease'].count()
print(disease_counts)

# count only rows with species "DO"
clinical_df.groupby('disease')['race'].count()['white']

# convert columns
clinical_df['age_at_diagnosis']/365

#### Visualizing data ####

# Make sure figures appear inline in ipython Notebook
%matplotlib inline
# Create a quick bar chart
disease_counts.plot(kind='bar');

total_count = clinical_df.groupby('disease')['site_of_resection_or_biopsy'].nunique()
# Let's plot that too
total_count.plot(kind='bar');

# isin function to find list of values
#clinical_df[clinical_df['species_id'].isin([listGoesHere])]

# can convert between data types, but is difficult without dealing with missing data
# Convert the record_id field from an float to integer
#clinical_df['age_at_diagnosis'] = clinical_df['age_at_diagnosis'].astype('int64')
#clinical_df['record_id'].dtype

# check for missing data
pd.isnull(clinical_df)

# To select just the rows with NaN values, we can use the 'any()' method
clinical_df[pd.isnull(clinical_df).any(axis=1)]

# What does this do?
empty_weights = clinical_df[pd.isnull(clinical_df['weight'])]['weight']
print(empty_weights)

len(clinical_df[pd.isnull(clinical_df.weight)])
# How many rows have weight values?
len(clinical_df[clinical_df.weight> 0])

df1 = clinical_df.copy()
# Fill all NaN values with 0
df1['weight'] = df1['weight'].fillna(0)

# filling with 0 gives different answer!
df1['weight'].mean()

# fill NaN with mean for all weight values
df1['weight'] = clinical_df['weight'].fillna(clinical_df['weight'].mean())

# write data to csv
clinical_df = pd.read_csv("data/clinical.csv")

# exclude any observation with missing data
df_na = clinical_df.dropna()

# Write DataFrame to CSV
df_na.to_csv('data/clinical_complete.csv', index=False)

#### Wrapping up ####

# review objectives
# preview next week's objectives
