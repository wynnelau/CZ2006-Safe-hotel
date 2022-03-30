from matplotlib.pyplot import hot
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
        
    return "https://www.booking.com/searchresults.en-gb.html?label=singapore-WzGdqcC1K4*NWFxkuYSqNAS380872793965%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-297601666555%3Akwd-307297810028%3Alp9062546%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfpWGnRw6lOGgfEoJVv7zYo&sid=aaf90ef021878f54ad97898b3e923abf&aid=1610687&lang=en-gb&sb_lp=1&src=index&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Faid%3D1610687%3Blabel%3Dsingapore-WzGdqcC1K4%252ANWFxkuYSqNAS380872793965%253Apl%253Ata%253Ap1%253Ap2%253Aac%253Aap%253Aneg%253Afi%253Atiaud-297601666555%253Akwd-307297810028%253Alp9062546%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YfpWGnRw6lOGgfEoJVv7zYo%3Bsid%3Daaf90ef021878f54ad97898b3e923abf%3Bsb_price_type%3Dtotal%3Bsrpvid%3Dfb8958792a44012a%26%3B&ss=Singapore&is_ski_area=0&ssne=Singapore&ssne_untouched=Singapore&dest_id=-73635&dest_type=city&" + \
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
        for i in range(0, 250, 26):
            data = scrape(url + "&offset=" + str(i))
            if data:
                for h in data['hotels']:
                    writer.writerow(h)

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
    covid_data = covid_data["sz"]["aggregatedObj"]
    covid_data = sorted(covid_data.items(), key=lambda x: x[1])
    hotel_list_with_risk_level = []
    truncate_point = -1
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
            price = int(item["price"].strip("$S ").replace(',', ''))
            if region == location:
                hotel_list_with_risk_level.append(dict(item))
                hotel_list_with_risk_level[len(hotel_list_with_risk_level) - 1]["location"] = location
                hotel_list_with_risk_level[len(hotel_list_with_risk_level) - 1]["price"] = price
                hotel_list_with_risk_level[len(hotel_list_with_risk_level) - 1]["risk_level"] = covid_risk
        if i >= 5 and len(hotel_list_with_risk_level) >= 10 and truncate_point == -1:
            truncate_point = len(hotel_list_with_risk_level)
    with open(daily_recommendation_json, 'w', encoding='utf-8') as f:
        f.write(json.dumps(hotel_list_with_risk_level[0:truncate_point], ensure_ascii=False))
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
            location = item["location"].strip(", Singapore").upper()
            if location == area:
                occurred = True
                break
        if occurred:
            area_data_list.append(area)
    with open(area_data_output, 'w', encoding='utf-8') as f:
        f.write(json.dumps(area_data_list, ensure_ascii=False))

def main():
    fetch_hotel_data()
    convert_to_json()
    generate_areas()
    generate_daily_recommendations_and_standardize_data()
    
main()