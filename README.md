# Del Barril Vino

Project Documentation for Taisgaly Vélez & Daniela Rivera

## Introduction

**Del Barril Vino** is a consulting company dedicated to providing the best wine recommendations to stores and restaurants in Puerto Rico. Our recent client wishes to incorporate a list of wines that could potentially increase sales.

To provide the best options, we’ve compared two sets of wine reviews from different sources to uncover similarities, differences and insights. While one dataset is focused on points given by professional tasters, the second focuses on ratings given by regular consumers.

## Data Collected

Our initial dataset consists of wines reviewed by professional sommeliers, who offer comprehensive details about each bottle, including an detailed description of its taste and an overall quality score ranging from 80 to 100.

In contrast, our second dataset features wine reviews from the website Vivino, where everyday consumers share their feedback on specific bottles and rate them on a scale from 1.0 to 5.0. Unlike the first dataset, the information provided here is less detailed, potentially complicating direct comparisons between the two sets of reviews.

Lastly, we've analyzed a third dataset that details the average serving size of alcohol consumption per person by country, categorized into beer, wine, and spirits. Although this dataset is not directly related to the first two, it offers valuable insights into the preferred types of alcohol consumed by people from different regions.

You will find the link to all datasets here:

>[Kaggle Wine_Review_Data](https://www.kaggle.com/datasets/zynicide/wine-reviews/data?select=winemag-data-130k-v2.csv)

>[Kaggle My Vivino](https://www.kaggle.com/code/atabekabduakimov/my-vivino/input))
   >We combined the csv files for red, white, rosé and sparkling wine

>[Kaggle Alcohol Consumption](https://www.kaggle.com/datasets/mysarahmadbhat/alcohol-consumption)

Other Sources of information:

We wanted to know which countries produced the most wine in the past year to potentially link the number of bottles reviewed by country to their wine production volume. The idea is that higher wine production could lead to greater variety and, as a result, more reviews.

>[Countries that Produce the Most Wine](https://worldpopulationreview.com/country-rankings/wine-producing-countries)

## Problem & Hypotheses

Our focus is to answer the following questions:

1. What are the top countries recorded in each dataset?
   > In both datasets, we believe the predominant countries recorded will be European countries such as Spain, France and Italy, followed by United States. 
2. What are the top varieties reviewed?
   > The top grapes will be red wine grapes such as Cabernet Sauvignon, Pinot Noir and Merlot. For white wine it will be Chardonnay.
3. Is there a correlation between the point given by professionals and the ratings given by consumers?
   > There will be consistency between the ratings and reviews of wines in the two datasets.

**Note:** The two datasets differ in the representation of wine varieties, with one dataset containing a much more diverse selection of varietals than the other. This could be influenced by the methods used to collect the data.

From the alcohol consumption dataset:
   
4. Which country consumes the most wine per person?
   > We do not believe the United States consumes the most wine per person. Their highest alcohol consumption will be for beer. For wine consumption it will most likely be a European country.


## Methodology

Describe the methodology you are using, explaining the steps upi took for data cleaning, analysis, etc.

## Conclusions

What did we find after cleaning and analyzing the data?

## Further Questions

Further analysis we would like to do
- What are the most common flavor profiles/descriptions for the top grapes
- Analyze the quality of the top grapes (acidity, sweetness, pH, etc.)
- Look for reviews that have more bottles of wine in common
   - Possible solution: web scrape Vivino to get more wine options

## Presentation URL

[Del Barril Vino PPT](https://docs.google.com/presentation/d/1ZH7R2Tw5t50jfIuhUUlLgipGgpBX1qEi/edit#slide=id.p1)

## Trello Page

[Trello Page](https://trello.com/b/hsTHufe9/ihproject1)



--------------------------------------------------------------------------------------------------------------------


## Deliverables

You must submit the following deliverables in order for the project to be deemed complete:

#### DONE A new repository with the name data-wrangling-project on your GitHub account.
#### DONE A working code that meets all technical requirements, built by you.
#### DONE At least 1 Jupyter notebook is required
#### DONE Include your functions in .py files
#### DONE Additional needed files for your work
6. A README with the completed project documentation.
#### DONE The URL of the slides for your project presentation.
8. Presentation: When presenting your work, there are many important factors to consider, such as the content of your presentation and the way you deliver it.
   Remember to allow time to rehearse the presentation beforehand.
   See “Presentation” section below for guidelines.
9. Paste your own repository’s link in the Student Portal Project Activity.
   Note: Each student should have their own repository to submit.
#### DONE Links to the data you are using (sources) and your Kanban board (Trello) in the README.
