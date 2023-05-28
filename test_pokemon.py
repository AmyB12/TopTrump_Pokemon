from pokemon_api_project.Pokemon_TopTrump.rest_pokemon import *
import unittest
import requests


class idTest(unittest.TestCase):

    def test_id_between_1_and_151(self):
        id_made = create_id()
        self.assertGreaterEqual(id_made, 1, "Wrong")
        self.assertLessEqual(id_made, 151, "Wrong")

    def get_pokemon_status(self):
        requested = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(create_id()))
        expect = requested.json()
        actual = get_pokemon()
        self.assertEqual(expect, actual, "Wrong Stuff")


if __name__ == "__main__":
    unittest.main(defaultTest="id_test.test_id_between_1_and_151", exit=False)

