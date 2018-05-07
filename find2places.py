import json, requests, sys, time

sys.path.append('.')
sys.path.append('./assets')

from auth_key import *
from api_data import *
from art import ascii_art, welcome_text

#Function handling requests to Google Maps API 
def send_request(location, radius, landmark, keyword, pagetoken = None):

        params = {
                'location': location,
                'radius': radius,
                'type': landmark,
                'keyword': keyword,
                'key': AUTH_KEY,
        }

        if pagetoken is not None:
                params['pagetoken'] = pagetoken

        response = requests.get(api_url, params=params)
    
        if response.status_code == 200:
                raw_data = json.loads(response.content)
                time.sleep(1)
                
        else:
                print ('Something went wrong. Error code: {}'.format(response.status_code))
                exit
                
        return raw_data
  
# Main searching function        
def check_primary_and_secondary():
        pagetoken = None
        blank_pagetoken = None
        match_count = 0
        
        while True:
        
                landmark_data = send_request(center_point, radius, landmark1_type, landmark1_keyword, pagetoken)

                for result in landmark_data['results']:
                        temp_name = result['name']
                        temp_lat = result['geometry']['location']['lat']
                        temp_lon = result['geometry']['location']['lng']
                        temp_location = '{},{}'.format(temp_lat,temp_lon)
                        secondary_landmark_results = send_request(temp_location, distance, landmark2_type, landmark1_keyword, blank_pagetoken)
                        if 'ZERO_RESULTS' not in secondary_landmark_results['status']:
                                print ("Found match at {} (location: {})".format(temp_name, temp_location))
                                match_count += 1
                                
                if 'next_page_token' not in landmark_data:
                        break
                
                else:
                        pagetoken = landmark_data['next_page_token']        
                
        return match_count

# Main program #
print(ascii_art)
print()
print(welcome_text)
print()


print('From which point do you want to start searching?')
lat = input('Latitude: ')
lon = input('Longtitude: ')
center_point = ('{},{}'.format(lat,lon))
radius = input("Search radius from above given coordinates [m]: ")

landmark1_keyword = input("Keyword for landmark no.1: ")

while True:
        landmark1_type = input("[Optional] Choose category for landmark no.1 to narrow search. Type 'help' for complete list of allowed categories [enter for None]: ")
        if landmark1_type == 'help':
                print(place_types)
        elif landmark1_type == "":
                break
        elif landmark1_type not in place_types:
                print('Invalid category. Try again.')
        else:
                break


landmark2_keyword = input("Keyword for landmark no.2: ")

while True:
        landmark2_type = input("[Optional] Choose category for landmark no.2 to narrow search. Type 'help' for complete list of allowed categories [enter for None]: ")
        if landmark2_type == 'help':
                print(place_types)
        elif landmark2_type == "":
                break
        elif landmark2_type not in place_types:
                print('Invalid category. Try again.')
        else:
                break

distance = input("Distance beetwen landmark no.1 and no.2 [m]: ")

final_count = check_primary_and_secondary()

print ('Done. Found {} locations matching given criteria.'.format(final_count))
