# Import the necessary modules
from serpapi import GoogleSearch
import csv 

# Set the search parameters
params = {
    'api_key': 'b23f9c0c727abb17b037f8ba102a8d996eafdbd4ae81080de0913415ee0da823',  # Serp API key                     
    'engine': 'google_maps',               # Search engine to use (Google Maps in this case) 	
    'q': 'The 90s Café, Chapter 1',        # Query to search for
    'll': '@21.2284856,81.29664,15z',      # Location coordinates
    'type': 'search'                      # Type of search to perform
}

# Execute the search and get the results as a dictionary
search = GoogleSearch(params)
results = search.get_dict()

# Extract the desired information from the search results
title = results["place_results"]['title']                # Store name
add = results["place_results"]['address']                # Store address
hrs = results["place_results"]['hours']                  # Store timings
gps_coor = results["place_results"]['gps_coordinates']   # GPS coordinates
ph = results["place_results"]['phone']                   # Phone number

# Remove the \u202f characters from the timings (if any)
for item in hrs:
    for key, value in item.items():
        item[key] = value.replace('\u202f', '')

# Set the CSV file fields and rows
fields = ['Store Name', 'Address', 'Timings', 'Coordinates (Latitude/Longitude)', 'Phone Number'] 
rows = [ str(title), str(add), str(hrs), str(gps_coor), str(ph)]
filename = "Retail_Store_Location_Scraper.csv"
    
# Write the data to a CSV file
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerow(rows)

# Print the extracted information
print("Store Name                       ",results["place_results"]['title'])
print("Address                          ",results["place_results"]['address'])
print("Timings                          ",results["place_results"]['hours'])
print("Coordinates (Latitude/Longitude) ",results["place_results"]['gps_coordinates'])
print("Phone Number                     ",results["place_results"]['phone'])