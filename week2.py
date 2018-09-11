#!/usr/bin/env python3

#### Starting with data ####

#### Before class ####

# share URL to hack.md with link to dataset to download

#### Objectives ####

# review previous week's objectives
# Today:
#   principles of tidy data
#   importing data using python
#   subsetting data
#   selecting columns

#### Using packages ####

# defining packages
#   collection of functions
#   community contributed
# describe pandas
#   python data analysis library

# make pandas available to use in this notebook
import pandas as pd

#### Importing data ####

# appropriate composition of data into tables still isn't commonly taught!
# overview of tidy data principles
#   columns: variables
#   rows: observations
#   one piece of info per cell
# csv: comma separated values (other things besides commas can have separators too though)
# describe data and where it came from

# import data as csv
pd.read_csv("data/clinical.csv")
# this only prints it to the screen!

# assign data to object
clinical_df = pd.read_csv("data/clinical.csv")

# preview data import
clinical_df.head() # print top few rows

## Challenge: import of clinical.txt and clinical.tsv

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

#### Subsetting data ####

# Select rows 0, 1, 2 (row 3 is not selected)
clinical_df[0:3]

# Select the first 5 rows (rows 0, 1, 2, 3, 4)
clinical_df[:5]

# Select the last element in the list
# (the slice starts at the last element, and ends at the end of the list)
clinical_df[-1:]

# copying objects is different than referencing
# Using the 'copy() method': actually creates another object
true_copy_clinical_df = clinical_df.copy()

# Using the '=' operator only references the previous object
ref_clinical_df = clinical_df

# Assign the value `0` to the first three rows of data in the DataFrame
ref_clinical_df[0:3] = 0

## Challenge: what happens to the following two data frames?

# ref_clinical_df was created using the '=' operator
ref_clinical_df.head()

# clinical_df is the original dataframe
clinical_df.head()

# slicing subsets of rows and columns

# iloc[row slicing, column slicing]
clinical_df.iloc[0:3, 1:4]

# Select all columns for rows of index values 0 and 10
clinical_df.loc[[0, 10], :]

# What happens when you type the code below?
clinical_df.loc[[0, 10, 35549], :]

# locate specific data element
clinical_df.iloc[2, 6]

#### Selecting data using labels ####

# select data using labels: two ways
# Method 1: select a 'subset' of the data using the column name
clinical_df['tumor_stage']
clinical_df['primary_diagnosis'].dtype # single column, O stands for "object"

# Method 2: use the column name as an 'attribute'; gives the same output
clinical_df.tumor_stage

# save `tumor_stage` column to object
clinical_species = clinical_df['tumor_stage']

# Select two columns from the DataFrame
clinical_df[['tumor_stage', 'vital_status']]

# What happens when you flip the order?
clinical_df[['vital_status', 'tumor_stage']]

# What happens if you ask for a column that doesn't exist?
#clinical_df['tumorstage']

# calculate basic stats for all records in single column
clinical_df['age_at_diagnosis'].describe()

# each metric one at a time (only prints last if all executed in one cell!)
clinical_df['age_at_diagnosis'].min()
clinical_df['age_at_diagnosis'].max()
clinical_df['age_at_diagnosis'].mean()
clinical_df['age_at_diagnosis'].std()
clinical_df['age_at_diagnosis'].count()

#### Wrapping up ####

# review objectives
# preview next week's objectives
