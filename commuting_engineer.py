import sys
import math
from sets import Set

distance_dict = {}

class Graph:
    vertices = []
    edges = []

    def __init__ (self, vertices = [], edges = []):
        self.vertices = vertices
        self.edges = edges

    def add_v(self, vertex):
        self.vertices.append(vertex)

    def add_e(self, edge):
        self.edges.append(edge)

    def get_distance(self, source, dest):
        for e in g.edges:
            if e[0] == (source, dest):
            	return e[1]



def min_dist(path, end, graph):
    for v in path:
        if v[0] is not end:
            pass
    return 1

def traverse(source, graph):
    for key in distance_dict.keys:
        path = distance_dict[key][0]
        for v in [x for x in graph if x not in path]:
        	distance_dict[(path, v)] = min_dist(path, v, graph)

def distance_on_unit_sphere(source, dest):

    lat1, long1 = source.split(',')
    lat1, long1 = float ( lat1.strip() ), float( long1.strip() )

    lat2, long2 = dest.split(',')
    lat2, long2 = float ( lat2.strip() ), float( long2.strip() )

    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0

    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians

    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians

    # Compute spherical distance from spherical coordinates.

    # For two locations in spherical coordinates
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) =
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length

    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
    math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    return arc

#Check for correct number of arguments
if len(sys.argv) is not 2:
    sys.exit('Wrong Argument Length. Usage: python sum.py [filename]')

filename = sys.argv[1]

#Open file and read in lines, exit if file does not exist
try:
    with open(filename) as f:
        lines = f.readlines()
except IOError:
    exit('File ' + filename + ' does not exist')


def parse(line):
    vertex_id = line.split('|')[0].strip()
    vertex_coords = line.split('(')[1][:-2]
    return vertex_id, vertex_coords

#For each line
g = Graph()

for line in lines:
    s = line.strip()
    g.add_v(parse(line))

for source in g.vertices:
    g.add_e( ( ( source[0], source[0]), 0.0) )
    for dest in g.vertices:
        if source is not dest:
        	g.add_e( ( (source[0],dest[0]), distance_on_unit_sphere(source[1], dest[1]) ) )

print g.get_distance('1','2')

exit(0)
