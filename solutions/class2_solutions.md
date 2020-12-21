# Intro to Python, Class 2 Solutions

#### Challenge-import

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

#### Challenge-typo

If you have a typo in a column name,
like `clinical_df.tumorstage`,
the result is  `KeyError: tumorstage`,
found at the bottom of the TraceBack.
This is cryptic until you understand that the "Key" is the column name!

#### Challenge-order

If you reverse the order of the columns,
`clinical_df[["vital_status", "tumor_stage"]]`,
they return results in a different order.
This means that columns don't have to be entered in same order as original data,
but the order of columns listed will affect order in the output.

#### Challenge-last

There are multiple solutions.
```python
clinical_df[-10:]
```

#### Challenge-location

The numbers are being interpreted as labels,
and there are no labels with those names.

One possible solution:
```python
clinical_df.iloc[2, 6]
```

However, it's not not clear what the intention was behind the code,
so it's not really possible to correct it!

#### Challenge-100

Two options:
```python
clinical_df.loc[6732:, ["vital_status", "days_to_death"]]
clinical_df.iloc[-100:, [3,5]]
```

#### Challenge-object

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

#### Challenge-deviation

```python
clinical_df.days_to_death.std()
```

#### Challenge-ref

This challenge is a bit easier to assess if you print only a portion of the objects using  `head`:

- `clinical_df.head()` has been modified because `ref_clinical_df` referenced it
- `ref_clinical_df.head()` was directly altered in our code
- `true_copy_clinical_df.head()` is the copy of original, and remains unaltered
