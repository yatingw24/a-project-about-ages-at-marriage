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

    selected_country = request.args.get("country_name")
    if selected_country:

        matching_rows = df[df['Country'] == selected_country]
        country=matching_rows.to_dict("records")[0]

        return render_template("individual_age.html", country=country)

    return render_template(
        'age_at_marriage.html',
        ages=ages
    )


@app.route("/age_at_marriage/<country_name>")
def age_by_country(country_name):
    df = pd.read_csv("ages.csv")
    
    matching_rows = df[df['Country'] == country_name]

    country = matching_rows.to_dict('records')[0]


    return render_template(
        'individual_age.html',
        country=country,

    )

# @app.route("/age_at_marriage/gender")
# def age_by_gender(female_ages):
#     df = pd.read_csv("ages.csv")
#     matching_rows = df[df['Female'] == female_ages]

#     female = matching_rows.to_dict('records')[0]

#     female_age = int(country["Female"].values[0]) if pd.notna(int(country['Female'].values[0])) else "Data not available"

#     return render_template(
#         'individual_age.html',
#         country=country,
#         female_age=female_age
#     )


#@app.route("/age_at_marriage")


