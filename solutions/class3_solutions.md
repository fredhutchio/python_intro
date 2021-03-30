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

#### Challenge-subset

```python
clinical_subset = clinical_df[(clinical_df.vital_status == 'alive') & (clinical_df.ethnicity == 'hispanic or latino')]
```

#### Challenge-subset2

```python
# grouping data by disease (x-axis)
grouped_disease = clinical_df_patients.groupby("disease")
# extracting and storing only the primary_diagnosis count numbers (y-axis)
primary_diagnosis_counts = grouped_disease.primary_diagnosis.count()

# creating a bar graph 
primary_diagnosis_counts.plot(title = 'Primary Diagnosis Numbers of Each Disease', kind = 'bar');
# semicolon in the previous line eliminates extra text in output

# labeling axes
plt.xlabel("Disease");
plt.ylabel("Frequency");
```

#### Challenge-disease-plot

```python

grouped_disease = clinical_df.groupby("disease")
disease_counts = grouped_disease.disease.count()
disease_counts.plot(kind="bar");
```

#### Challenge-alive-yob

```python
# remove missing data (not 
alive_complete = clinical_df[clinical_df.vital_status == "alive"]
alive_counts = alive_complete.year_of_birth.count()
print(age_counts)
```
