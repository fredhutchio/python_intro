#!/usr/bin/env python3

#### Starting with data ####

#### Before class ####

# share URL to hack.md with link to dataset to download

#### Objectives ####

# Today:
# import dataset
# operators, functions, and data types
# sequences and dictionaries
# defining functions

#### Using packages ####

# defining packages
#   collection of functions
#   community contributed
# describe pandas
#   python data analysis library

# make pandas available to use in this notebook
import pandas as pd

#### Importing data ####

# overview of tidy data principles
# appropriate composition of data into tables still isn't commonly taught!
# columns: variables
# rows: observations
# one piece of info per cell
# csv: comma separated values (other things besides commas can have separators too though)
# describe data and where it came from

# import data as csv
pd.read_csv("data/clinical.csv")
# this only prints it to the screen!

# assign data to object
clinical_df = pd.read_csv("data/clinical.csv")

# inspect data import
clinical_df.head() # print top few rows
clinical_head = clinical_df.head()
type(clinical_df) # look at data type
clinical_df.columns # view column names
clinical_df.dtypes # look at type of data in each column
clinical_df['primary_diagnosis'].dtype # single column, O stands for "object"

# numeric and text data types
# Int64 stands for 64 bit integer

# text data type: pandas vs native python
# object = string
# int64 = int
# float64 = float
# datetime64 = N/A

# can convert between data types, but is difficult without dealing with missing data
# Convert the record_id field from an float to integer
#clinical_df['age_at_diagnosis'] = clinical_df['age_at_diagnosis'].astype('int64')
#clinical_df['record_id'].dtype

#### Inspecting and summarizing data ####

pd.unique(clinical_df['disease'])

# calculate basic stats for all records in single column
clinical_df['age_at_diagnosis'].describe()

# each metric one at a time (only prints last if all exectuted in one cell!)
clinical_df['age_at_diagnosis'].min()
clinical_df['age_at_diagnosis'].max()
clinical_df['age_at_diagnosis'].mean()
clinical_df['age_at_diagnosis'].std()
clinical_df['age_at_diagnosis'].count()

# Group data by sex
grouped_data = clinical_df.groupby('disease')

# Summary statistics for all numeric columns by sex
grouped_data.describe()
# Provide the mean for each numeric column by sex
grouped_data.mean()

# Count the number of samples by species
disease_counts = clinical_df.groupby('disease')['race'].count()
print(disease_counts)

# count only rows with species "DO"
clinical_df.groupby('disease')['race'].count()['white']

# convert columns
clinical_df['age_at_diagnosis']/365

#### Visualizing data ####

# Make sure figures appear inline in Ipython Notebook
%matplotlib inline
# Create a quick bar chart
disease_counts.plot(kind='bar');

total_count = clinical_df.groupby('disease')['site_of_resection_or_biopsy'].nunique()
# Let's plot that too
total_count.plot(kind='bar');

#### Wrapping up ####

# review objectives
# preview next week's objectives
