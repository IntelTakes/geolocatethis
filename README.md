# find2places

Idea came to life during geolocation of a picture taken in unknown location. I thought it would be very helpful to ask google maps to find "all restaurants in area with maximum distance of 30 metres from newspaper kiosk". So I've written simple python script that allows querying Google Maps API for 2 specific places within precise distance from each other in given area. 
<br>

<h3>DATA INPUTS:</h3>

<b>Latitude and Logtitude</b> - points to the center of the search circle. For best results give closest approximate cooridnates to place you are trying to find.  

<b>Radius</b> - Defines radius for area to search from given above coordinates. The maximum allowed radius is 50 000 meters. Because of Google Maps advertising policy, sometimes one or two places can be included from outside of the given radius. 

<b>Keyword</b> - A term to be matched against all content that Google has indexed for this place, including but not limited to name, type, and address, as well as customer reviews and other third-party content.

<b>Category</b> (type of place) - Restricts the results to places matching the specified type. Only one type may be specified (if more than one type is provided, all types following the first entry are ignored). See the list of <a href='https://developers.google.com/places/web-service/supported_types'> allowed categories </a>.

<b>Distance</b> - Number (in metres) defines distance beetwen to searched places (landmarks). 

