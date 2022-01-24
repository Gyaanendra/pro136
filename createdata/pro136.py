import csv
import pandas as pd

data = pd.read_csv("main.csv")
print(data.head())

rows = []
with open ("main.csv") as file:
  file_reader = csv.reader(file)
  for i in file_reader:
    rows.append(i)

#CREATE TWO VARIABLES, 'HEADERS' - HOLDS THE COLUMN NAMES AND 'PLANET_DATA' - HOLDS THE DATA INSIDE EACH ROW
headers = rows[0]
planet_data = rows[1:]

print(headers[1])


concluding_data_for_api_list = []

lost = list(planet_data)
for e in lost:
  temp_dict = {
          "name": e[1],
          "distance": e[2],
          "planet_mass": e[3],
          "planet_radius": e[4],
          "planet_luminosity": e[5],
                  
              }
  concluding_data_for_api_list.append(temp_dict)

print(concluding_data_for_api_list)

import json

json_object = json.dumps(concluding_data_for_api_list, indent = 4)
  
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)