# find2places
Allows querying Google Maps API for 2 specific places in precise distance from each other within given radius. Useful for geolocating from photographs. 

<b>PARAMETERS:</b>

Latitude and Logtitude - points to the center of the search circle. For best results give closest approximate cooridnates to place you are trying to find.  

Defines the distance (in meters) within which to bias place results.  however, prominent results from outside of the search radius may be included.

Radius - Defines radius for area to search from given above coordinates. The maximum allowed radius is 50 000 meters. Because of Google Maps advertising policy, sometimes one or two places can be included from outside of the given radius. 

Keyword - A term to be matched against all content that Google has indexed for this place, including but not limited to name, type, and address, as well as customer reviews and other third-party content.

Category (type of place) - Restricts the results to places matching the specified type. Only one type may be specified (if more than one type is provided, all types following the first entry are ignored). See the list of <a href='https://developers.google.com/places/web-service/supported_types'> allowed categories </a>.

Distance - Number (in metres) defines distance beetwen to searched places (landmarks). 
