# Intro to Python
# Class 3 Solutions

## Challenge-conditionals

Print to the screen all data from clinical_df for patients with stage ia tumors who live more than 365 days

```python
clinical_df[(clinical_df.tumor_stage == "stage ia") & (clinical_df.days_to_death > 365)]
```

## Challenge-combine

Write code that will display the number of patients in this dataset who are listed as alive

```python
clinical_df.groupby("vital_status")["vital_status"].count()["alive"]
```

## Challenge-total-count

Create a new object called `total_count` that counts the number of samples for each cancer type (disease)

```python
total_count = clinical_df.groupby("disease")["disease"].count()
total_count = clinical_df.groupby("disease").disease.count() # same as above
# plot the number of samples for each cancer type
total_count.plot(kind="bar");
```

## Challenge-filter

Filter out missing data for year of birth and vital status

```python
birth_reduced = birth_reduced.dropna(subset = ["year_of_birth", "vital_status"])

birth_reduced = birth_reduced[-pd.isnull(birth_reduced["year_of_birth"])]
birth_reduced = birth_reduced[-pd.isnull(birth_reduced["vital_status"])]

# check to see that it worked
pd.unique(birth_reduced["vital_status"])
## Challenge: remove "not reported" from vital status
birth_reduced = birth_reduced[birth_reduced.vital_status != "not reported"]
pd.unique(birth_reduced["vital_status"])
```
