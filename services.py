# -*- coding: utf-8 -*-
"""services

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DXG4wjKHqnNLmtndCTHNEbsAQd2WaCsT
"""

data = [{"name": "prime", "address": "Nageshwar Nagar moshi,bhosari,india","buyer":True},
    {"name": "Sanku", "address": "DY patil akurdi,pune,india","seller":True},
    {"name": "harsha", "address": "1600 Pennsylvania Avenue NW, Washington, DC","buyer":True},
    {"name": "adya", "address": "1600 Pennsylvania Avenue NW, Washington, DC 20500","seller":True}]

print(data)



import requests
import pandas as pd
from geopy.distance import geodesic

# Define the API endpoint and API key for OpenCage Geocoder
geocoder_endpoint = "https://api.opencagedata.com/geocode/v1/json"
geocoder_api_key = "8e1d04c8640f461eb852a9f44c79387e"

# Define the list of buyers and sellers with their addresses
people = [
    {"name": "prime", "address": "350 Fifth Avenue, New York, NY 10118,US", "buyer": True},
    {"name": "Sanku", "address": "DY patil akurdi,pune,india", "buyer": False},
    {"name": "harsha", "address": "1600 Pennsylvania Avenue NW, Washington, DC,US", "buyer": True},
    {"name": "adya", "address": "Nageshwar Nagar moshi,bhosari,india", "buyer": False}
]

# Create a pandas dataframe from the people list
df = pd.DataFrame(people)

# Create two separate dataframes for buyers and sellers
buyers_df = df[df["buyer"] == True]
sellers_df = df[df["buyer"] == False]

# Loop through each buyer and find the nearest seller
for index, buyer in buyers_df.iterrows():
    buyer_address = buyer["address"]
    buyer_params = {"q": buyer_address, "key": geocoder_api_key}
    buyer_response = requests.get(geocoder_endpoint, params=buyer_params).json()
    
    if buyer_response["results"]:
        buyer_lat = buyer_response["results"][0]["geometry"]["lat"]
        buyer_lon = buyer_response["results"][0]["geometry"]["lng"]
        seller_distances = {}
        
        # Loop through each seller and calculate the distance from the buyer
        for index, seller in sellers_df.iterrows():
            seller_address = seller["address"]
            seller_params = {"q": seller_address, "key": geocoder_api_key}
            seller_response = requests.get(geocoder_endpoint, params=seller_params).json()

            if seller_response["results"]:
                seller_lat = seller_response["results"][0]["geometry"]["lat"]
                seller_lon = seller_response["results"][0]["geometry"]["lng"]
                distance = geodesic((buyer_lat, buyer_lon), (seller_lat, seller_lon)).km
                seller_distances[seller["name"]] = distance
        
        # Sort the seller distances by distance
        sorted_distances = sorted(seller_distances.items(), key=lambda x: x[1])
        nearest_seller_name = sorted_distances[0][0]
        print(f"The nearest seller to {buyer['name']} is {nearest_seller_name}")
    else:
        print(f"Error: {buyer_address} not found")
