import json

map_data_url = "https://d209m3w127yzkd.cloudfront.net/data/calcAggOutput.js"
map_data_path = "src/components/map/calcAggOutput.js"
map_image_url = "src/assets/img/map_initial.svg"
map_output_url = "src/data/map.svg"
json_file_url = "src/data/data.json"
vue_input_url = "src/components/map/MapImg.source"
vue_output_url = "src/components/map/MapImg.vue"

booking_data = 'src/assets/booking.yml'
hotel_data_csv = 'src/data/hotel_data.csv'
hotel_data_json = 'src/data/hotel_data.json'
daily_recommendation_json = 'src/data/recommendation.json'
area_data_raw = 'src/assets/area.json'
area_data_output = 'src/data/area.json'

region_map_url = 'src/assets/region_map.json'

region_map = None
with open(region_map_url, 'r', encoding='utf-8') as f:
    region_map = json.load(f)