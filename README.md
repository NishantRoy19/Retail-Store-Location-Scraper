# Retail-Store-Location-Scraper
Task is to scrape the locations of retail brand in India and extract the following information: Store Name, Address, Timings, Coordinates (Latitude/Longitude), Phone Number.

This project is about scraping the locations of a retail brand in India from Google Maps using different Python libraries like Selenium, Playwright, and serpapi. We have used the serpapi library in this example to extract the locations of 'The 90s Café, Chapter 1' in India.

To use this script, you will need to have an API key for SerpAPI. The API key needs to be added to the params dictionary in the script.

To run the script, simply execute the script in your Python environment. The extracted store location details will be printed to the console, and the details will be written to a CSV file named "Retail_Store_Location_Scraper.csv".

## Requirements
+ Python 3.7+
+ serpapi library  (https://pypi.org/project/google-serp-api/)
+ csv

## Installation
To install the serpapi library, use the following command:

```
pip install google-search-results
```

## Usage
To use this script, replace the value of q in the params dictionary with the name of the retail brand you want to search for, and replace the value of ll with the latitude, longitude, and zoom level of the location you want to search around.

After running the script, it will extract the store name, address, timings, coordinates, and phone number for the retail brand's locations in India and save the data in a CSV file named Retail_Store_Location_Scraper.csv.

## License
This project is licensed under the MIT License.
