# -*- coding: utf-8 -*-

import json
import pandas
  
  
def read_json(filename: str) -> dict:
  
    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")
  
    return data

def create_dataframe(data: list) -> pandas.DataFrame:
  
    # Declare an empty dataframe to append records
    dataframe = pandas.DataFrame()
  
    # Looping through each record
    for d in data:
          
        # Normalize the column levels
        record = pandas.json_normalize(d)
          
        # Append it to the dataframe 
        dataframe = dataframe.append(record, ignore_index=True)
  
    return dataframe

def main():
    # Read the JSON file as python dictionary 
    inputjson = str(input("The JSON file path :"))
    data = read_json(filename=inputjson)

  
    # Generate the dataframe for the array items in 
    # details key 
    dataframe = create_dataframe(data=data['items'])
  
    # Renaming columns of the dataframe 
    print("Normalized Columns:", dataframe.columns.to_list())
    # Convert dataframe to CSV
    dataframe.to_csv("data.csv", index=False)
  
  
if __name__ == '__main__':
    main()

