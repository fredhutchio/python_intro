## Intro to Python
# Class 4 Solutions

## Challenge-scatter

Create a scatterplot from smoke_complete showing age at diagnosis vs years smoked with points colored by gender and appropriate axis labels

```python
(p9.ggplot(data=smoke_complete,
         mapping=p9.aes(x="age_at_diagnosis", y="years_smoked"))
    + p9.geom_point(mapping=p9.aes(color="gender"))
    )
```

## Challenge-comments

What is the advantage of writing code like this?

```python
my_plot = p9.ggplot(smoke_complete, p9.aes(x='vital_status', y='cigarettes_per_day'))
(my_plot 
    + p9.geom_boxplot(outlier_alpha=0)
    + p9.geom_jitter(alpha=0.2, color='purple')
)
```

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

Does the order of layers in the last plot matter? 
What happens if `jitter` is coded before `boxplot`?

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

Visualize the same data as a violin plot in a color of your choice

```python
(p9.ggplot(data=smoke_complete,
          mapping=p9.aes(x="vital_status", y="cigarettes_per_day"))
     + p9.geom_jitter(alpha=0.2, color="orange")
     + p9.geom_violin()
    )
```

## Challenge-line

Create a line plot for year of birth and number of patients with lines representing each gender.
Hint: you'll need to manipulate the `birth_reduced` dataset first.

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

How do you show differences in lines using dashes/dots instead of color?

```python
(p9.ggplot(yearly_counts)
    + p9.geom_line(p9.aes(x='year_of_birth',
                          y='counts',
                          linetype='disease'))
    )
```

## Challenge-panels

Alter your last challenge plot of (birth year by number of patients) 
to show each gender in separate panels

```python
(p9.ggplot(data=gender_counts,
          mapping=p9.aes(x="year_of_birth", y="counts"))
     + p9.geom_line(mapping=p9.aes(color="gender"))
     + p9.facet_wrap("gender")
    )
```

## Challenge: 

How do you change axis formatting, like tick marks and lines?
Hint: You may want to use Google!

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
