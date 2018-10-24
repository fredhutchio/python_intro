#!/usr/bin/env python3

#### Extracting data from data frames ####

#### Objectives ####

# review previous week's objectives
# Today:
#   conditional subsetting
#   grouping data
#   visualizing data with matplotlib
#   dealing with missing data

#### Getting set up ####

# make sure folks are working in project directory with data/

# Make sure pandas is loaded
import pandas as pd

# read in data
clinical_df = pd.read_csv("data/clinical.csv") # import data as csv file
# inspect output
clinical_df.head()
len(clinical_df)

#### Conditional subsetting ####

# conditional subsetting: extracting data based on criteria

# what samples are from patients born in 1930?
clinical_df.year_of_birth == 1930
# this gives true/false results

# conditional subsetting: all patients born in 1930
clinical_df[clinical_df.year_of_birth == 1930]

# all patients NOT born in 1930
clinical_df[clinical_df.year_of_birth != 1930]

# combining criteria: AND
clinical_df[(clinical_df.year_of_birth >= 1930) & (clinical_df.year_of_birth <= 1940)]

# combining subsetting: OR
clinical_df[(clinical_df.year_of_birth == 1930) | (clinical_df.year_of_birth == 1931)]

## Challenge: print to the screen all data from clinical_df for patients with
# stage ia tumors who live more than 365 days

#### Grouping ####

# group data by disease (object isn't interpretable by us)
grouped_data = clinical_df.groupby("race")

# summary stats for all columns by disease
grouped_data.describe()

# extract summary data from one of the columns for race
grouped_data.age_at_diagnosis.describe()

# identify number of unique elements in a column
pd.unique(clinical_df["race"])

# Count the number of each race
grouped_data.count()

# extract only the race column from the previous output
grouped_data["race"].count()

# count the number of each race for which days to death data is available
grouped_data["days_to_death"].count()

# only display one race
grouped_data["days_to_death"].count()["asian"]
# remember this is synonymous with:
clinical_df.groupby("race")["days_to_death"].count()["asian"]

# save output to object for later use
race_counts = grouped_data["days_to_death"].count()
print(race_counts) # see script-friendly output

## Challenge: Write code that will display:
# the number of patients in this dataset who are listed as alive

#### Visualizing data with matplotlib ####

# Make sure figures appear inline in notebook
%matplotlib inline

# Create a quick bar chart of number of patients with race known
race_counts.plot(kind="bar");
# the semicolon suppresses the output, allowing the plot to show

## Challenge:
# create a new object called total_count that counts the number of samples for each cancer type (disease)
total_count = clinical_df.groupby("disease")["disease"].count()
total_count = clinical_df.groupby("disease").disease.count() # same as above
# plot the number of samples for each cancer type
total_count.plot(kind="bar");

#### Missing data: replacing data in copied df ####

## replace missing data in copied data frame

# create new copy of data frame
birth_replace = clinical_df.copy()

# look for missing data
birth_replace[pd.isnull(birth_replace["year_of_birth"])]
# fill missing values with 0
birth_replace["year_of_birth"] = birth_replace["year_of_birth"].fillna(0)

# filling with 0 gives different answer!
birth_replace["year_of_birth"].mean()
clinical_df["year_of_birth"].mean()

# fill NaN with mean for all weight values
birth_replace["year_of_birth"] = birth_replace["year_of_birth"].fillna(birth_replace["year_of_birth"].mean())
# this won't do anything since we've already replaced all missing data!

# can convert between data types, but is difficult without dealing with missing data
# convert the age_at_diagnosis from an float to integer
birth_replace["year_of_birth"] = birth_replace["year_of_birth"].astype("int64")
birth_replace["year_of_birth"].dtype
#clinical_df["year_of_birth"].dtype # gives error

#### Missing data: masking ####

# mask: excluding missing values

# check for missing data anywhere in dataset
pd.isnull(clinical_df)
# gives true/false matrix
# other options include pd.isna (alias of pd.isnull) and pd.notna (removes missing data)

# extract all rows values WITHOUT missing data
clinical_df[-pd.isnull(clinical_df).any(axis=1)]
len(clinical_df[-pd.isnull(clinical_df).any(axis=1)])
# another way to extract rows WITHOUT missing data
clinical_df.dropna() # yet another way
len(clinical_df.dropna())
# filtering for any missing data cuts out a lot of the dataset!

# exclude missing data in only days to death
clinical_df[-pd.isnull(clinical_df["cigarettes_per_day"])]
clinical_df.dropna(subset = ["cigarettes_per_day"])

# save masked results to new object
smoke_complete = clinical_df.dropna(subset = ["cigarettes_per_day"])
# apply additional filter for age at diagnosis
smoke_complete = smoke_complete[smoke_complete.age_at_diagnosis > 0]
# save filtered data to file
smoke_complete.to_csv("data/smoke_complete.csv", index=False)
# this is the first of two datasets we'll use next week!

## use masking to create second dataframe for next week

# reference original data
birth_reduced = clinical_df

## Challenge: filter out missing data for year of birth and vital status
birth_reduced = birth_reduced.dropna(subset = ["year_of_birth", "vital_status"])

birth_reduced = birth_reduced[-pd.isnull(birth_reduced["year_of_birth"])]
birth_reduced = birth_reduced[-pd.isnull(birth_reduced["vital_status"])]

# check to see that it worked
pd.unique(birth_reduced["vital_status"])
## Challenge: remove "not reported" from vital status
birth_reduced = birth_reduced[birth_reduced.vital_status != "not reported"]
pd.unique(birth_reduced["vital_status"])

# count number of samples for each cancer type
birth_reduced.groupby("disease").count()

# create list of desired values
dis_list = ["LGG", "UCEC", "GBM", "LUSC", "BRCA"]
# extract values
birth_reduced = birth_reduced[birth_reduced["disease"].isin(dis_list)]

# write data to csv
birth_reduced.to_csv("data/birth_reduced.csv", index=False)

#### Wrapping up ####

# review objectives
# preview next week's objectives
# check install for next week: import plotnine as p9
# demo use of Atom + Hydrogen to code in Python
