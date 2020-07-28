# Intro to Python
# Class 2 Solutions

## Challenge-import

Download, import, and inspect the following data files. The URL for each sample dataset is included along with a name to assign to the variable. (Hint: you can use the same function as above, but may need to update the `sep =` argument)

Example 1:
```python
urllib.request.urlretrieve("https://raw.githubusercontent.com/fredhutchio/R_intro/master/extra/clinical.tsv", "data/clinical.tsv")
example1 = pd.read_csv("../data/clinical.tsv", sep="\t")
```

Example2:
```python
urllib.request.urlretrieve("https://raw.githubusercontent.com/fredhutchio/R_intro/master/extra/clinical.txt", "data/clinical.txt")
example2 = pd.read_csv("../data/clinical.txt", sep=" ")
```

## Challenge-typo

What happens if you misspell the name of a column?

If you have a typo in a column name,
like `clinical_df.tumorstage`,
the result is  `KeyError: tumorstage`,
found at the bottom of the TraceBack.
This is cryptic until you understand that the "Key" is the column name!

## Challenge-order

Does the order of the columns you list matter?

If you reverse the order of the columns,
`clinical_df[["vital_status", "tumor_stage"]]`,
they return results in a different order.
This means that columns don't have to be entered in same order as original data,
but the order of columns listed will affect order in the output.

## Challenge-last

How would you extract the last 10 rows of the dataset?

There are multiple solutions.
```python
clinical_df[-10:]
```

## Challenge-location

Why doesn't the following code work?
```python
clinical_df.loc[2, 6]
```

The numbers are being interpreted as labels,
and there are no labels with those names.

One possible solution:
```python
clinical_df.iloc[2, 6]
```

However, it's not not clear what the intention was behind the code,
so it's not really possible to correct it!

## Challenge-100

How would you extract the last 100 rows for only vital status and days to death?

Two options:
```python
clinical_df.loc[6732:, ["vital_status", "days_to_death"]]
clinical_df.iloc[-100:, [3,5]]
```

## Challenge-object

What type of summary stats do you get for object data?

Try this on any of the columns of type "object":
```python
clinical_df.site_of_resection_or_biopsy.describe()
```

In the output,
the object (categorical) data are described with:
- count: total observations
- unique: number of categories
- top: most frequently occurring category
- freq: number of observations in the most frequently occurring category

## Challenge-deviation

How would you extract only the standard deviation for days to death?

```python
clinical_df.days_to_death.std()
```

## Challenge-ref

How and why are the following three objects different?

This challenge is a bit easier to assess if you print only a portion of the objects using  `head`:

- `clinical_df.head()` has been modified because `ref_clinical_df` referenced it
- `ref_clinical_df.head()` was directly altered in our code
- `true_copy_clinical_df.head()` is the copy of original, and remains unaltered
