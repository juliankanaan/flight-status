
import requests
import json
import time


def flightData() :

    # authenticate myself

    username = 'xx'
    api_key = "xx"
    baseUrl = "https://flightxml.flightaware.com/json/FlightXML2/"

    # build params
    ident = 'wn1662' # change this to your flight 
    # get only one result
    howMany = 1

    parameters = {'ident': ident, 'howMany': howMany}

    # build request

    r = requests.get(baseUrl + "FlightInfo", params=parameters, auth=(username, api_key))

    # check for good request
    if r.status_code == 200 :

        print("Good response")
        # json-ize the response
        data = r.json()
        # it's a complicated response, so just focus on the "flights'" dictionary
        flightdata = data['FlightInfoResult']['flights']

        # get dictionary info we need
        flight_num = flightdata[0]["ident"]

        dest = flightdata[0]["destinationName"]

        est_arrival = flightdata[0]["estimatedarrivaltime"]

        # print the relevant data
        print("The flight", flight_num, "to", dest, "will arrive at", time.strftime("%H:%M:%S", time.localtime(est_arrival)), "local time")



    else :
        print("The API request failed. Code", r.status_code)



flightData()
