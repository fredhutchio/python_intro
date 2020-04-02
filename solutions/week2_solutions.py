#### Intro to Python: class 2 exercises ####

# Starting with data

# Objectives:
#   using packages
#   tidy data and importing data to python
#   selecting data using labels (columns) and rows
#   slicing subsets of rows and columns
#   calculating summary statistics

#### In-class exercises ####

## Challenge: What do you need to do to download and import the following files correctly:
# example1: https://raw.githubusercontent.com/fredhutchio/R_intro/master/extra/clinical.tsv
urllib.request.urlretrieve("https://raw.githubusercontent.com/fredhutchio/R_intro/master/extra/clinical.tsv", "data/clinical.tsv")
example1 = pd.read_csv("../data/clinical.tsv", sep="\t")
# example2: https://raw.githubusercontent.com/fredhutchio/R_intro/master/extra/clinical.txt
urllib.request.urlretrieve("https://raw.githubusercontent.com/fredhutchio/R_intro/master/extra/clinical.txt", "data/clinical.txt")
example2 = pd.read_csv("../data/clinical.txt", sep=" ")

## Challenge:
# what happens if you misspell the name of a column?
#clinical_df["tumorstage"] # KeyError: tumorstage (at bottom of TraceBack)

## Challenge: does the order of the columns you list matter?
clinical_df[["vital_status", "tumor_stage"]]
# columns don't have to be entered in same order as original data
# order of columns listed will affect order in output

## Challenge: how would you extract the last 10 rows of the dataset?
clinical_df[-10:]

## Challenge: How and why are the following three objects different?
# Hint: try applying head()
clinical_df.head() # has been modified because ref_clinical_df referenced it
ref_clinical_df.head() # was actually altered
true_copy_clinical_df.head() # actual copy of original, unaltered

## Challenge: why doesn't the following code work?
#clinical_df.loc[2, 6] # numbers are interpreted as labels
clinical_df.iloc[2, 6] # one possible solution, but not clear what was intended!

## Challenge: how would you extract the last 100 rows for only vital status and days to death?
clinical_df.loc[6732:, ["vital_status", "days_to_death"]]
clinical_df.iloc[-100:, [3,5]]

## Challenge: What type of summary stats do you get for object data?
clinical_df["site_of_resection_or_biopsy"].describe()

## Challenge: How would you extract only the standard deviation for days to death?
clinical_df["days_to_death"].std()

#### Extra exercises ####
