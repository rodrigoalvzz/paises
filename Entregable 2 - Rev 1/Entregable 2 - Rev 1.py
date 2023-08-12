import pandas as pd
import time
from tabulate import tabulate
import psycopg2
import requests


def get_country_data():
    url = "https://restcountries.com/v2/all"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors

        data = response.json()  # Parse the response as JSON
        return data
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


# Extract data from the API
country_data = get_country_data()

if country_data:
    # Create a list of dictionaries to store the data
    records = []

    for country in country_data:
        record = {
            "Country": country.get("name", ""),
            "Capital": country.get("capital", "Not available"),
            "Population": country.get("population", None),
            "Region": country.get("region", ""),
            "Timezones": ", ".join(country.get("timezones", [])),
            "Subregion": country.get("subregion", ""),
            "Demonym": country.get("demonym", ""),
            "Area": country.get("area", None),
            "Languages": ", ".join(lang.get("name", "") for lang in country.get("languages", [])),
            "Currencies": ", ".join(
                f"{cur.get('name', '')} ({cur.get('symbol', '')})" for cur in country.get("currencies", []))
        }
        records.append(record)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(records)

    # Display the DataFrame
    print(df)
else:
    print("Failed to retrieve country data.")


def get_country_data():
    url = "https://restcountries.com/v2/all"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors

        data = response.json()  # Parse the response as JSON
        return data
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


# Extract data from the API
country_data = get_country_data()

if country_data:
    # Create a list of dictionaries to store the data
    records = []

    for country in country_data:
        record = {
            "Country": country.get("name", ""),
            "Capital": country.get("capital", "Not available"),
            "Population": country.get("population", None),
            "Region": country.get("region", ""),
            "Timezones": ", ".join(country.get("timezones", [])),
            "Subregion": country.get("subregion", ""),
            "Demonym": country.get("demonym", ""),
            "Area": country.get("area", None),
            "Languages": ", ".join(lang.get("name", "") for lang in country.get("languages", [])),
            "Currencies": ", ".join(
                f"{cur.get('name', '')} ({cur.get('symbol', '')})" for cur in country.get("currencies", []))
        }
        records.append(record)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(records)

    # Connect to Amazon Redshift
    conn = psycopg2.connect(
        dbname='data-engineer-database',
        host='data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com',
        port='5439',
        user='rodrigoleonelalvarez_coderhouse',
        password='qrdWA2847A'
    )

    # Create a cursor
    cursor = conn.cursor()

    # Insert data into the Redshift table
    for index, row in df.iterrows():
        query = """
            INSERT INTO country_data (country_name, capital, population, region, timezone, subregion, demonym, area, languages, currencies)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            row["Country"],
            row["Capital"],
            row["Population"],
            row["Region"],
            row["Timezones"],
            row["Subregion"],
            row["Demonym"],
            row["Area"],
            row["Languages"],
            row["Currencies"]
        )

        # Execute the query
        cursor.execute(query, values)

    # Commit and close the connection
    conn.commit()
    conn.close()

    print("Data inserted successfully.")
else:
    print("Failed to retrieve country data.")