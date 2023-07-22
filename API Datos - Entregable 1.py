#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import time


# In[11]:




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

# Example usage
country_data = get_country_data()

if country_data:
    # Process and display the country data
    for country in country_data:
        print("Country:", country["name"])
        if "capital" in country:
            print("Capital:", country["capital"])
        else:
            print("Capital: Not available")
        print("Population:", country["population"])
        print("Region:", country["region"])
        print("------------")
else:
    print("Failed to retrieve country data.")


# In[12]:


# Expresando los datos en forma de tabla
country_data = get_country_data()

if country_data:
    # Prepare the table data
    table_data = []
    for country in country_data:
        table_row = [
            country.get("name", ""),
            country.get("capital", "Not available"),
            country.get("population", ""),
            country.get("region", "")
        ]
        table_data.append(table_row)

    # Display the table
    headers = ["Country", "Capital", "Population", "Region"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
else:
    print("Failed to retrieve country data.")


# In[ ]:




