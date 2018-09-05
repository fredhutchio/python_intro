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
pd.read_csv("data/surveys.csv")
# this only prints it to the screen!

# assign data to object
surveys_df = pd.read_csv("data/surveys.csv")

# inspect data import
surveys_df.head() # print top few rows
type(surveys_df) # look at data type
surveys_df.columns # view column names
surveys_df.dtypes # look at type of data in each column
surveys_df['sex'].dtype # single type; O stands for object/string

# numeric and text data types
# Int64 stands for 64 bit integer

# text data type: pandas vs native python
# object = string
# int64 = int
# float64 = float
# datetime64 = N/A

# examine data type

# Convert the record_id field from an integer to a float
surveys_df['record_id'] = surveys_df['record_id'].astype('float64')
surveys_df['record_id'].dtype

#### Inspecting and summarizing data ####

pd.unique(surveys_df['species_id'])

# calculate basic stats for all records in single column
surveys_df['weight'].describe()

# each metric one at a time (only prints last if all exectuted in one cell!)
surveys_df['weight'].min()
surveys_df['weight'].max()
surveys_df['weight'].mean()
surveys_df['weight'].std()
surveys_df['weight'].count()

# Group data by sex
grouped_data = surveys_df.groupby('sex')

# Summary statistics for all numeric columns by sex
grouped_data.describe()
# Provide the mean for each numeric column by sex
grouped_data.mean()

# Count the number of samples by species
species_counts = surveys_df.groupby('species_id')['record_id'].count()
print(species_counts)

# count only rows with species "DO"
surveys_df.groupby('species_id')['record_id'].count()['DO']

# Multiply all weight values by 2
surveys_df['weight']*2

#### Visualizing data ####

# Make sure figures appear inline in Ipython Notebook
%matplotlib inline
# Create a quick bar chart
species_counts.plot(kind='bar');

total_count = surveys_df.groupby('plot_id')['record_id'].nunique()
# Let's plot that too
total_count.plot(kind='bar');

#### Wrapping up ####

# review objectives
# preview next week's objectives
