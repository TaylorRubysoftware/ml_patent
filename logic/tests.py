import unittest
import json

from search import *
from generate_hash import *


class TestSearchMethods(unittest.TestCase):
    def setUp(self):
        self.database = [
            {'name': "Storage device", 'id': "028319334", 'hash': [0.1, 0.1, 0.1, 0.1], 'cat': [['A', '77']]},
            {'name': "Insulating conductor bars", 'id': "1289189334", 'hash': [0.4, 0.4, 0.4, 0.4], 'cat': [['B', '11'], ['C', '12']]},
            {'name': "Ceramic coatings", 'id': "1289189334", 'hash': [0.8, 0.8, 0.8, 0.8], 'cat': [['A', '12'], ['A', '12']]}
        ]

    def test_find_closest_patents_returns_given_number_of_patents(self):
        hash = [0.1, 0.1, 0.1, 0.2]
        results = find_closest_patents(self.database, hash, patents=2)
        self.assertEqual(len(results), 2)

    def test_find_closest_patents_returns_patents_sorted_by_distance(self):
        hash = [0.4, 0.4, 0.4, 0.1]
        [patent_a, patent_b] = find_closest_patents(self.database, hash, patents=2)
        self.assertTrue(patent_a['dist'] < patent_b['dist'])
        self.assertEqual("Insulating conductor bars", patent_a['name'])
        self.assertEqual("Storage device", patent_b['name'])

    def test_hash_distance_is_calculated_in_euclidean_space(self):
        hash_a = [0.1, 0.1, 0.1, 0.2]
        hash_b = [0.1, 0.3, 0.1, 0.1]
        distance = calculate_distance(hash_a, hash_b)
        self.assertEqual(np.sqrt(0.05), distance)

    def test_create_dictionary_creates_dictionary_with_zero_values(self):
        words = ['foo', 'bar', 'foobar']
        dictionary = create_dictionary(words)
        self.assertEqual(len(dictionary), len(words))
        self.assertEqual(dictionary['bar'], 0)

    def test_create_bag_of_words_stems_words(self):
        bow = create_bag_of_words(['sleep', 'direct'], ['sleeping', 'direction', 'direct'])
        self.assertEqual(bow['sleep'], 1)
        self.assertEqual(bow['direct'], 2)

    def test_url_generation(self):
        id = "03D889"
        service = "http://domain.com/service/"
        url = generate_url(service, id)
        self.assertEqual("http://domain.com/service/3D889.pdf", url)


if __name__ == '__main__':
    unittest.main()
