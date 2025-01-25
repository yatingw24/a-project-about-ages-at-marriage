# This is a final project for my Foundations class at Columbia J-School. 
In simple words, it is an interactive application allowing people, who find `.csv` or `.xlsx` files cognitively overwhelmed, to browse gender differences in terms of their age at first marriage across countries.\
Here is the [web!](https://a-project-about-ages-at-marriagegunicorn.onrender.com/)

## Goals of My Project:
1. learning and using Flask and pandas to create a simplified interactive application;\
2. converting a dataframe from one version to another - a csv file to an html page;\
3. getting myself familiarized with HTML and CSS basic formatting.

## What I Did:
### Getting Started
acquired the data from [World Bank;](https://databank.worldbank.org/source/gender-statistics) and downloaded the most recent statistics in a csv file;
### Cleaning and Filter Data
1. open the csv file, remove all null values and re-order the countries in which those without any data are moved to the bottom in pandas;
2. exported the cleaned DataFrame as `ages.csv`:
| Country     |     Male    |    Female   |
| --------    |     --      |      --     |
| Afghanistan |    21       |      24     | 
| Albania     |    24       |      30     |
| xxx country |    xx       |      xx     |
|     ...     |    ..       |      ..     |
| Albania     |not available|not available|

### Adding URLS 
1. created the `app.py` file, adding the homepage route:
```python
@app.route("/")
def age_at_marriage():

    df = pd.read_csv("ages.csv")
    ages = df.to_dict('records')

    ages=ages
```
2. building the html template `age_at_marriage.html`;
```python
<body>
    <h1>Age at First Marriage Across Countries</h1>
```
3. rendering it to a full web page: 
```python 
return render_template(
    'age_at_marriage.html')

```

### Adding More Pages and Content
now, we want pages for each country, right?\
So I built another route, `age_at_marriage/<country_name>` and another template, `individual_age.html`:
```python
@app.route("/<country_name>")
def age_by_country(country_name):
    df = pd.read_csv("ages.csv")
    
    matching_rows = df[df['Country'] == country_name]
    country = matching_rows.to_dict('records')[0]
    
    female_age = int(country['Female']) if country['Female'] != 'not available' else None
    male_age = int(country['Male']) if country['Male'] != 'not available' else None
```
Here is what I did in `individual_age.html` for countries without any data:
```python
        <h2>
            {% if country['Female'] != "not available" %}
                Female's age at her first marriage is {{country['Female'] |int}} years old.
            {% else %}
                Data for female's age at first marriage is not available, sorry. 
            {% endif %}
        </h2>
```
### Linking everything
If a user specifies a `country_name`, the app searches for matching rows in the data and returns details for that country:

```python
@app.route("/", methods=["GET"])
def age_at_marriage():
    
    ......

    country = request.args.get("country_name")
    select_gender = request.args.get("gender")

    if country:
        matching_rows = df[df['Country'] == country]
        country=matching_rows.to_dict("records")[0]
        
        return render_template('individual_age.html',
                               country = country
                               )
    elif select_gender:
        if select_gender == 'Female':
            age = df[['Country', 'Female']]

        elif select_gender == 'Male':
            age = df[['Country', 'Male']]
 

        age=age.to_dict('records')
        return render_template('select_gender.html',
                                   gender=select_gender,
                                   ages=age)


    return render_template(
        'age_at_marriage.html',
        ages=ages,
            country=country)
```

## Things I'd like to add/improve:
insert a chart showing gender difference for each country;\
use gender as a secondary filter  to exactly pinpoint a specific gender's age in a specific country;\
autogenerating a chart for comparision purposes




