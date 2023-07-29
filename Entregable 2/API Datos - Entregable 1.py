#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
import pandas as pd
import time


# In[12]:


pip install tabulate


# In[14]:



from tabulate import tabulate


# In[7]:




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


# In[15]:


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


# In[10]:


pip install sqlalchemy-redshift


# In[11]:


pip install redshift_connector


# In[16]:


pip install ipython-sql


# In[1]:


pip install psycopg2


# In[2]:


import requests
import psycopg2

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

def insert_country_data_to_redshift(data):
    # Datos de acceso a Amazon Redshift
    host = "data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com"
    port = "5439"
    database = "data-engineer-database"
    user = "rodrigoleonelalvarez_coderhouse"
    password = "qrdWA2847A"

    # Establecer la conexión a Amazon Redshift
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    # Crear un cursor para ejecutar las sentencias SQL
    cursor = conn.cursor()

    # Preparar la sentencia SQL INSERT
    sql_insert = "INSERT INTO country_data (country_name, capital, population, region) VALUES (%s, %s, %s, %s);"

    # Insertar los datos en la tabla
    for country in data:
        values = (country.get("name", ""),
                  country.get("capital", "Not available"),
                  country.get("population", ""),
                  country.get("region", ""))
        cursor.execute(sql_insert, values)

    # Confirmar y cerrar la conexión
    conn.commit()
    conn.close()

# Obtener los datos de la API
country_data = get_country_data()

if country_data:
    # Insertar los datos en Amazon Redshift
    insert_country_data_to_redshift(country_data)
    print("Datos insertados correctamente en la tabla country_data.")
else:
    print("Fallo al obtener los datos de la API.")


# In[ ]:




