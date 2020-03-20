#!/usr/bin/env python3

#### Extracting data from data frames ####

#### Objectives ####

# review previous week's objectives
# Today:
#   conditional subsetting
#   grouping data
#   visualizing data with pandas
#   dealing with missing data

#### Getting set up ####

# make sure folks are working in project directory with data/

# load pandas library
import pandas as pd

# read in data
clinical_df = pd.read_csv("data/clinical.csv") # import data as csv file
# inspect output
clinical_df.head()
len(clinical_df)

# Sometimes when reading in a long df it gets tricky to remember each column name and where it is by index.
# You might also want to rename a bunch of columns at some point. To help you remember index and assist in renaming columns 
# you can use a dictionary comprehension from Week 1 to create a dictionary view of the data:

col_mapping_dict = {c[0]:c[1] for c in enumerate(clinical_df.columns)}
print(col_mapping_dict)

#### Conditional subsetting ####

# motivation: extracting data based on criteria

# what samples are from patients born in 1930?
clinical_df.year_of_birth == 1930
# double equal signs to differentiate from variable assignment and parameter specification
# this gives true/false results

# conditional subsetting: all patients born in 1930
clinical_df[clinical_df.year_of_birth == 1930]

# all patients NOT born in 1930
clinical_df[clinical_df.year_of_birth != 1930]
# inverting the true/false results

# combining criteria: AND
clinical_df[(clinical_df.year_of_birth >= 1930) & (clinical_df.year_of_birth <= 1940)]

# combining subsetting: OR
clinical_df[(clinical_df.year_of_birth == 1930) | (clinical_df.year_of_birth == 1931)]

## Challenge: print to the screen all data from clinical_df for patients with
# stage ia tumors who live more than 365 days

#### Grouping ####

# motivation: evaluting data available for a variable (column of categorical data)

# what categories exist for race?
# identify number of unique elements in a column
pd.unique(clinical_df["race"])
pd.unique(clinical_df.race) # same as above, specifying column differently

# how can we summarize data by category?
# group data by race (object isn't interpretable by us)
grouped_data = clinical_df.groupby("race")
# note: we can't specify race as an attribute here because of the syntax of the method groupby

# summary stats for all columns by race
grouped_data.describe()
# only summarizes for quantitative variables, gives summary stats for each column grouped by race

# summary stats for race for only one column (race)
grouped_data.race.describe()

# show the number of patients for each race available for all columns (only one summary stat from above)
grouped_data.count()
# for only one column
grouped_data.race.count()

# count the number of each race for which days to death data is available
grouped_data.days_to_death.count()
# how does this differ from the last command?

# only display one race (asian), from days_to_death grouped by race
grouped_data.days_to_death.count().asian
# remember this is synonymous with:
clinical_df.groupby("race")["days_to_death"].count()["asian"]
# this second command differs because of the data object (clinical_df) and the syntax for identifying columns

# save output to object for later use
race_counts = grouped_data.days_to_death.count()
print(race_counts) # see script-friendly output

## Challenge: Write code that will display:
# the number of patients in this dataset who are listed as alive

#### Visualizing data with pandas ####

# Make sure figures appear inline in some interfaces
%matplotlib inline
# can also use plt.show()

# Create a quick bar chart of number of patients with race known
race_counts.plot(kind="bar");
# the semicolon suppresses the output, allowing the plot to show

## BREAK

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

# look for missing data in a single column
birth_replace[pd.isnull(birth_replace.year_of_birth)]
# fill missing values with 0 (this makes an obvious change we'll be able to track visually)
birth_replace.year_of_birth = birth_replace.year_of_birth.fillna(0)

# filling with 0 gives different answer for mean! not a good approach for work where summary stats matter later in the analysis
birth_replace.year_of_birth.mean()
clinical_df.year_of_birth.mean()

# fill NaN with mean for all weight values
birth_replace.year_of_birth = birth_replace.year_of_birth.fillna(birth_replace.year_of_birth.mean())
# this won't do anything since we've already replaced all missing data!

# Optional: can convert between data types, but is difficult without dealing with missing data
# convert the age_at_diagnosis from an float to integer
birth_replace.year_of_birth = birth_replace.year_of_birth.astype("int64")
birth_replace.year_of_birth.dtype
#clinical_df.year_of_birth.astype("int64") # gives error because of missing data

#### Missing data: masking ####

# mask: excluding missing values

# extract all rows values WITHOUT missing data
clinical_df.dropna()
len(clinical_df.dropna())
# filtering for any missing data cuts out a lot of the dataset!

# optional: can also do this with .isnull
clinical_df[-pd.isnull(clinical_df).any(axis=1)] # axis specifies if missing data is removed by rows or columns
len(clinical_df[-pd.isnull(clinical_df).any(axis=1)])

# exclude missing data in only days to death
clinical_df.dropna(subset = ["cigarettes_per_day"])

# assign masked results to new name (masking doesn't interfere with original data)
smoke_complete = clinical_df.dropna(subset = ["cigarettes_per_day"])
# apply additional filter for age at diagnosis
smoke_complete = smoke_complete[smoke_complete.age_at_diagnosis > 0]
# save filtered data to file
smoke_complete.to_csv("data/smoke_complete.csv", index=False) # index=False stops index value from being printed before first column
# this is the first of two datasets we'll use next week!

## use masking to create second dataframe for next week

# reference original data
birth_reduced = clinical_df

## Challenge: filter out missing data for year of birth and vital status
birth_reduced = birth_reduced.dropna(subset = ["year_of_birth", "vital_status"])
# another option:
birth_reduced = birth_reduced[-pd.isnull(birth_reduced.year_of_birth)]
birth_reduced = birth_reduced[-pd.isnull(birth_reduced.vital_status)]

# check to see that it worked
pd.unique(birth_reduced.vital_status)
## Challenge: remove "not reported" from vital status
birth_reduced = birth_reduced[birth_reduced.vital_status != "not reported"]
pd.unique(birth_reduced.vital_status)

## count number of samples for each cancer type
# group by disease and count
dis_counts = birth_reduced.groupby("disease").disease.count()
# reset index to default (because of groupby)
dis_counts = dis_counts.reset_index(name="counts")
# keep only diseases with many observations
dis_counts = dis_counts[dis_counts.counts > 500]
# extract values
birth_reduced = birth_reduced[birth_reduced["disease"].isin(dis_counts.disease)]

# write data to csv
birth_reduced.to_csv("data/birth_reduced.csv", index=False)

#### Wrapping up ####

# review objectives
# preview next week's objectives
# check install for next week: import plotnine as p9
# demo use of Atom + Hydrogen to code in Python
