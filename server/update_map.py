import requests
import json
import os
from server.utils import *

if not os.path.exists("src/data"):
    os.mkdir("src/data")

def fetch_data():
    session = requests.session()
    calcAggOutput = session.get(map_data_url)
    return calcAggOutput

def convert_to_stringified_json(calcAggOutput):
    js_contents = calcAggOutput.content.decode('utf-8')
    js_contents = js_contents[18:-1]
    return js_contents

def generate_image(features, svg_contents):
    ordered_regions = {}
    for region in features:
        properties = region["properties"]
        ordered_regions[properties["SUBZONE_N"]] = properties["COUNT"]
    map_image_contents = []
    index = 0
    while not svg_contents[index].startswith("<g"):
        map_image_contents.append(svg_contents[index])
        index += 1
    while index < len(svg_contents):
        region = svg_contents[index][7:-3]
        map_image_contents.append(svg_contents[index])
        index += 1
        while not svg_contents[index].startswith("</g"):
            sentence = svg_contents[index].split("path")
            index += 1
            map_image_contents.append(sentence[0] + 'path fill="rgb(255, ' + str(255 - min(ordered_regions[region] // 2, 255)) + ", " + str(255 - min(ordered_regions[region] // 2, 255)) + ')" ' + sentence[1])
        map_image_contents.append(svg_contents[index])
        index += 1
    map_image_file = open(map_output_url, "w")
    map_image_file.writelines(map_image_contents)

def write_to_vue():
    with open(vue_input_url, "r", encoding='utf-8') as infile, open(vue_output_url, "w", encoding='utf-8') as outfile:
        lines = infile.readlines()
        output = []
        for line in lines:
            output.append(line)
            if '<svg @mouseenter="loadMap" class="map" xmlns="http://www.w3.org/2000/svg" version="1.2" baseProfile="tiny" viewBox="0 0 800 518" fill="white" stroke="black" stroke-linecap="round" stroke-linejoin="round">' in line:
                with open(map_output_url, "r", encoding='utf-8') as f:
                    svg_contents = f.readlines()
                    for svg_line in svg_contents:
                        output.append(svg_line)
        outfile.writelines(output)

def main():
    calcAggOutput = fetch_data()
    calcAggOutputContents = calcAggOutput.content.decode('utf-8')
    calcAggOutputContents += "\nexport default calcAggOutput;"
    with open(map_data_path, "w") as f:
        f.writelines(calcAggOutputContents)
    json_stringify_contents = convert_to_stringified_json(calcAggOutput)
    json_file = open(json_file_url, "w")
    json_file.writelines(json_stringify_contents)
    json_file = open(json_file_url, "r")
    json_contents = json.load(json_file)
    sz = json_contents["sz"]
    geojsonObj = sz["geojsonObj"]
    features = geojsonObj["features"]
    map_image_file = open(map_image_url, "r")
    svg_contents = map_image_file.readlines()
    generate_image(features, svg_contents)
    write_to_vue()

main()