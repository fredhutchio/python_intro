# Intro to Python, Class 3 Solutions

#### Challenge-conditionals

```python
clinical_df[(clinical_df.tumor_stage == "stage ia") & (clinical_df.days_to_death > 365)]
```

#### Challenge-combine

```python
clinical_df.groupby("vital_status")["vital_status"].count()["alive"]
```

#### Challenge-total-count

```python
total_count = clinical_df.groupby("disease")["disease"].count()
total_count = clinical_df.groupby("disease").disease.count() # same as above
# plot the number of samples for each cancer type
total_count.plot(kind="bar");
```

#### Challenge-filter

```python
# Option 1
birth_reduced = birth_reduced.dropna(subset = ["year_of_birth", "vital_status"])

# Option 2
birth_reduced = birth_reduced[-pd.isnull(birth_reduced["year_of_birth"])]
birth_reduced = birth_reduced[-pd.isnull(birth_reduced["vital_status"])]

# check to see that it worked
pd.unique(birth_reduced["vital_status"])
```

#### Challenge-not-reported

```python
birth_reduced = birth_reduced[birth_reduced.vital_status != "not reported"]
pd.unique(birth_reduced["vital_status"])
```
