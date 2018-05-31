# geolocatethis

Idea came to life during geolocation of a picture taken in unknown location. I thought it would be very helpful to ask google maps to find "all restaurants in area with maximum distance of 30 metres from newspaper kiosk". So I've written simple python script that allows querying Google Maps API for 2 specific places within precise distance from each other in given area.
<br>
<br>
<h3>DATA INPUTS:</h3>

<b>Latitude and Logtitude</b> - points to the center of the search circle. For best results give closest approximate coordinates to place you are trying to find.  

<b>Radius</b> - Defines radius for area to search from given above coordinates. The maximum allowed radius is 50 000 meters. Because of Google Maps advertising policy, sometimes one or two places can be included from outside of the given radius.

<b>Keyword</b> - A term to be matched against all content that Google has indexed for this place, including but not limited to name, type, and address, as well as customer reviews and other third-party content.

<b>Category</b> - Restricts the results to places matching the specified type. Only one type may be specified (if more than one type is provided, all types following the first entry are ignored). See the list of <a href='https://developers.google.com/places/web-service/supported_types'> allowed categories </a>.

<b>Distance</b> - Number (in metres) defines distance beetwen to searched places (landmarks).
<br>
<br>
<h3>HOW TO RUN IT?</h3>
Min. required python version: 3.6

Copy all files (including 'assets' folder) to your disk. Remeber to paste your API Google Map key into 'assets/auth_key.py' file.

Run script with command: <i>python geolocatethis.py</i>

While searching program prints out coordinates of places that met previously given criteria.
<br>
<br>
<h3>USE EXAMPLE:</h3>
Let's assume we need to geolocate this photo:
<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Apotheke_an_der_Alten_Schule_in_Berlin-Adlershof.JPG/640px-Apotheke_an_der_Alten_Schule_in_Berlin-Adlershof.JPG'>

All we know it was taken somewhere in <a href='https://www.google.pl/maps/@52.4139645,13.5292603,13z'> southern Berlin near Schonefeld</a>.
On the photo, there is a pharmacy and a small shop with Deutsche Post sing above the door. That is enough information to run program.

There are 4 parts of the city where photo potentially could have been taken: Rudow, Adlershof, Altglienicke, and Bohnsdorf. The best place to place marker for center point would be somewhere around State Park (52.415430, 13.526943).

Next, we should type in following data:<br>
<ul>
  <li>Radius = 8000m (distance between the center point and edge of every adjacent neighborhood).</li>
  <li>A keyword for place 1 = 'pharmacy' (best to use a word in English as this is the main language of Google Maps database)</li>
  <li>Category for place 1 = 'pharmacy' (limit search only to actual pharmacies)</li>
  <li>A keyword for place 2 = 'post' (you can type in multiple keywords, however, in this case, is better to give a more general description as we don't know how this shop is described in google maps).</li>
  <li>Category for place 2 = 'store' (it will limit search only to stores with 'post' related keyword)</li>
  <li>Distance = 10m (rough estimate from photo)</li>
</ul>
Result gives 20 positive matches. In the same area, Google Map search shows over 60 pharmacies. It means three times less work to do on google street view.

...and yes, our pharmacy is in results ;)
