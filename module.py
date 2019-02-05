
import requests
import json
import time



def flightData() :

    # authenticate myself

    username = 'xx'
    api_key = "xxx"
    baseUrl = "https://flightxml.flightaware.com/json/FlightXML2/"

    # build params
    ident = 'wn1662'
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
        sch_arrival = flightdata[0]["filed_time"]

        # print the relevant data
        print("The flight", flight_num, "to", dest, "will arrive at", time.strftime("%H:%M:%S", time.localtime(est_arrival)), "local time")

        print("It was supposed to arrrive at", time.strftime("%H:%M:%S", time.localtime(sch_arrival)))

    else :
        print("The API request failed. Code", r.status_code)

# is the flight late? shoot me a text
def lateCheck():

    # check for late

    if est_arrival > sch_arrival :

        # convert into real mins
        lateness = time.strftime("%H:%M:%S",est_arrival - sch_arrival )

        sendText(lateness)

def sendText(lateness):

    late = lateness

    from twilio.rest import Client


    account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = 'xxxxx'
    client = Client(account_sid, auth_token)

    text = "Your flight has been delayed"+str(lateness)

    message = client.messages \
                    .create(
                         body=text,
                         from_='fill-this-in',
                         to='fill-this-in'
                     )

    print(message.sid)


flightData()
