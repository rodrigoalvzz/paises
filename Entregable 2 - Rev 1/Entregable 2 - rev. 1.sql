 -- Drop the existing table
DROP TABLE IF EXISTS country_data;

-- Create the table with the primary key constraint
CREATE TABLE country_data (
    country_name VARCHAR(255) PRIMARY KEY,
    capital VARCHAR(255),
    population INT,
    region VARCHAR(255),
    timezone VARCHAR(255),
    subregion VARCHAR(255),
    demonym VARCHAR(255),
    area INT,
    languages VARCHAR(255),
    currencies VARCHAR(255)
);
select*from country_data
