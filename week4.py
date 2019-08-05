#!/usr/bin/env python3

#### Visualizing data ####

#### Objectives ####

# Today:
#   creating and modifying scatterplots and boxplots
#   representing time series data as line plots
#   splitting into multiple panels
#   customizing plots

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
# layers:# layers: visual representation of plot, including ways (geometries/shapes) through which data are represented and themes (everything but data) ways (shapes) through which data are represented
(p9.ggplot(data=smoke_complete)
    + p9.geom_point(mapping=p9.aes(x="age_at_diagnosis", y="cigarettes_per_day"))
    )

# ignore warnings (FutureWarning not fatal, just annoying)
import warnings
warnings.simplefilter("ignore")
# add new cell at top of notebook and re-execute plot to remove errors

# building plots iteratively
# add transparency (and remove argument labels, they are implied)
(p9.ggplot(data=smoke_complete)
    + p9.geom_point(mapping=p9.aes(x="age_at_diagnosis", y="cigarettes_per_day"),
    alpha=0.1)
    )

# color points blue
(p9.ggplot(data=smoke_complete)
    + p9.geom_point(mapping=p9.aes(x="age_at_diagnosis", y="cigarettes_per_day"),
    alpha=0.1, color="blue")
    )

# color points by disease
(p9.ggplot(smoke_complete)
    + p9.geom_point(p9.aes(x="age_at_diagnosis", y="cigarettes_per_day",
    color = "disease"), alpha=0.1)
    )

# change background theme
(p9.ggplot(smoke_complete)
    + p9.geom_point(p9.aes(x="age_at_diagnosis", y="cigarettes_per_day",
    color = "disease"), alpha=0.1)
    + p9.theme_bw()
    )

# add x axis label
(p9.ggplot(smoke_complete)
    + p9.geom_point(p9.aes(x="age_at_diagnosis", y="cigarettes_per_day",
    color = "disease"), alpha=0.1)
    + p9.theme_bw()
    + p9.labs(title = "Age at diagnosis vs cigarettes per day",
       x="age (days)",
       y="cigarettes per day")
    )

# save plot
my_plot = (p9.ggplot(smoke_complete)
    + p9.geom_point(p9.aes(x="age_at_diagnosis", y="cigarettes_per_day",
    color = "disease"), alpha=0.1)
    + p9.theme_bw()
    + p9.labs(title = "Age at diagnosis vs cigarettes per day",
       x="age (days)",
       y="cigarettes per day")
    )
my_plot.save("figures/scatterplot.png", width=10, height=10, dpi=300)

## Challenge: create a scatterplot from smoke_complete showing
# age at diagnosis vs years smoked with points colored by gender
# and appropriate axis labels

#### Box and whisker plots ####

# boxplot
(p9.ggplot(smoke_complete)
    + p9.geom_boxplot(p9.aes(x="vital_status", y="cigarettes_per_day"))
    )

# change color of boxes and move aes to geom layer
(p9.ggplot(smoke_complete)
    + p9.geom_boxplot(p9.aes(x="vital_status", y="cigarettes_per_day"),
    color="tomato")
    )

# adding colored points to black box and whisker plot
(p9.ggplot(smoke_complete)
    + p9.geom_boxplot(p9.aes(x=vital_status, y=cigarettes_per_day))
    + p9.geom_jitter(p9.aes(x=vital_status, y=cigarettes_per_day),
    alpha = 0.3, color = "blue")
    )

## Challenge: Run this code in your head and predict what the output will look like. Then, run the code in R and check your predictions. What is the advantage of writing code like this?
my_plot = p9.ggplot(smoke_complete, p9.aes(x="vital_status", y="cigarettes_per_day"))
(my_plot +
  p9.geom_boxplot() +
  p9.geom_jitter(alpha = 0.2, color = "purple")
  )
# note: this is how many ggplot tutorials show iterative plotting!

## Challenge: In the last plot, does the order of layers matter?

#### Plotting time series data ####

# group and count vital status by year of birth
yearly_counts = birth_reduced.groupby(["year_of_birth", "vital_status"])["vital_status"].count()
yearly_counts.head() # both year and vital status are row indexes
# reset the index to use both as column variables
yearly_counts = yearly_counts.reset_index(name="counts")
yearly_counts.head()

# create line plot
(p9.ggplot(yearly_counts)
    + p9.geom_line(p9.aes(x="year_of_birth", y="counts"))
    )
# suboptimal, because two data points for each year (alive and dead)

# map vital status to color, which plots a line each for alive and dead
(p9.ggplot(yearly_counts)
    + p9.geom_line(p9.aes(x="year_of_birth", y="counts", color="vital_status"))
    )

## Challenge: create a plot of birth year and number of patients with two lines representing each gender

## Challenge: how do you show differences in lines using dashes/dots instead of color?

#### Faceting ####

# use previous scatterplot, but separate panels by disease
(p9.ggplot(smoke_complete,
        p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    + p9.facet_wrap("disease")
    )
# wraps panels to make a square/rectangular plot

# add a variable by leaving color but changing panels to other categorical data
(p9.ggplot(smoke_complete,
        p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    + p9.facet_wrap("tumor_stage")
    )
# more categories, but wrapped to keep close to a square

# arrange plots via a formula: vital status in rows, disease in columns
(p9.ggplot(smoke_complete,
        p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    + p9.facet_grid("vital_status ~ disease")
    )

## Challenge: alter your last challenge plot of (birth year by number of patients)
# to show each gender in separate panels

#### Optional: bar plots ####

# can compare with last week's plotting using pandas

# bar plot to show disease counts
(p9.ggplot(smoke_complete)
    + p9.geom_bar(p9.aes(x="disease"))
    )

# change theme to black and white
(p9.ggplot(smoke_complete)
    + p9.geom_bar(p9.aes(x="disease"))
    + p9.theme_bw()
    )

#### Optional: customization ####

# rotate x axis labels 90 degrees
(p9.ggplot(smoke_complete,
        p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    + p9.theme_bw()
    + p9.theme(axis_text_x = p9.element_text(angle=90))
    )

# create custom theme
my_custom_theme = p9.theme(axis_text_x = p9.element_text(color="blue", size=16,
                                                         angle=90, hjust=.5),
                           axis_text_y = p9.element_text(color="blue", size=16))
(p9.ggplot(smoke_complete,
        p9.aes(x="age_at_diagnosis",
        y="cigarettes_per_day",
        color = "disease"))
    + p9.geom_point(alpha=0.1)
    + p9.theme_bw()
    + my_custom_theme
    )

## Challenge: find way to change axes, like tick marks, labels, lines, etc (Google search!)

## Challenge: improve one of the plots previously created today,
# by changing thickness of lines, name of legend, or color palette
# (http://www.cookbook-r.com/Graphs/Colors_(ggplot2)/)

#### Wrapping up ####

# review this class' objectives
# direct towards practice questions (linked in HackMD)
# review course objectives
# direct to additional resources available on HackMD
# reminder about course evaluations and when HackMD page will be cleared
