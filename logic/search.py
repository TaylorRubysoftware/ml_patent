
import numpy as np

def find_closest_patents(database, hash, patents=3):
    distances = np.array(map(lambda patent: calculate_distance(patent['hash'], hash), database))
    indices = distances.argsort()[:patents]
    found_patents = map(database.__getitem__, indices)

    def addDist(patent, dist):
        patent['dist'] = dist
        return patent

    return map(addDist, found_patents, distances[indices])

def calculate_distance(first, second):
    return np.linalg.norm(np.subtract(first, second))

def generate_url(service, id):
    while id[0] == '0':
        id = id[1:]
    return service + id + ".pdf"