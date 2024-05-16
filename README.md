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

### Data Cleaning
-Verified uniformity of column names (lowercase and underscores if necessary)
-Created new columns for better comparison of the two datasets
   -Added the year of wine to first dataset; extracted from title column
   -Added the variety to the second dataset; extracted from the name column
-Checked for duplicated bottles of wine, not necessarily duplicated rows
-Checked for null values

### Data Transformation
-Combined 4 datasets divided by type of variety (red, white, rosé and sparkling) from Vivino into one main dataset
-After analyzing the two datasets seperately, we merged them by winery, variety, year and country

### Data Analysis
-Used descriptive statistics to understand the central tendencies and dispersion in each dataset
   -Identify the top values for categorical columns
   -Get the average and standard deviation for numerical columns
-Compared the points and ratings in the merged data to identify any correlation

## Conclusions

#### Top Contries & Varieties with Most Reviews

##### Reviews from Sommeliers 
|Rank|country|count|
|----|-------|-----|
|1|US|50233|
|2|France|19970|
|3|Italy|17812|
|4|Spain|6026|
|5|Portugal|5222|
|6|Chile|4179|
|7|Argentina|3543|
|8|Austria|3024|
|9|Australia|2183|
|10|Germany|1990|

#### Wine Reviews by Sommeliers
   >Both the average point given to wines and the median are 88
    -Most wines received between 86 and 91 points, indicating a relatively high overall quality of wines in the dataset.

   >The average price for a bottle of wine in the dataset is $35.36. Additionally, the standard deviation is high (41.02), indicating a wide dispersion of prices around the mean.
    -The range for prices was from $4 to $3,300 
    -We believe the pressence of outliers inlfluenced the values for the mean and standard deviation

   >We found the points given to the most expensive wine and the cheapest
    -The most expensive wine got 88 points while the cheapest wines averaged at 84

#### Wine Reviews by Consumers
   >The average rating given to wines is 3.86 (similar to the median 3.9)
    -Most wines received ratings between 3.8 and 4.1, indicating a relatively high overall quality of wines

   >The average price for a bottle of wine in the dataset is $33.02 while the median is $15.95. Additionally, the standard deviation is high (70.90), indicating a wide dispersion of prices around the mean.
    -The range for prices was from $3.15 to $3,410.79
    -These results are likely due to the pressence of various outliers in the dataset

   >We found the ratings given to the most expensive wine and the cheapest
    -The most expensive wine got a 4.7 rating while the cheapest wines got a 3.8 and 4.2

#### Correlation between the Ratings and Points


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
