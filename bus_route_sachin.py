import json, sys
import urllib.request as urllib
from operator import itemgetter


DISTANCE_MATRIX_BASE_URL = "http://maps.googleapis.com/maps/api/distancematrix/json?origins="

ORIGINS = []
ORIGINS.append(sys.argv[1].replace(" ","+") )

DESTINATIONS = [ "Divisadero+and+Lombard",
            "Lombard+and+Filmore",
            "Van+Ness+and+Union",
            "Van+Ness+and+Pacific",
            "Van+Ness+and+Pine",
            "Van+Ness+and+Geary",
            "Van+Ness+and+Eddy",
            "Van+Ness+and+Oak",
            "Mission+and+15th",
            "Valencia+and+16th",
            "Valencia+and+24th",
            "Cesar+Chavez+and+Florida",
            ]

ORIGIN_PARAMS = '|'.join( [''.join([origin, "+San+Francisco"]) for origin in ORIGINS] )
DESTINATION_PARAMS = '|'.join( [''.join([dest, "+San+Francisco"]) for dest in DESTINATIONS] )

URL = DISTANCE_MATRIX_BASE_URL + ORIGIN_PARAMS + '&destinations=' + DESTINATION_PARAMS + "&mode=walking&sensor=false"

def get_min_distance_point():
    result = urllib.urlopen(URL)
    encoding = result.headers.get_content_charset()
    result = json.loads(result.read().decode(encoding))

    if result['origin_addresses'] == ['San Francisco, CA, USA']:
        print("Badly formated origin address")
        exit(-1)

    elems = [ row['elements'] for row in result['rows'] ]
    min_dist = float('inf')
    min_source = ''
    min_dest = ''

    all_routes = []

    for i in range(0, len(elems)):
        source = ORIGINS[i]
        current_elem = elems[i]

        for j in range(0, len(current_elem)):
            my_dict = current_elem[j]

            dest = DESTINATIONS[j]
            all_routes.append( (source, dest, my_dict['distance']['value'], my_dict['duration']['text']) )

            if my_dict['distance']['value'] < min_dist:
                min_dist = my_dict['distance']['value']
                min_source = source
                min_dest = dest

        #if elem[1][1]> min_dist:
         #   min_dist = elem['distance']['value']

    all_routes.sort(key= itemgetter(2) )

    for route in all_routes:
        print ( "%(time)s walk to %(stop)s" % { "time" : route[3], "stop" : route[1].replace("+"," ")} )

get_min_distance_point()
