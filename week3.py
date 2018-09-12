#!/usr/bin/env python3

#### Extracting data from data frames ####

#### Objectives ####

# review previous week's objectives
# Today:
#   conditional subsetting, grouping, and manipulating data
#   visualizing data with matplotlib
#   handling missing data
#   saving data to files

#### Getting set up ####

# Make sure pandas is loaded
import pandas as pd

# Read in the survey CSV
clinical_df = pd.read_csv("data/clinical.csv") # import data as csv file

#### Conditional subsetting, grouping, and manipulating data ####

# conditional subsetting (using a criteria)
clinical_df[clinical_df.year_of_birth == 1930]

# not containing
clinical_df[clinical_df.year_of_birth != 1930]

# sets of criteria
clinical_df[(clinical_df.year_of_birth >= 1930) & (clinical_df.year_of_birth <= 1940)]

# identify number of unique elements in a column
pd.unique(clinical_df['disease'])

# Group data by disease
grouped_data = clinical_df.groupby('disease')

# Summary statistics for all numeric columns by disease
grouped_data.describe()

# Count the number of each race
clinical_df.groupby('race').count()

# see script-friendly output
race_counts = clinical_df.groupby('race')['disease'].count()
print(race_counts)

# only display disease column in output
clinical_df.groupby('race')['disease'].count()

# only display one race
clinical_df.groupby('race')['disease'].count()['asian']

## Challenge: Write code that will display:
# the number of patients in this dataset who are listed as alive
# the number of patients with breast cancer (BRCA)

# isin function to find list of values
#clinical_df[clinical_df['species_id'].isin([listGoesHere])]

#### Visualizing data with matplotlib ####

# Make sure figures appear inline in ipython Notebook
%matplotlib inline
# Create a quick bar chart of number of patients with race known
race_counts.plot(kind='bar');

total_count = clinical_df.groupby('disease')['race'].nunique()
# Let's plot that too
total_count.plot(kind='bar');

#### Missing data ####

# check for missing data
pd.isnull(clinical_df)

# To select just the rows with NaN values, we can use the 'any()' method
clinical_df[pd.isnull(clinical_df).any(axis=1)]

# print all missing data in days to death
empty_death = clinical_df[pd.isnull(clinical_df['days_to_death'])]['days_to_death']
print(empty_death)

# count number of observations with missing data
len(clinical_df[pd.isnull(clinical_df.days_to_death)])

# count number of observations with days to death values
len(clinical_df[clinical_df.days_to_death> 0])

# create new copy of data frame to filter for missing data
df1 = clinical_df.copy()

# Fill all NaN values with 0
df1['days_to_death'] = df1['days_to_death'].fillna(0)

# filling with 0 gives different answer!
df1['days_to_death'].mean()
clinical_df['days_to_death'].mean()

# fill NaN with mean for all weight values
df1['days_to_death'] = clinical_df['days_to_death'].fillna(clinical_df['days_to_death'].mean())

# write data to csv
clinical_df = pd.read_csv("data/clinical.csv")

# exclude any observation with missing data
df_na = clinical_df.dropna()

# can convert between data types, but is difficult without dealing with missing data
# Convert the record_id field from an float to integer
#clinical_df['age_at_diagnosis'] = clinical_df['age_at_diagnosis'].astype('int64')
#clinical_df['record_id'].dtype

# Write DataFrame to CSV
df_na.to_csv('data/clinical_complete.csv', index=False)

#### Wrapping up ####

# review objectives
# preview next week's objectives
