# Microservice
Microservice implementation for CS 361. Takes a string value encoded in utf-8 of a specified state and returns the highest temperature recorded in that location. Then, it passes back that data to the client as an integer to be converted from fahrenheit to celsius.

# how to REQUEST data 
Send location data as a string from a selection of the following:
"Alaska", "Arizona", "California", "Colorado", "Florida", "Hawaii", "Illinois", "Maine", "Montana", "Nevada", "New York", "Oregon", "Texas", "Washington"

Send data via client.send(data.encode())

# how to RECEIVE data
Data is returned in fahrenheit as a string and needs to be converted to an integer for conversion. 
Example of returned data: "100"

[Microservice Socket UML]()
