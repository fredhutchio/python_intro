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

# Read in the survey CSV
surveys_complete = pd.read_csv('data/birth_reduced.csv')
smoke_complete = pd.read_csv('data/smoke_complete.csv')

# create a simple ggplot
# bind data to new plot
# specify aesthetic: mapping data to plot
# layers: ways (shapes) through which data are represented
(p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x='age_at_diagnosis', y='cigarettes_per_day'))
    + p9.geom_point()
    )
# Create object to hold plot framework
smoke_plot = p9.ggplot(data=smoke_complete,
                         mapping=p9.aes(x='age_at_diagnosis', y='cigarettes_per_day'))

# Draw the plot
smoke_plot + p9.geom_point()

# building plots iteratively
# add transparency
smoke_plot + p9.geom_point(alpha=0.1)

# color points blue
smoke_plot + p9.geom_point(alpha=0.1, color='blue')

# color points by disease
(p9.ggplot(data=smoke_complete,
        mapping=p9.aes(x='age_at_diagnosis',
        y='cigarettes_per_day',
        color = 'disease'))
    + p9.geom_point(alpha=0.1)
    )

# add x axis label
(p9.ggplot(data=smoke_complete,
        mapping=p9.aes(x='age_at_diagnosis',
        y='cigarettes_per_day',
        color = 'disease'))
    + p9.geom_point(alpha=0.1)
    + p9.xlab("age at diagnosis (days)")
)

# change background theme
(p9.ggplot(data=smoke_complete,
        mapping=p9.aes(x='age_at_diagnosis',
        y='cigarettes_per_day',
        color = 'disease'))
    + p9.geom_point(alpha=0.1)
    + p9.xlab("age at diagnosis (days)")
    + p9.theme_bw()
)

# change font size
(p9.ggplot(data=smoke_complete,
        mapping=p9.aes(x='age_at_diagnosis',
        y='cigarettes_per_day',
        color = 'disease'))
    + p9.geom_point(alpha=0.1)
    + p9.xlab("age at diagnosis (days)")
    + p9.theme_bw()
    + p9.theme(text=p9.element_text(size=16))
)

# plotting distributions
(p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x='vital_status',
                          y='cigarettes_per_day'))
    + p9.geom_boxplot()
)

# change color
(p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x='vital_status',
                          y='cigarettes_per_day'))
    + p9.geom_boxplot(color="tomato")
)

# adding colored points to black box and whisker plot
(p9.ggplot(data=smoke_complete,
           mapping=p9.aes(x='vital_status',
                          y='cigarettes_per_day'))
    + p9.geom_boxplot()
    + p9.geom_jitter(alpha=0.2, color="blue")
)

# plotting time series data

yearly_counts = surveys_complete.groupby(['year', 'species_id'])['species_id'].count()
yearly_counts

yearly_counts = yearly_counts.reset_index(name='counts')
yearly_counts

(p9.ggplot(data=yearly_counts,
           mapping=p9.aes(x='year',
                          y='counts'))
    + p9.geom_line()
)

(p9.ggplot(data=yearly_counts,
           mapping=p9.aes(x='year',
                          y='counts',
                          color='species_id'))
    + p9.geom_line()
)

# faceting

(p9.ggplot(data=surveys_complete,
           mapping=p9.aes(x='weight',
                          y='hindfoot_length',
                          color='species_id'))
    + p9.geom_point(alpha=0.1)
)

# separate graphs for each sex

(p9.ggplot(data=surveys_complete,
           mapping=p9.aes(x='weight',
                          y='hindfoot_length',
                          color='species_id'))
    + p9.geom_point(alpha=0.1)
    + p9.facet_wrap("sex")
)

# separate graph for each plot ID

(p9.ggplot(data=surveys_complete,
           mapping=p9.aes(x='weight',
                          y='hindfoot_length',
                          color='species_id'))
    + p9.geom_point(alpha=0.1)
    + p9.facet_wrap("plot_id")
)

# arrange plots via a formula

# only selecte the years of interest
survey_2000 = surveys_complete[surveys_complete["year"].isin([2000, 2001])]

(p9.ggplot(data=survey_2000,
           mapping=p9.aes(x='weight',
                          y='hindfoot_length',
                          color='species_id'))
    + p9.geom_point(alpha=0.1)
    + p9.facet_grid("year ~ sex")
)

# bar plot

(p9.ggplot(data=surveys_complete,
           mapping=p9.aes(x='factor(year)'))
    + p9.geom_bar()
)

# add theme

(p9.ggplot(data=surveys_complete,
           mapping=p9.aes(x='factor(year)'))
    + p9.geom_bar()
    + p9.theme_bw()
    + p9.theme(axis_text_x = p9.element_text(angle=90))
)

# create custom theme

my_custom_theme = p9.theme(axis_text_x = p9.element_text(color="grey", size=10,
                                                         angle=90, hjust=.5),
                           axis_text_y = p9.element_text(color="grey", size=10))
(p9.ggplot(data=surveys_complete,
           mapping=p9.aes(x='factor(year)'))
    + p9.geom_bar()
    + my_custom_theme
)

# save plot

my_plot = (p9.ggplot(data=surveys_complete,
           mapping=p9.aes(x='weight', y='hindfoot_length'))
    + p9.geom_point()
)
my_plot.save("scatterplot.png", width=10, height=10, dpi=300)

#### Wrapping up ####

# review objectives
# preview next week's objectives
