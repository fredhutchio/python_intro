#!/usr/bin/env python3

#### Starting with data ####

#### Before class ####

# share URL to hack.md with link to zipped dataset file to download

#### Objectives ####

# review previous week's objectives
# Today:
#   using packages
#   tidy data and importing data to python
#   selecting data using labels (columns) and rows
#   slicing subsets of rows and columns
#   calculating summary statistics

#### Using packages ####

# make sure everyone is working in project directory
# create new notebook for this week's material

# defining packages
#   collection of functions
#   community contributed
# describe pandas
#   python data analysis library

# make pandas available to use in this notebook
import pandas as pd

#### Importing data ####

# show where to download data
# emphasize unzipping directory and moving data to appropriate location

# import data as csv
pd.read_csv("data/clinical.csv")
# this only prints it to the screen!

# appropriate composition of data into tables still isn't commonly taught!
# overview of tidy data principles
#   columns: variables
#   rows: observations
#   one piece of info per cell
# csv: comma separated values (other things besides commas can have separators too though)
# describe data and where it came from

# assign data to object
clinical_df = pd.read_csv("data/clinical.csv")

# preview data import
clinical_df.head() # print top few rows

## Challenge: What do you need to do to import the following files correctly:
#clinical.tsv
#clinical.txt

# examine data import
type(clinical_df) # look at data type
clinical_df.columns # view column names
clinical_df.dtypes # look at type of data in each column

# numeric and text data types
# Int64 stands for 64 bit integer

# text data type: pandas vs native python
# object = string
# int64 = int
# float64 = float
# datetime64 = N/A

#### Selecting data using labels (columns) and row ranges ####

# select a 'subset' of the data using the column name
clinical_df['tumor_stage']
clinical_df['tumor_stage'].dtype # single column, O stands for "object"

# use the column name as an 'attribute'; gives the same output
clinical_df.tumor_stage

# What happens if you ask for a column that doesn't exist?
#clinical_df['tumorstage']

# Select two columns at once
clinical_df[['tumor_stage', 'vital_status']]

## Challenge: does the order of the columns you list matter?

# Select rows 0, 1, 2 (row 3 is not selected)
clinical_df[0:3]

# Select row 2 to the end
clinical_df[1:]

# Select the last element in the list
clinical_df[-1:] # what does this mean in the context of indexing?

## Challenge: how would you extract the last 10 rows of the dataset?

#### Copying vs referencing objects ####

# Using the '=' operator references the previous object
ref_clinical_df = clinical_df

# Using the 'copy() method': actually creates another object
true_copy_clinical_df = clinical_df.copy()

# Assign the value `0` to the first three rows of data in the DataFrame
ref_clinical_df[0:3] = 0

## Challenge: How and why are the following three objects different?
# Hint: try applying head()
clinical_df.head() # has been modified because ref_clinical_df referenced it
ref_clinical_df.head() # was actually altered
true_copy_clinical_df.head() # actual copy of original, unaltered
# reinforce that the order of operations matters!

# re-load fresh copy of object
clinical_df = pd.read_csv("data/clinical.csv")

#### Slicing subsets of rows and columns ####

# iloc is integer indexing [row slicing, column slicing]
# locate specific data element
clinical_df.iloc[2, 6]

# select range of data
clinical_df.iloc[0:3, 1:4]
# select rows 0, 1, 2; up to but not including 3
# select rows 1, 2, 3; up to but not including 4

# loc is for label indexing (integers interpreted as labels)
# start and stop bound are inclusive
clinical_df.loc[0: ]

# Select all columns for rows of index values specified
clinical_df.loc[[0, 10, 6831], :]

# select all rows for specified columns
clinical_df.loc[0, ['primary_diagnosis', 'tumor_stage', 'age_at_diagnosis']]

## Challenge: why doesn't the following code work?
#clinical_df.loc[2, 6]

## Challenge: how would you extract the last 100 rows for only vital status and days to death?

#### Calculating summary statistics ####

# calculate basic stats for all records in single column
clinical_df['age_at_diagnosis'].describe()

# each metric one at a time (only prints last if all executed in one cell!)
clinical_df['age_at_diagnosis'].min()

# convert columns
clinical_df['age_at_diagnosis']/365

## Challenge: How would you extract only the standard deviation for days to death?

#### Wrapping up ####

# review objectives
# preview next week's objectives
