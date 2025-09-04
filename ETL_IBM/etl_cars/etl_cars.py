import glob
import pandas as pd 
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "log_file.txt" 
target_file = "transformed_data.csv" 

def ex_csv(f):
    return pd.read_csv(f)

def ex_json(f):
    return pd.read_json(f, lines=True)

def ex_xml(f):
    rows = []
    tree = ET.parse(f)
    root = tree.getroot()
    for p in root:
        rows.append({
            'car_model': p.find('car_model').text,
            'year_of_manufacture': int(p.find('year_of_manufacture').text),
            'price': float(p.find('price').text),
            'fuel': p.find('fuel').text
        })
    return pd.DataFrame(rows)

def extract(): 
    extracted_data = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])

    for csvfile in glob.glob("*.csv"): 
        if csvfile != target_file: 
            extracted_data = pd.concat([extracted_data, ex_csv(csvfile)], ignore_index=True) 

    for jsonfile in glob.glob("*.json"): 
        extracted_data = pd.concat([extracted_data, ex_json(jsonfile)], ignore_index=True) 

    for xmlfile in glob.glob("*.xml"): 
        extracted_data = pd.concat([extracted_data, ex_xml(xmlfile)], ignore_index=True) 
         
    return extracted_data 

def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file, index=False) 

def log_progress(message): 
    timestamp_format = '%Y-%b-%d-%H:%M:%S'  # Fixed format
    now = datetime.now() 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file, "a") as f: 
        f.write(timestamp + ',' + message + '\n') 

# Main ETL Process
log_progress("ETL Job Started") 
log_progress("Extract phase Started") 
extracted_data = extract() 
log_progress("Extract phase Ended") 
log_progress("Load phase Started") 
load_data(target_file, extracted_data) 
log_progress("Load phase Ended") 
log_progress("ETL Job Ended") 
