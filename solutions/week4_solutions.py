#### Intro to Python: week 4 exercises ####

# Visualizing data

# Objectives:
#   import dataset
#   operators, functions, and data types
#   sequences and dictionaries
#   defining functions

#### In-class exercises ####

## Challenge: create a scatterplot from smoke_complete showing
# age at diagnosis vs years smoked with points colored by gender
# and appropriate axis labels
(p9.ggplot(data=smoke_complete,
         mapping=p9.aes(x="age_at_diagnosis", y="years_smoked"))
    + p9.geom_point(mapping=p9.aes(color="gender"))
    )

## Challenge: visualize the same data as a violin plot in a color of your choice
(p9.ggplot(data=smoke_complete,
          mapping=p9.aes(x="vital_status", y="cigarettes_per_day"))
     + p9.geom_jitter(alpha=0.2, color="orange")
     + p9.geom_violin()
    )

## Challenge: create a plot of birth year and number of patients with
# two lines representing the number of patients of each gender
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

## Challenge: alter your last challenge plot of (birth year by number of patients)
# to show each gender in separate panels
(p9.ggplot(data=gender_counts,
          mapping=p9.aes(x="year_of_birth", y="counts"))
     + p9.geom_line(mapping=p9.aes(color="gender"))
     + p9.facet_wrap("gender")
    )

## Challenge: find way to change tick marks (Google search!)
# search "tick marks ggplot2", most results will be for R and may need to be adapted!
# one possible solution: https://rstudio-pubs-static.s3.amazonaws.com/3364_d1a578f521174152b46b19d0c83cbe7e.html
(p9.ggplot(data=gender_counts,
          mapping=p9.aes(x="year_of_birth", y="counts"))
     + p9.geom_line(mapping=p9.aes(color="gender"))
     + p9.theme(axis_ticks_major_y=p9.element_blank()) #removes y axis ticks
     + p9.facet_wrap("gender")
    )

## Challenge: improve one of the plots previously created today,
# by changing thickness of lines, name of legend, or color palette
# (http://www.cookbook-r.com/Graphs/Colors_(ggplot2)/)
# one example:
(p9.ggplot(data=gender_counts,
          mapping=p9.aes(x="year_of_birth", y="counts"))
     + p9.geom_line(mapping=p9.aes(color="gender"))
     + p9.theme(axis_line_x=p9.element_line(color="black", size=2)) # thicker, black x axis
     + p9.facet_wrap("gender")
    )


#### Extra exercises ####
