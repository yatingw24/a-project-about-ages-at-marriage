import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/age_at_marriage", methods=["GET"])
def age_at_marriage():

    df = pd.read_csv("ages.csv")
    ages = df.to_dict('records')

    ages=ages

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
            country=country 

        )



@app.route("/age_at_marriage/<country_name>")
def age_by_country(country_name):
    df = pd.read_csv("ages.csv")
    
    matching_rows = df[df['Country'] == country_name]
    country = matching_rows.to_dict('records')[0]
    
    female_age = int(country['Female']) if country['Female'] != 'not available' else None
    male_age = int(country['Male']) if country['Male'] != 'not available' else None


    return render_template(
        'individual_age.html',
        country=country,
        female_age=female_age,
        male_age=male_age
    )




@app.route("/age_at_marriage/<gender>", methods=["GET"])
def age_by_gender(gender):
    df = pd.read_csv("ages.csv")
    


    gender = request.args.get("gender")
    
    if gender == "Female":
        age = df[['Country', 'Female']]
    elif gender == "Male":
        age = df[['Country', 'Male']]

    ages = ages.to_dict('records')
    return render_template('select_gender.html', gender=gender, ages=ages)


