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
### Cleaning and Filtering Data
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
So I built another route, `age_at_marriage/<country_name>` and another template, `individual_age.html`.\The logic is pretty simple here:
```python
<h1>In {{country['Country']}}, the average age at first marriage for...</h1>
```

If an integer, aka `the age`, is unavilable for a country, then a `not available` will be returned:  
```python
        <h2>
            {% if country['Male'] != "not available"  %}
                Male's age at his first marriage {{country['Male'] |int}} years old.
            {% else %}
                Data for male's age at first marriage is not available, sorry. 
            {% endif %}
        </h2>
```
If data is available for either or both genders:
```python
        <h2>
            {% if country['Female'] != "not available" %}
                Female's age at her first marriage is {{country['Female'] |int}} years old.
            {% else %}
                Data for female's age at first marriage is not available, sorry. 
            {% endif %}
        </h2>
```
Due to time constraint towards the end of semester, I was't able to add gender as a secondary condition/filter. However, I did try to add a new route which is similar to the `@app.route("/<country_name>")` route:

```python 
@app.route("/<gender>", methods=["GET"])
def age_by_gender(gender):
    df = pd.read_csv("ages.csv")

    gender = request.args.get("gender")
```
An user is able to look up a sepcific gender's data for all countries: 
```python
    
    if gender == "Female":
        age = df[['Country', 'Female']]
    elif gender == "Male":
        age = df[['Country', 'Male']]

    ages = ages.to_dict('records')
    return render_template('select_gender.html', gender=gender, ages=ages)
```
the presentable format is a table. In my template, `select_gender.html', I first set up each column's name:
```python
<tr>
    <th>Country</th>
    <th>Age at First Marriage for {{ gender }}</th>
</tr>
```

then, looping through each country's data for the selected gender:
```python

            {% for entry in ages %}
                <tr>
                    <td>{{ entry['Country'] }}</td>
                    <td>
                        {% if entry[gender] != 'not available' %}
                            {{ entry[gender] }} years
                        {% else %}
                            Data not available
                        {% endif %}
                    </td>
                </tr>
            {% endfor %}
```
### Linking everything
To link everything, I went back to my `app.py`. I added and adjusted a few more lines of codes:

```python
country = request.args.get("country_name")
select_gender = request.args.get("gender")
```

If a user specifies a `country_name`, the app searches for matching rows in the data and returns details for that `country`:
```python
    if country:
        matching_rows = df[df['Country'] == country]
        country=matching_rows.to_dict("records")[0]
        
        return render_template('individual_age.html',
                               country = country
                               )
``` 
If a user specifies a `gender`, the app searches for matching rows in the data and returns details for that `gender':
```python
        age=age.to_dict('records')
        return render_template('select_gender.html',
                                   gender=select_gender,
                                   ages=age)
```

## Things I'd like to add/improve:
1. insert a chart showing gender difference for each country;\
2. use gender as a secondary filter  to exactly pinpoint a specific gender's age in a specific country;\
3. autogenerating a chart for comparision purposes




