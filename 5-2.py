# import urllib.request, json
#
# # Opening a web request
# url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=n&apiKey=faf40cd9190d9127fd68")
# # Decoding response to str
# data = json.loads(url.read().decode()) # Decoding a web request
#
# # Parsing results
# results = data['results']
# USD_ILS = results['USD_ILS']
# exchange = USD_ILS['val']
#
# print("Welcome to currency converter")
# # check the input with exception for valid number
# while True:
#     try:
#         num_of_shekel = int(input("Please enter an amount of Shekeles to convert: "))
#         break
#     except ValueError:
#         print("Please enter valid number")
#
# print("The exchange will be: ", num_of_shekel / float(exchange), "US Dollar")
# print("Thanks for using our currency converter")
# 123456789
# 33

import urllib.request, json
def get_data_from_url(url):
    url_object = urllib.request.urlopen(url)
    data = json.loads(url_object.read().decode())  # Decoding a web request
    return data.get('results', [])


u = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Jerusalem&key=AIzaSyD2she6rJGiE9vDeJnEkl6hbwq6KheCXgE"
results = get_data_from_url(u)
try:
    location = results[0].get('geometry', {}).get('location', {})
    lat = location.get('lat')
    lng = location.get('lng')
    print('lat=',lat,'\nlng=',lng)
except IndexError:
    print('Empty list')