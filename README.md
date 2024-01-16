# CZ2006-SafeHotel

Group project done in Year 2 Sem 1

• Drafted the Software Requirements Specification (SRS), which includes the use case description and the sequence diagram, to better show how the system works to both users and developers.  
• Extracted information of required hotels by scraping a hotel booking website using Python and SelectorLib to ensure that users have access to updated prices of hotel rooms.

## Prerequisite
```
npm >= 8.1.2
python >= 3.6
```

## First Time Running
```
pip install -r requirements.txt
npm install # optional
```

## Run the Project
```
python main.py
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Framework
```
/src: this folder stores data and frontend codes;
    /src/assets: static data;
    /src/components: frontend Vue components, may be involved in multiple use cases;
    /src/data: volatile data;
    /src/network: define the rules communicating frontend and backend;
    /src/router: define the url of each page;
    /src/view: main web pages (use cases) in the project;
/server: this folder stores backend codes;
    /server/flask_app.py: flask app, implementing the "filter" use case functional requirements;
    /server/update_hotel.py: periodically fetch hotel data to /src/data;
    /server/update_map.py: periodically fetch covid data to /src/data;
    /server/utils.py: general variables and functions to be used.
```
