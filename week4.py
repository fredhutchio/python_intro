#!/usr/bin/env python3

#### Visualizing data ####

#### Objectives ####

# Today:
# import dataset
# operators, functions, and data types
# sequences and dictionaries
# defining functions

#### Getting set up ####

%matplotlib inline
import plotnine as p9
import pandas as pd

# read in filtered datasets
birth_reduced = pd.read_csv("data/birth_reduced.csv")
smoke_complete = pd.read_csv("data/smoke_complete.csv")

#### create a simple ggplot ####
# bind data to new plot
# specify aesthetic: mapping data to plot
# layers: ways (shapes) through which data are represented
(p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x="age_at_diagnosis", y="cigarettes_per_day"))
    + p9.geom_point()
    )

# ignore warnings (FutureWarning not fatal)
import warnings
warnings.simplefilter("ignore")
# add new cell at top of notebook and re-execute plot to remove errors

# Create object to hold plot framework
smoke_plot = p9.ggplot(data=smoke_complete,
                         mapping=p9.aes(x="age_at_diagnosis", y="cigarettes_per_day"))

# Draw the plot
smoke_plot + p9.geom_point()

# building plots iteratively
# add transparency
smoke_plot + p9.geom_point(alpha=0.1)

# color points blue
smoke_plot + p9.geom_point(alpha=0.1, color="blue")

# color points by disease
(p9.ggplot(data=smoke_complete,
        mapping=p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    )

# add x axis label
(p9.ggplot(data=smoke_complete,
        mapping=p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    + p9.xlab("age at diagnosis (days)")
    )

# change background theme
(p9.ggplot(data=smoke_complete,
        mapping=p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    + p9.xlab("age at diagnosis (days)")
    + p9.theme_bw()
    )

# change font size
(p9.ggplot(data=smoke_complete,
        mapping=p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    + p9.xlab("age at diagnosis (days)")
    + p9.theme_bw()
    + p9.theme(text=p9.element_text(size=16))
    )

## Challenge: create a scatterplot from smoke_complete showing
# age at diagnosis vs years smoked with points colored by gender
# and appropriate axis labels

#### Plotting distributions ####

# boxplot
(p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x="vital_status",
                          y="cigarettes_per_day"))
    + p9.geom_boxplot()
    )

# change color of boxes
(p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x="vital_status",
                          y="cigarettes_per_day"))
    + p9.geom_boxplot(color="tomato")
    )

# adding colored points to black box and whisker plot
(p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x="vital_status",
                          y="cigarettes_per_day"))
    + p9.geom_boxplot()
    + p9.geom_jitter(alpha=0.2, color="blue")
    )

## Challenge: visualize the same data as a violin plot in a color of your choice

#### Plotting time series data

# group and count vital status by year of birth
yearly_counts = birth_reduced.groupby(["year_of_birth", "vital_status"])["vital_status"].count()
yearly_counts # both year and vital status are row indexes
# reset the index to use both as column variables
yearly_counts = yearly_counts.reset_index(name="counts")
yearly_counts

# create line plot
(p9.ggplot(data=yearly_counts,
           mapping=p9.aes(x="year_of_birth",
                          y="counts"))
    + p9.geom_line()
    )
# suboptimal, because two data points for each year (alive and dead)

# map vital status to color, which plots a line each for alive and dead
(p9.ggplot(data=yearly_counts,
           mapping=p9.aes(x="year_of_birth",
                          y="counts",
                          color="vital_status"))
    + p9.geom_line()
    )

## Challenge: create a plot of birth year and number of patients with
# two lines representing the number of patients of each gender

#### Faceting ####

# recall previous scatterplot
(p9.ggplot(data=smoke_complete,
        mapping=p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    )

# separate panels for each disease
(p9.ggplot(data=smoke_complete,
        mapping=p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    + p9.facet_wrap("disease")
    )

# separate graph for each tumor stage
(p9.ggplot(data=smoke_complete,
        mapping=p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    + p9.facet_wrap("tumor_stage")
    )

# arrange plots via a formula: vital status in rows, disease in columns
(p9.ggplot(data=smoke_complete,
        mapping=p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    + p9.facet_grid("vital_status ~ disease")
    )

## Challenge: alter your last challenge plot of (birth year by number of patients)
# to show each gender in separate panels

# bar plot to show disease counts
(p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x="factor(disease)"))
    + p9.geom_bar()
    )

# change theme to black and white
(p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x="factor(disease)"))
    + p9.geom_bar()
    + p9.theme_bw()
    )


# rotate x axis labels 90 degrees
(p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x="factor(disease)"))
    + p9.geom_bar()
    + p9.theme_bw()
    + p9.theme(axis_text_x = p9.element_text(angle=90))
    )

# create custom theme
my_custom_theme = p9.theme(axis_text_x = p9.element_text(color="blue", size=16,
                                                         angle=90, hjust=.5),
                           axis_text_y = p9.element_text(color="blue", size=16))
(p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x="factor(disease)"))
    + p9.geom_bar()
    + my_custom_theme
    )

# save plot
my_plot = (p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x="factor(disease)"))
    + p9.geom_bar()
    + my_custom_theme
    )
my_plot.save("figures/scatterplot.png", width=10, height=10, dpi=300)

## Challenge: find way to change tick marks (Google search!)

## Challenge: improve one of the plots previously created today,
# by changing thickness of lines, name of legend, or color palette
# (http://www.cookbook-r.com/Graphs/Colors_(ggplot2)/)

#### Wrapping up ####

# review objectives
# preview next week's objectives
