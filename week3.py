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

# make sure folks are working in project directory with data/

# Make sure pandas is loaded
import pandas as pd

# Read in the survey CSV
clinical_df = pd.read_csv("data/clinical.csv") # import data as csv file
# inspect output
clinical_df.head()
len(clinical_df)

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

# only display disease column in output
clinical_df.groupby('race')['disease'].count()

# only display one race
clinical_df.groupby('race')['disease'].count()['asian']

# save output to object for later use
race_counts = clinical_df.groupby('race')['disease'].count()
print(race_counts) # see script-friendly output

## Challenge: Write code that will display:
# the number of patients in this dataset who are listed as alive
# the number of patients with breast cancer (BRCA)

#### Visualizing data with matplotlib ####

# Make sure figures appear inline in notebook
%matplotlib inline

# Create a quick bar chart of number of patients with race known
race_counts.plot(kind='bar');
# the semicolon suppresses the output, allowing the plot to show

## Challenge:
# create a new object called total_count that counts the number of samples for each cancer type
total_count = clinical_df.groupby('disease')['race'].count()
# plot the number of samples for each cancer type
total_count.plot(kind='bar');

#### Missing data ####

# two methods: masking and replacing missing data with zeros

## mask: method of indicating missing values, as with separate array indicating which values to exclude
#   set true/false criteria
#   assess each value in object to see if it meets criteria
#   creates output object that is same shape as original, but with Boolean values
#   masks can be applied to lots of other conditions!

# check for missing data anywhere in dataset
pd.isnull(clinical_df)

# select just the rows with NaN values
clinical_df[pd.isnull(clinical_df).any(axis=1)]
# count how many rows have missing data
len(clinical_df[pd.isna(clinical_df).any(axis=1)])

# How could we extract all values WITHOUT missing data?
clinical_df[-pd.isnull(clinical_df).any(axis=1)]
clinical_df[pd.notna(clinical_df).any(axis=1)] # alternative way of selecting non-missing data
len(clinical_df[-pd.isnull(clinical_df).any(axis=1)])
# filtering for any missing data cuts out a lot of the dataset!

# exclude missing data in only days to death
clinical_df[-pd.isnull(clinical_df['cigarettes_per_day'])]

# save masked results to new object
smoke_complete = clinical_df[-pd.isnull(clinical_df['cigarettes_per_day'])]
# apply additional filter for age at diagnosis
smoke_complete = smoke_complete[smoke_complete.age_at_diagnosis > 0]
# save filtered data to file
smoke_complete.to_csv('data/smoke_complete.csv', index=False)

## replace missing data in copied data frame

birth_reduced
year_of_birth
vital_status (not reported)
frequent diseases


# create new copy of data frame
birth_reduced = clinical_df.copy()

# Fill all NaN values with 0
pd.isna(birth_reduced['year_of_birth']).any(axis=1)
birth_reduced['year_of_birth'] = birth_reduced['age_at_diagnosis'].fillna(0)

# filling with 0 gives different answer!
birth_reduced['days_to_death'].mean()
birth_reduced['days_to_death'].mean()

# fill NaN with mean for all weight values
birth_reduced['days_to_death'] = clinical_df['days_to_death'].fillna(clinical_df['days_to_death'].mean())

# write data to csv
df_na.to_csv('data/clinical_complete.csv', index=False)

# exclude any observation with missing data
df_na = clinical_df.dropna()

# can convert between data types, but is difficult without dealing with missing data
# Convert the record_id field from an float to integer
#clinical_df['age_at_diagnosis'] = clinical_df['age_at_diagnosis'].astype('int64')
#clinical_df['record_id'].dtype

# Write DataFrame to CSV


#### Wrapping up ####

# review objectives
# preview next week's objectives
