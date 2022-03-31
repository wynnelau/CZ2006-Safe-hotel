from selectorlib import Extractor
import requests 
from time import sleep
import csv
import json
import os
from datetime import datetime
from server.utils import *

if not os.path.exists("src/data"):
    os.mkdir("src/data")

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file(booking_data)

def get_url():
    current_year, current_month, current_day = datetime.now().year, datetime.now().month, datetime.now().day
    next_year, next_month, next_day = current_year, current_month, current_day
    if current_month in [1, 3, 5, 7, 8, 10, 12] and current_day == 31:
        next_day = 1
        if next_month == 12:
            next_year += 1
            next_month = 1
        else:
            next_month += 1
    elif current_month != 2 and current_day == 30:
        next_day = 1
        next_month += 1
    elif current_month == 2:
        if current_year % 4 == 0 and current_year % 100 != 0:
            if current_day == 29:
                next_day = 1
                next_month += 1
            else:
                next_day += 1
        else:
            if current_day == 28:
                next_day = 1
                next_month += 1
            else:
                next_day += 1
    else:
        next_day += 1
        
    return "https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1DCAMoggI46AdIM1gEaMkBiAEBmAEJuAEXyAEM2AED6AEB-AECiAIBqAIDuALcu5WSBsACAdICJDJiNDk2ZmI0LWVjMGUtNDU5MS1iMzM0LTc1Mjk4Mzg4MTgwOdgCBOACAQ;sid=0737c5e24a4d094304ae8d9a75c98c33;city=-73635&" + \
        "checkin_year=" + str(current_year) + "&checkin_month=" + str(current_month) + "&checkin_monthday=" + str(current_day) + \
        "&checkout_year=" + str(next_year) + "&checkout_month=" + str(next_month) + "&checkout_monthday=" + str(next_day)

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
    return e.extract(r.text, base_url=url)

def fetch_hotel_data():
    url = get_url()
    with open(hotel_data_csv, 'w', encoding='utf-8') as outfile:
        fieldnames = [
            "name",
            "image",
            "price",
            "location",
            "review",
            "url",
        ]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for i in range(0, 10000, 25):
            data = scrape(url + "&offset=" + str(i))
            if data['hotels']:
                for h in data['hotels']:
                    writer.writerow(h)
            else:
                break

def convert_to_json():
    fields_name = ["name", "image", "price", "location", "review", "url"]
    with open(hotel_data_csv, 'r', encoding='utf-8') as infile, open(hotel_data_json, 'w', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile, fields_name)
        out = json.dumps([row for row in reader if row["name"] != "name"], ensure_ascii=False)
        outfile.write(out)
    
def generate_daily_recommendations_and_standardize_data():
    covid_data = None
    with open(json_file_url, 'r', encoding='utf-8') as f:
        covid_data = json.load(f)
    hotel_data = None
    with open(hotel_data_json, 'r', encoding='utf-8') as f:
        hotel_data = json.load(f)
    for item in hotel_data:
        item["price"] = int(item["price"].strip("$S ").replace(',', ''))
    hotel_data = sorted(hotel_data, key=lambda x: x["price"])
    i = 1
    while i < len(hotel_data):
        if hotel_data[i]["name"] == hotel_data[i - 1]["name"]:
            hotel_data.pop(i)
            i -= 1
        i += 1
    covid_data = covid_data["sz"]["aggregatedObj"]
    covid_data = sorted(covid_data.items(), key=lambda x: x[1])
    hotel_list_with_risk_level = []
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
            location = item["location"].replace(", Singapore", "").upper()
            if location in region_map:
                location = region_map[location]
            if item["review"] == "":
                item["review"] = 10
            review = float(item["review"])
            if region == location:
                hotel_list_with_risk_level.append(dict(item))
                hotel_list_with_risk_level[len(hotel_list_with_risk_level) - 1]["location"] = location
                hotel_list_with_risk_level[len(hotel_list_with_risk_level) - 1]["risk_level"] = covid_risk
                hotel_list_with_risk_level[len(hotel_list_with_risk_level) - 1]["review"] = review
    hotel_list_recommendation = []
    last = 0
    for i in range(len(hotel_list_with_risk_level)):
        flag = False
        for j in range(last, i):
            if hotel_list_with_risk_level[i]["review"] <= hotel_list_with_risk_level[j]["review"]:
                flag = True
                break
        if i > 0 and hotel_list_with_risk_level[i]["risk_level"] != hotel_list_with_risk_level[i - 1]["risk_level"] and len(hotel_list_recommendation) >= 10:
            break
        if not flag:
            hotel_list_recommendation.append(hotel_list_with_risk_level[i])
        if i < len(hotel_list_with_risk_level) - 1 and hotel_list_with_risk_level[i]["location"] != hotel_list_with_risk_level[i + 1]["location"]:
            last = i + 1
    with open(daily_recommendation_json, 'w', encoding='utf-8') as f:
        f.write(json.dumps(hotel_list_recommendation, ensure_ascii=False))
    with open(hotel_data_json, 'w', encoding='utf-8') as f:
        f.write(json.dumps(hotel_list_with_risk_level, ensure_ascii=False))

def generate_areas():
    hotel_data = None
    with open(hotel_data_json, 'r', encoding='utf-8') as f:
        hotel_data = json.load(f)
    area_data = None
    with open(area_data_raw, 'r', encoding='utf-8') as f:
        area_data = json.load(f)
    area_data_list = []
    for area in area_data:
        occurred = False
        for item in hotel_data:
            if item["location"] == area:
                occurred = True
                break
        if occurred:
            area_data_list.append(area)
    with open(area_data_output, 'w', encoding='utf-8') as f:
        f.write(json.dumps(area_data_list, ensure_ascii=False))

def main():
    fetch_hotel_data()
    convert_to_json()
    generate_daily_recommendations_and_standardize_data()
    generate_areas()
    
main()