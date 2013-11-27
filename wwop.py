#!/usr/bin/python
# -*- coding: utf-8 -*-

# www.worldweatheronline.com parser. Useful for conky and any other
# system monitors. You have to provide city and API key. API key you
# will get after registering on above-mentioned site.

import os, sys, json, urllib.request as urler, configparser, datetime

# Config file path
config_path = os.path.join(os.path.expanduser("~/.config/wwop/"))

weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def parse_parameters(params):
    if "--download" in params:
        download_data()
    else:
        parse_data(params)

def download_data():
    config = configparser.ConfigParser()
    config.read(config_path + "/config")
    API_KEY = config["main"]["API_KEY"]
    CITY = config["main"]["CITY"]
    DAYS = config["forecast"]["DAYS"]
    
    data = urler.urlopen("http://api.worldweatheronline.com/free/v1/weather.ashx?q={0}&fx=yes&cc=yes&format=json&num_of_days={1}&key={2}".format(CITY, DAYS, API_KEY)).read().decode('utf-8')
    data = json.loads(data)
    f = open(os.path.expanduser("~/.config/wwop/cache"), "w")
    f.write(json.dumps(data))
    f.close()
    
def parse_data(params):
    # Parsing config variables
    config = configparser.ConfigParser()
    config.read(config_path + "/config")
    try:
        TEMP_TYPE = config["forecast"]["TEMP_TYPE"]
    except:
        TEMP_TYPE = "C"
        
    if TEMP_TYPE == "C":
        TEMP_SIGN = "°C"
    else:
        TEMP_SIGN = "°F"
    
    # Loading translations
    path = os.path.abspath(os.path.dirname(__file__))
    try:
        LANGUAGE = config["forecast"]["LANGUAGE"]
        lang = json.loads(open("{0}/translations/{1}.json".format(path, LANGUAGE)).read())
    except:
        pass
    
    f = open(config_path + "/cache")
    data = f.read()
    f.close()
    data = json.loads(data)
    data = data["data"]
    if "-c" in params:
        data = data["current_condition"][0]
        if "temp" in params:
            print(data["temp_{0}".format(TEMP_TYPE)] + TEMP_SIGN)
        if "cond" in params:
            try:
                print(lang[data["weatherDesc"][0]["value"]])
            except:
                print(data["weatherDesc"][0]["value"])
        exit()
    elif "-d" in params:
        data = data["weather"][int(params[1]) - 1]

    if "cond" in params:
        try:
            print(lang[data["weatherDesc"][0]["value"]])
        except:
            print(data["weatherDesc"][0]["value"])
    elif "mintemp" in params:
        print(data["tempMin{0}".format(TEMP_TYPE)] + TEMP_SIGN)
    elif "maxtemp" in params:
        print(data["tempMax{0}".format(TEMP_TYPE)] + TEMP_SIGN)
    elif "dof" in params:
        day = data["date"].split("-")
        weekday = datetime.date(int(day[0]), int(day[1]), int(day[2])).weekday()
        try:
            print(lang[weekdays[weekday]])
        except:
            print(weekdays[weekday])
    
if __name__ == "__main__":
    parse_parameters(sys.argv[1:])
    
    

