import json, requests, sys

sys.path.append('.')
sys.path.append('./assets')

from auth_key import *
from api_data import *
from art import ascii_art, welcome_text


#Function handling requests to Google Maps API 
def send_request(location, radius, keyword, category, pagetoken = None):

        params = {
                'location': location,
                'radius': radius,
                'type': category,
                'keyword': keyword,
                'key': AUTH_KEY,
        }

        if pagetoken is not None:
                params['pagetoken'] = pagetoken

        response = requests.get(api_url, params=params)
    
        if response.status_code == 200:
                raw_data = json.loads(response.content)
                
        else:
                print ('Something went wrong. Error code: {}'.format(response.status_code))
                exit
                
        return raw_data


# Main searching function     

def geo_locate_this():
        pagetoken = None
        blank_pagetoken = None
        match_count = 0
        
        while True:
                place_1_data = send_request(center_point, radius, keyword_place_1, category_place_1, pagetoken)
                        
                if 'OK' in place_1_data['status']:
                        for result in place_1_data['results']:
                                temp_name = result['name']
                                temp_lat = result['geometry']['location']['lat']
                                temp_lng = result['geometry']['location']['lng']
                                temp_location = '{},{}'.format(temp_lat,temp_lng)
                                
                                place_2_data = send_request(temp_location, distance, keyword_place_2, category_place_2, blank_pagetoken)
                                if 'ZERO_RESULTS' not in place_2_data['status']:
                                        print ("Found match at {} (location: {})".format(temp_name, temp_location))
                                        match_count += 1     
                                
                        if 'next_page_token' not in place_1_data:
                                print ('Done. Found {} locations matching given criteria.'.format(match_count))
                                break
                
                        else:
                                pagetoken = place_1_data['next_page_token']        
                
                elif 'ZERO_RESULTS' in place_1_data['status']:
                        print('Sorry, no results with provided parameters')
                        break                
                
                elif 'OVER_QUERY_LIMIT' in place_1_data['status']:
                        print('You have reached your daily API quota limit for this key.')
                        break
                
                elif 'REQUEST_DENIED' in place_1_data['status']:
                        print('Request to Google API denied. Check your API key.')
                        break                
                
        return  

#
# Main program #
#
print(ascii_art)
print()
print(welcome_text)
print()


print('Define center point of searched area.')
lat = input('[+]Latitude: ')
lon = input('[+]Longtitude: ')
center_point = ('{},{}'.format(lat,lon))
radius = input("[+]Search radius from above given coordinates [in metres, max. 50000]: ")

keyword_place_1 = input("[+]Keyword for place 1: ")

while True:
        category_place_1 = input("[Optional] Choose category for place 1 to narrow search. Type 'help' for complete list of allowed categories [enter for None]: ")
        if category_place_1 == 'help':
                print(place_types)
        elif category_place_1 == "":
                break
        elif category_place_1 not in place_types:
                print('Invalid category. Try again.')
        else:
                break


keyword_place_2 = input("[+]Keyword for place 2: ")

while True:
        category_place_2 = input("[Optional] Choose category for place 2 to narrow search. Type 'help' for complete list of allowed categories [enter for None]: ")
        if category_place_2 == 'help':
                print(place_types)
        elif category_place_2 == "":
                break
        elif category_place_2 not in place_types:
                print('Invalid category. Try again.')
        else:
                break

distance = input("[+]Distance beetwen place 1 and place 2 [m]: ")
print('searching...')
geo_locate_this()


