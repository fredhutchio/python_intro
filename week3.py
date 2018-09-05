#!/usr/bin/env python3

#### Extracting data from data frames ####

#### Objectives ####

# Today:
# import dataset
# operators, functions, and data types
# sequences and dictionaries
# defining functions

#### Getting set up ####

# Make sure pandas is loaded
import pandas as pd

# Read in the survey CSV
surveys_df = pd.read_csv("data/surveys.csv")

#### Selecting data using labels ####

# select data using labels: two ways
# Method 1: select a 'subset' of the data using the column name
surveys_df['species_id']

# Method 2: use the column name as an 'attribute'; gives the same output
surveys_df.species_id

# save `species_id` column to object
surveys_species = surveys_df['species_id']

# Select the species and plot columns from the DataFrame
surveys_df[['species_id', 'plot_id']]

# What happens when you flip the order?
surveys_df[['plot_id', 'species_id']]

# What happens if you ask for a column that doesn't exist?
#surveys_df['speciess']

# slicing rows
# Select rows 0, 1, 2 (row 3 is not selected)
surveys_df[0:3]

# Select the first 5 rows (rows 0, 1, 2, 3, 4)
surveys_df[:5]

# Select the last element in the list
# (the slice starts at the last element, and ends at the end of the list)
surveys_df[-1:]

# copying objects is different than referencing
# Using the 'copy() method': actually creates another object
true_copy_surveys_df = surveys_df.copy()

# Using the '=' operator only references the previous object
ref_surveys_df = surveys_df

# Assign the value `0` to the first three rows of data in the DataFrame
ref_surveys_df[0:3] = 0

# what happens to the following two data frames?

# ref_surveys_df was created using the '=' operator
ref_surveys_df.head()

# surveys_df is the original dataframe
surveys_df.head()

# slicing subsets of rows and columns

# iloc[row slicing, column slicing]
surveys_df.iloc[0:3, 1:4]

# Select all columns for rows of index values 0 and 10
surveys_df.loc[[0, 10], :]

# What does this do?
surveys_df.loc[0, ['species_id', 'plot_id', 'weight']]

# What happens when you type the code below?
surveys_df.loc[[0, 10, 35549], :]

# locate specific data element
surveys_df.iloc[2, 6]

# conditional subsetting (using a criteria)
surveys_df[surveys_df.year == 2002]

# not containing
surveys_df[surveys_df.year != 2002]

# sets of criteria
surveys_df[(surveys_df.year >= 1980) & (surveys_df.year <= 1985)]

# isin function to find list of values
#surveys_df[surveys_df['species_id'].isin([listGoesHere])]

# check for missing data
pd.isnull(surveys_df)

# To select just the rows with NaN values, we can use the 'any()' method
surveys_df[pd.isnull(surveys_df).any(axis=1)]

# What does this do?
empty_weights = surveys_df[pd.isnull(surveys_df['weight'])]['weight']
print(empty_weights)

len(surveys_df[pd.isnull(surveys_df.weight)])
# How many rows have weight values?
len(surveys_df[surveys_df.weight> 0])

df1 = surveys_df.copy()
# Fill all NaN values with 0
df1['weight'] = df1['weight'].fillna(0)

# filling with 0 gives different answer!
df1['weight'].mean()

# fill NaN with mean for all weight values
df1['weight'] = surveys_df['weight'].fillna(surveys_df['weight'].mean())

# write data to csv
surveys_df = pd.read_csv("data/surveys.csv")

# exclude any observation with missing data
df_na = surveys_df.dropna()

# Write DataFrame to CSV
df_na.to_csv('data/surveys_complete.csv', index=False)

#### Wrapping up ####

# review objectives
# preview next week's objectives
