## Intro to Python, Class 4 Solutions

## Challenge-scatter

```python
(p9.ggplot(data=smoke_complete,
         mapping=p9.aes(x="age_at_diagnosis", y="years_smoked"))
    + p9.geom_point(mapping=p9.aes(color="gender"))
    )
```

## Challenge-comments

```python
# create object holding data and aesthetic mapping
my_plot = p9.ggplot(smoke_complete, p9.aes(x='vital_status', y='cigarettes_per_day'))
# plot using object
(my_plot 
    # boxplot
    + p9.geom_boxplot(outlier_alpha=0)
    # points overlaid on boxplot
    + p9.geom_jitter(alpha=0.2, color='purple')
)
```

This allows the coder to experiment with different ways of representing the data,
while holding the data and comparisons (e.g., axes) static.

## Challenge-layers

```python
my_plot = p9.ggplot(smoke_complete, p9.aes(x='vital_status', y='cigarettes_per_day'))
(my_plot 
    + p9.geom_jitter(alpha=0.2, color='purple')
    + p9.geom_boxplot(outlier_alpha=0)
)
```

Yes, the order matters:
later layers are plotted on top of previous layers.

## Challenge-violin

```python
(p9.ggplot(data=smoke_complete,
          mapping=p9.aes(x="vital_status", y="cigarettes_per_day"))
     + p9.geom_jitter(alpha=0.2, color="orange")
     + p9.geom_violin()
    )
```

## Challenge-line

```python
# create new data object grouping by year of birth and gender
gender_counts = birth_reduced.groupby(["year_of_birth", "gender"])["gender"].count()
# reset index to format data frame
gender_counts = gender_counts.reset_index(name="counts")
gender_counts.head()
# plot graph
(p9.ggplot(data=gender_counts,
          mapping=p9.aes(x="year_of_birth", y="counts"))
     + p9.geom_line(mapping=p9.aes(color="gender"))
    )
```

## Challenge-dashes 

```python
(p9.ggplot(yearly_counts)
    + p9.geom_line(p9.aes(x='year_of_birth',
                          y='counts',
                          linetype='disease'))
    )
```

## Challenge-panels

```python
(p9.ggplot(data=gender_counts,
          mapping=p9.aes(x="year_of_birth", y="counts"))
     + p9.geom_line(mapping=p9.aes(color="gender"))
     + p9.facet_wrap("gender")
    )
```

## Challenge: 

Search "tick marks ggplot2", most results will be for R and may need to be adapted!
One possible solution: https://rstudio-pubs-static.s3.amazonaws.com/3364_d1a578f521174152b46b19d0c83cbe7e.html

```python
(p9.ggplot(data=gender_counts,
          mapping=p9.aes(x="year_of_birth", y="counts"))
     + p9.geom_line(mapping=p9.aes(color="gender"))
     + p9.theme(axis_ticks_major_y=p9.element_blank()) #removes y axis ticks
     + p9.facet_wrap("gender")
    )
```
