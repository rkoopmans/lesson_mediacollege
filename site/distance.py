import urllib
import json


def get_distance(location_a, location_b):
    params = urllib.urlencode({'origins': location_a, 'destinations': location_b})
    response = urllib.urlopen('https://maps.googleapis.com/maps/api/distancematrix/json?%s' % params)
    return json.loads(response.read())
