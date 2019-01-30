# Flight Status

My flight to NYC from HTX got delayed a while, so I threw this together. 

# How to Use

You'll need to sign up for <a href='http://flightxml.flightaware.com/soap/FlightXML2/doc'>FlightAware's API</a>. It's basically free per request, especially with tiny queries like this. Register and get an API key. 

A list of <a href="https://flightaware.com/commercial/flightxml/explorer/#op_FlightInfo">endpoints</a> available is here, but we'll just use the `FlightInfo` module. 

# Notes

The only hard part here is picking out the data needed from the full JSON response from `FlightInfo`. Hella gross. You might find some of this useful, but I only needed a few of these. It'll look something like this: 

```
{'FlightInfoResult': {'next_offset': 1, 'flights': [{'ident': 'SWA1662', 'aircrafttype': 'B737', 'filed_ete': '03:00:00', 'filed_time': 1548829550, 'filed_departuretime': 1549044600, 'filed_airspeed_kts': 414, 'filed_airspeed_mach': '', 'filed_altitude': 0, 'route': '', 'actualdeparturetime': 0, 'estimatedarrivaltime': 1549055400, 'actualarrivaltime': 0, 'diverted': '', 'origin': 'KHOU', 'destination': 'KLGA', 'originName': 'William P Hobby', 'originCity': 'Houston, TX', 'destinationName': 'LaGuardia', 'destinationCity': 'New York, NY'}]}}
```
