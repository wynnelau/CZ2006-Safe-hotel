from selectorlib import Extractor
import requests 
from time import sleep
import csv
import json
import os
from update_map import json_file_url

if not os.path.exists("src/data"):
    os.mkdir("src/data")

url_data = 'src/assets/urls.txt'
booking_data = 'src/assets/booking.yml'
hotel_data_csv = 'src/data/hotel_data.csv'
hotel_data_json = 'src/data/hotel_data.json'


# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file(booking_data)

def scrape(url):    
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'https://www.booking.com/index.en-gb.html',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    # Download the page using requests
    r = requests.get(url, headers=headers)
    # Pass the HTML of the page and create 
    return e.extract(r.text,base_url=url)

def convert_to_json():
    fields_name = ["name", "image", "price", "location", "review", "url"]
    with open(hotel_data_csv, 'r', encoding='utf-8') as infile, open(hotel_data_json, 'w', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile, fields_name)
        out = json.dumps([row for row in reader if row["name"] != "name"], ensure_ascii=False)
        outfile.write(out)
    
def generate_daily_recommendations():
    covid_data = None
    with open(json_file_url, 'r', encoding='utf-8') as f:
        covid_data = json.load(f)
    hotel_data = None
    with open(hotel_data_json, 'r', encoding='utf-8') as f:
        hotel_data = json.load(f)
    covid_data = covid_data["sz"]["aggregatedObj"]
    covid_data = sorted(covid_data.items(), key=lambda x: x[1])
    recommended_hotel = []
    for i in range(len(covid_data)):
        region = covid_data[i][0]
        covid_num = covid_data[i][1]
        covid_risk = None
        if covid_num <= 50:
            covid_risk = "Low"
        elif covid_num <= 150:
            covid_risk = "Medium Low"
        elif covid_num <= 300:
            covid_risk = "Medium"
        elif covid_num <= 500:
            covid_risk = "Medium High"
        else:
            covid_risk = "High"
        for item in hotel_data:
            location = item["location"].strip(", Singapore").upper()
            if region == location:
                recommended_hotel.append(item)
                recommended_hotel[len(recommended_hotel) - 1]["risk_level"] = covid_risk
        if i >= 5 and len(recommended_hotel) >= 10:
            break
    with open(hotel_data_json, 'w', encoding='utf-8') as f:
        f.write(json.dumps(recommended_hotel, ensure_ascii=False))
            

def main():
    with open(url_data, 'r') as urllist, open(hotel_data_csv, 'w', encoding='utf-8') as outfile:
        fieldnames = [
        "name",
        "image",
        "price",
        "location",
        "review",
        "url",
        ]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for url in urllist.readlines():
            data = scrape(url) 
            if data:
                for h in data['hotels']:
                    writer.writerow(h)
    convert_to_json()
    generate_daily_recommendations()
    
main()