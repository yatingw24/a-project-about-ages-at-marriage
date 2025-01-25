# This is a final project for my Foundations class at Columbia J-School. 
In simple words, it is an interactive application allowing people, who find csv or xlsx files too complicated to filter, to browse gender differences in terms of their age at first marriage across countries.\
Here is the [web!](https://a-project-about-ages-at-marriagegunicorn.onrender.com/)

## Goals of My Project:
1.learning and using Flask and pandas to create a simplified interactive application;\
2.converting a dataframe from one version to another - a csv file to an html page;\
3.getting myself familiarized with HTML and CSS basic formatting.

## What I did:
1. acquired the data from [World Bank;](https://databank.worldbank.org/source/gender-statistics) and downloaded the most recent statistics in a csv file;\
2. in a jupyter notebook, imported the csv file and created a new DataFrame. Then, removed all null values and re-ordered the countries in which countries without any data are moved to the bottom;\
3. exported the cleaned DataFrame in csv format;\
4. created the `app.py` file, adding the homepage route while at the same time building the html template `age_at_marriage.html`;/
5. now, we want pages for each country, right? So I built another route, `age_at_marriage/<country_name>`.\
6. In order to populate the page, I created a new template, `individual_age.html`.

## Things I'd like to add/improve:
### insert a chart showing gender difference for each country;
### use gender as a secondary filter 




