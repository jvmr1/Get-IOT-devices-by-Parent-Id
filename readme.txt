Get IOT devices by Parent Id > Coding
REST API
Back-End Development
Medium
JSON

QUESTION DESCRIPTION

In this challenge, the REST API contains information about a collection of IoT devices. Given the status query and the identifier of the parent device, the goal is to use the API to get the average rotor speed of available IoT devices with the status containing given status query and having their parent identifier matching the given parent identifier.

To access the collection of devices with some status perform HTTP GET request to:
https://jsonmock.hackerrank.com/api/iot_devices/search?status=<statusQuery>&page=<pageNumber> where <statusQuery> is a string such that all devices having <statusQuery> as a substring of their status value (using case-insensitive matching) will be included in the result and <pageNumber> is integer denoting the page of the results to return.

For example, GET request to:
https://jsonmock.hackerrank.com/api/iot_devices/search?status=STOP&page=2 will return the second page of the devices with their status containing "STOP" as a substring (using case-insensitive matching) of their statuses. Pages are numbered from 1, so in order to access the first page, you need to ask for page number 1.

The response to such request is a JSON with the following 5 fields:

page : The current page of the results
per_page : The maximum number of devices returned per page.
total : The total number of devices available on all pages of the result.
total_pages : The total number of pages with results.
data : An array of objects containing devices returned on the requested page

Each device object has the following schema:

id : The unique ID of the device
timestamp : The timestamp when the device was added to the collection, in UTC milliseconds
status : The status of the device
operatingParams : the object containing operating parameters of the device
asset : The object containing information about the asset of the device
parent : Optional. The object containing information about the parent of the device

The operating parameters object has the following schema:

rotorSpeed : The rotor speed of the device
slack : The slack in the device
rootThreshold : The root threshold for the device

The asset object has the following schema:

id: The unique ID of the asset
alias : The alias for the asset

The parent object has the following schema:

id : The unique ID of the parent of the asset
alias : The alias for the parent of the asset

Given string statusQuery, and numerical parentId value, the goal is to return the average rotor speed, rounded down to integer value, of all devices that have statusQuery as a substring of their status (using case-insensitive matching) and having their parent identifier matching the parentId value. If there are no devices matching the given criteria, the result must be 0.

Function Description
Complete the function avgRotorSpeed in the editor below.

avgRotorSpeed has the following parameter(s):

statusQuery: string denoting the substring of devices status to query for
parentId: integer denoting the identifier of the parent of devices to query for

The function must return an integer denoting the average rotor speed of matching devices rounded down to integer value. If there are no devices matching the given criteria, the function must return 0.
